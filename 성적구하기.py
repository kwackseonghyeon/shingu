seiseki = []

student_su = int(raw_input('�л� ���� �Է��ϼ��� : '))

for student in range(student_su):
	
	student_info = []
	
	print '\n======= ', student + 1, '�� �л� ======='
	
	language = int(raw_input('���������� �Է��ϼ��� : '))
	english = int(raw_input('���������� �Է��ϼ��� : '))
	math = int(raw_input('���������� �Է��ϼ��� : '))
	total = language + english + math
	average = total / 3
	
	student_info.append(language)
	student_info.append(english)
	student_info.append(math)
	student_info.append(total)
	student_info.append(average)
	
	seiseki.insert(student, student_info)

for final in range(student_su):
	print '\n================ ', final + 1, '�� �л� ���� ================'
	print '����', seiseki[final][0], '| ����', seiseki[final][1], '| ����', seiseki[final][2], '| ����', seiseki[final][3], '| ���', seiseki[final][4]

