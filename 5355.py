number = int(input())


def calculate(x):
    sum_of_num = 0
    string = str(x).split()
    for i in range(len(string)):
        if i == 0:
            sum_of_num += float(string[i])
        elif string[i] == "@":
            sum_of_num *= 3
        elif string[i] == "%":
            sum_of_num += 5
        elif string[i] == "#":
            sum_of_num -= 7
    result = "{:.2f}".format(sum_of_num)
    return result


for i in range(number):
    cal = input()
    print(calculate(cal))
