import random    
while True:
    k = ["0", "0", "0"]
    k[0] = str(random.randrange(1, 9, 1))
    k[1] = k[0]
    while (k[0] == k[1]):
        k[1] = str(random.randrange(1, 9, 1))
    k[2] = k[0]
    while (k[0] == k[2] or k[1] == k[2]):
        k[2] = str(random.randrange(1, 9, 1))
   
   
    sido = 0 
    strike = 0 
    ball = 0 
    restart = 0
    print("Baseball game")
    while ( strike < 3 ):
        strike = 0
        ball = 0
        err = 0 
        num = str(raw_input("Enter 3 : "))
        if(num == '0'):
            print "The End"
            err += 1
            break
        elif(len(num) != 3):  
            print "you input wrong values"
            err += 1
            continue
        elif(num[0] == num[1] or num[1]==num[2] or num[0]==[2]): 
            print "you input wrong values"
            err += 1
            continue
        elif(num.isdigit() == False): 
            print "you input wrong values"
        

        else:
            for i in range(0, 3):
                for j in range(0, 3):
                    if(num[i] == str(k[j]) and i == j):
                        strike += 1
                    elif(num[i] == str(k[j]) and i != j):
                        ball += 1
            print "Strike:" ,strike, "Ball:",ball 
            sido += 1

    print "You've played ",sido ,"times"
    restart = str(raw_input("Do you want one more game? (yes/no)? :"))
    if (restart.upper() == 'YES'):
        continue
    else:
        print "The End"
        break
