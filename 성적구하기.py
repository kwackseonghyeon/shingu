seiseki = []

student_su = int(raw_input('학생 수를 입력하세요 : '))

for student in range(student_su):
	
	student_info = []
	
	print '\n======= ', student + 1, '번 학생 ======='
	
	language = int(raw_input('국어점수를 입력하세요 : '))
	english = int(raw_input('영어점수를 입력하세요 : '))
	math = int(raw_input('수학점수를 입력하세요 : '))
	total = language + english + math
	average = total / 3
	
	student_info.append(language)
	student_info.append(english)
	student_info.append(math)
	student_info.append(total)
	student_info.append(average)
	
	seiseki.insert(student, student_info)

for final in range(student_su):
	print '\n================ ', final + 1, '번 학생 성적 ================'
	print '국어', seiseki[final][0], '| 영어', seiseki[final][1], '| 수학', seiseki[final][2], '| 총점', seiseki[final][3], '| 평균', seiseki[final][4]

