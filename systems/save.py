import json
from sprites.player import Player
from sprites.fish import Fish
from systems.inventory import Inventory
from Crypto.Cipher import AES
import hashlib 
import os

magic = b"VuiVeDangODay\x04"
class Save:
    """
    Xử lý việc lưu và tải dữ liệu người chơi.

    Dữ liệu bao gồm:
    - Thông tin player
    - Inventory
    - Tiến trình game

    Attributes:
        player (Player): Người chơi
        file_path (str): Đường dẫn file lưu dữ liệu
    """
    def __init__( self, player: Player, inv: Inventory, password ):
        self.player = player
        self.inv = inv
        self.password = password
    def load_all( self ):
        if not os.path.exists( "save.bin" ):
            return {"players": {}}
        with open( "save.bin", "rb") as f:
            data = f.read()
        nonce = data[: 16 ]
        tag = data[ 16: 16 + 16 ]
        ciphertext = data[ 16 + 16:]
        with open( "main.exe", "rb" ) as f:
            parts = f.read().split( magic )
        key = parts[-1]
        cipher = AES.new( key, AES.MODE_GCM, nonce = nonce )
        plaintext = cipher.decrypt_and_verify( ciphertext, tag )

        return json.loads( plaintext.decode() )
    def save_all( self, data ):
        with open( "main.exe", "rb" ) as f:
            data_exe = f.read()
        key = data_exe.split( magic )[1]
        cipher = AES.new( key, AES.MODE_GCM )
        ciphertext, tag = cipher.encrypt_and_digest( json.dumps( data ).encode() )
        nonce = cipher.nonce
        with open( "save.tmp", "wb" ) as f:
            f.write( nonce + tag + ciphertext )
        os.replace("save.tmp", "save.bin" )  

    def save_player( self ):
        """
        Lưu dữ liệu người chơi vào file.

        Ghi lại:
        - Thông tin player
        - Inventory
        - Trạng thái game
        """
        data = self.load_all()     
        password_hash = hashlib.sha256( self.password.encode() ).hexdigest() 
        state = {
            "password": password_hash,
            "player": self.player.to_dict(),
            "inv": [ fish.to_dict() for fish in self.inv.fish_list ]
        }          
        data["players"][self.player.player_name] = state  
        self.save_all( data )     

    def load_player( self, name ):
        """
        Tải dữ liệu người chơi từ file.

        Returns:
            Player: Đối tượng player đã được khôi phục
        """
        data = self.load_all() 
        password_hash = hashlib.sha256( self.password.encode() ).hexdigest()
        state = data["players"].get( name )
        if state is None:
            return None
        if state["password"] != password_hash:
            print( "Sai mật khẩu!" )
            return 0
        player = Player.from_dict( state["player"] )
        fish_list = [ Fish.from_dict( fish ) for fish in state["inv"] ]
        return player, fish_list    
    