def rem(dividend,divid):
    a = dividend
    b = divid
    c = a%b
    return c

def get_code(number):
    if number == 1:
        code = [1,1,1]
    elif number == 2:
        code = [2,1,1]
    elif number == 3:
        code = [1,2,1]
    elif number == 4:
        code = [2,2,1]
    elif number == 5:
        code = [1,1,2]
    elif number == 6:
        code = [2,1,2]
    elif number == 7:
        code = [1,2,2]
    elif number == 0:
        code = [2,2,2]
    return code

def change_calc(number):
    if number == 0:
        code = 6
    else:
        code = number
    return code

def symbol_show(number):
    sun = """——————————"""
    moon = """————  ————"""
    if number == 1:
        print(sun)
    else:
        print(moon)

if __name__ == '__main__':
    #input No.
    symbol_bottom_in = int(input("输入第一个三位数："))
    symbol_head_in = int(input("输入第二个三位数："))
    change_in = int(input("输入第三个三位数："))
    
    #calc No.
    change_out = change_calc(rem(change_in,6))
    symbol_head_out = get_code(rem(symbol_head_in,8))
    symbol_bottom_out = get_code(rem(symbol_bottom_in,8))
    print(change_out, symbol_head_out, symbol_bottom_out)
    
    #print symbol
    print("==================")
    print("爻:"+str(change_out))
    print("==================")
    for number in symbol_head_out:
        symbol_show(number)
    for number in symbol_bottom_out:
        symbol_show(number)
