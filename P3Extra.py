def main():
    # initialize variales
    numberMax = 0
    numberMid = 0
    numberMin = 0
    temp = 0

    # store first number in max
    numberMax = eval(input("Enter the first number "))
    # store second number in temp until we find out if it is bigger than our max or not
    temp = eval(input("Enter the second number "))
    if numberMax > temp:
        numberMin = temp
    else:
        numberMin = numberMax
        numberMax = temp
    # store third number and determine if it's placement
    temp = eval(input("Enter the third number "))
    if numberMax >= temp and temp >= numberMin:
        numberMid = temp
    elif numberMax <= temp:
        numberMid = numberMax
        numberMax = temp
    elif numberMin >= temp:
        numberMid = numberMin
        numberMin = temp
    # print the correct order!
    print(numberMax," ,", numberMid," ,",numberMin)

main()