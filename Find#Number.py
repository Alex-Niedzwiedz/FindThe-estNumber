def NumberFinder(number,position):
    length = len(number)

    for i in range(length):
        for x in range(0,length-i-1):
            if number[x]>number[x+1]:
                number[x],number[x+1]=number[x+1],number[x]
    print(number,"\n")
    print(number[length-position])

def main():
    number=[213,1,5,2,100]
    postion= eval(input("What biggest number do you want "))
    NumberFinder(number,postion)
main()
