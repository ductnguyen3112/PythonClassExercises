import time
aws = int(input('Enter PIN:  '))

if aws == 123:


    print('Logged In, Welcome!')
    print("Loading....")
    time.sleep(1)
    print("Abit More...")
    time.sleep(1)
    print("Done!..")
    time.sleep(1)

    a = [3, 4, 5]
    b = a[0] or a[1]
    if b:
        print('b is true')
    else:
        print('b is false')
else:
    print('Wrong Password')








