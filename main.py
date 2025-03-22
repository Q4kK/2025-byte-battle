def main():
    number = int(input("enter a number:"))

    for i in range(number + 1):
            
        buff = " " *int( (number - i)*(1.5))
        for j in range(i):
            # if number > 10:
            #     buff += " "
            if i < 10:
                buff += " "
            buff += f"{i} "
        print(buff)
main()