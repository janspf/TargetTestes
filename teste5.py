def recursion(s):
    if len(s) == 0:
        return s
    else: 
        return recursion(s[1:]) + s[0]
    
invert = input('[*] Digite a string a ser invertida: ')
print(recursion(invert))
