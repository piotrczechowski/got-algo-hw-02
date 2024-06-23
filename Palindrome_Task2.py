from collections import deque

def is_palindrome(input_str):
    processed_str = ''.join(input_str.lower().split())
    #print("string : ",processed_str)
    char_deque = deque(processed_str)
    #print(char_deque)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():

            return False
    
    return True 

#Check
print(is_palindrome("checking if there is a "))  
print(is_palindrome("Hello"))   
print(is_palindrome("madam")) 

