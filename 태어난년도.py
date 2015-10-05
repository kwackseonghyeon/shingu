# -*- coding: cp949 -*-
print "당신이 태어난 년도를 입력하세요"
year= raw_input()
real = 2015-int(year)+1

if real >= 20 and real <=26:
        print "대학생"
elif   real  >=17 and real <20:
        print "고등학생"
elif   real  >=14 and real <17:
        print "중학생"
elif   real  >=8 and real <14:
        print "초등학생"

else:    print "학생이아닙니다."
