import random
while True:
    num = str(input("���ڸ� �Է��Ͻʽÿ�."))
    list=[]
    for i in range(1,int(num)+1):   
        list.append(i)    
        random.shuffle(list) 
    print "�ʱ�\n",list
    p = 0
    for i in range(len(list)):
        p=0
        for j in range(0,len(list)):
            if (list[i]<list[j]):
                list[i],list[j]=list[j],list[i] 
                p+=1
 

    print "����Ȱ�\n",list
    print "����Ƚ��",p
    if (num != '0'):
        continue
    else:
        print "����Ǿ����ϴ�."
        break
