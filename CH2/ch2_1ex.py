def leap(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True

if __name__ == '__main__':
    print('as main program')
    while True:
        inputs = input("Enter year:")
        if len(inputs)<=0:
            print('wrong input')
            continue
        elif inputs =='q': break
        else:
            try:
                year=int(inputs)
                if leap(year):
                    print(year ,'is leap year')
                else:
                    print(year,' is not leap year')
            except:
                print('Enter number')
else:
    print('as module')
