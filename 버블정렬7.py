import random
while True:
    num = str(input("숫자를 입력하십시오."))
    list=[]
    for i in range(1,int(num)+1):   
        list.append(i)    
        random.shuffle(list) 
    print "초기\n",list
    p = 0
    for i in range(len(list)):
        p=0
        for j in range(0,len(list)):
            if (list[i]<list[j]):
                list[i],list[j]=list[j],list[i] 
                p+=1
 

    print "변경된값\n",list
    print "변경횟수",p
    if (num != '0'):
        continue
    else:
        print "종료되었습니다."
        break
