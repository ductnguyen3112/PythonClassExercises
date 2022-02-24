import time
def pin_checker():

    correct_passwd = 123
    print("Please Enter the PIN")
    while True:
        password = input("PIN:  ")





        if password == correct_passwd:

            print('Logged In, Welcome!')
            time.sleep(1)
            print("Loading...")
            time.sleep(1)
            print("Abit More..")
            time.sleep(1)
            print("Done!.")
            time.sleep(1)
            ######function start######
            a = [3, 4, 5]
            b = a[0] or a[1]
            if b:
                print('b is true')
            else:
                print('b is false')
            break
            #####function stop######
        else:
            print("Invalid , please try again...")
pin_checker()











