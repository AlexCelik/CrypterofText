def crypt(string):
    string = string.replace('a', '2'+',')
    string = string.replace('b', '22'+',')
    string = string.replace('c', '222'+',')
    string = string.replace('d', '3'+',')
    string = string.replace('e', '33'+',')
    string = string.replace('f', '333'+',')
    string = string.replace('g', '4'+',')
    string = string.replace('h', '44'+',')
    string = string.replace('i', '444'+',')
    string = string.replace('j', '5'+',')
    string = string.replace('k', '55'+',')
    string = string.replace('l', '555'+',')
    string = string.replace('m', '6'+',')
    string = string.replace('n', '66'+',')
    string = string.replace('o', '666'+',')
    string = string.replace('p', '7'+',')
    string = string.replace('q', '77'+',')
    string = string.replace('r', '777'+',')
    string = string.replace('s', '7777'+',')
    string = string.replace('t', '8'+',')
    string = string.replace('u', '88'+',')
    string = string.replace('v', '888'+',')
    string = string.replace('w', '9'+',')
    string = string.replace('x', '99'+',')
    string = string.replace('y', '999'+',')
    string = string.replace('z', '9999'+',')
    return string





text = input('encrypt : ')
crypt_str = crypt(text)
print(crypt_str)

