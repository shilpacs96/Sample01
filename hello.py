def ask():
    waiting = True
    while True:
        try:
            n=int(input("enter a number"))
        except:
            print("try again\n")
            continue
        else:
            waiting == False
            
    print(n**2)