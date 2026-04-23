import random 
#--- QUICK SORT ---
def partition( a, low, high, key  ):
    pivot =  random.randint( low, high ) 
    a[pivot], a[high] = a[high], a[pivot]
    i = low - 1 
    for j in range( low, high ):
        if( key( a[j] ) <= key( a[high] ) ):
            i += 1 
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1
def quick_sort( a, low = 0, high = None, key = lambda x: x ): 
    if( high is None ):
        high = len( a ) - 1
    if( low < high ):
        pivot = partition( a, low, high, key )
        quick_sort( a, low, pivot - 1, key )
        quick_sort( a, pivot + 1, high, key )
    return a
