from stack import Stack

def dec_to_bin(dec):
    # Finish the function
    s = Stack()
    while dec != 0:
        b = dec%2
        s.push(b)
        dec = dec//2
        
    binary = ''
    while  not s.isEmpty():
        binary = binary + str(s.pop())

    return binary 
    
print(dec_to_bin(42) )  # 回傳 101010
print(dec_to_bin(100))  # 回傳 1100100