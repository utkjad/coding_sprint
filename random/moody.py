# Enter your code here. Read input from STDIN. Print output to STDOUT

def evaluate_expr(exp):
    operand = []
    operator = []
    digit = 0
    asterisk = 0
    i = 0
    while i < len(exp):
        print i
        if exp[i].isdigit():
            digit = 0
            while (i<len(exp) and exp[i].isdigit()):
                digit = (digit * 10) + int(exp[i])
                i += 1
            operand.append(digit)
            if len(operand) == 0 :
                continue
            else:
                if len(operator) != 0 and operator[-1] == "**":
                    digit = operand.pop()
                    digit2 = operand.pop()
                    operand.append(digit2**digit)
        else:
            count = 0
            while (i < len(exp) and exp[i] == "*"):
                count += 1
                i += 1
            if count == 2:
                # got asterisk
                operator.append("**")
            elif count == 1:
                operator.append("*")
            else:
                operator[:] = []
                operand[:] = []
                print "hjfjhgfjh"
                return
    product = 1
    for i in operand:
        product *= i
    return product


if __name__ == '__main__':
	print evaluate_expr("4**2*500000**2")