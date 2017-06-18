from stack import Stack

def dec2bin(decnum):
    s = Stack()
    str_aux = ''
    while decnum > 0:
        dig = decnum % 2
        decnum = decnum // 2
        s.push(dig)
    while not s.isEmpty():
        str_aux += str(s.pop())
    return str_aux

def bin2dec(binNum):
    pass

if __name__ == "__main__":
    for number in range(100,160):
        print(number,'\t', dec2bin(number))