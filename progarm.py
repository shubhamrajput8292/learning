
string = input("Enter a string: ")
char_count = {}

for ch in string:
    
    if ch in char_count:
        char_count[ch] += 1  
    else:
        char_count[ch] = 1  
print("Character count dictionary:")
print(char_count)
