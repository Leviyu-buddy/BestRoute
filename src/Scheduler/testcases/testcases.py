

def Example1(getSchedule):
	work_beg = "08:00"
	work_end = "14:00"
	work_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
	loading_time = 3.0
	departure_time = "2018-08-13 10:00"
	loading_same_day = True
	schedule = getSchedule(work_beg,work_end,work_days,loading_time,departure_time,loading_same_day)
	print("--> Example #1")
	print('		Loading Schedule is: {0}'.format(schedule))
	print('		Expected to be: 	 {0}'.format("2018-08-11 11:00:00"))
	return

def Example2(getSchedule):
	work_beg = "08:00"
	work_end = "14:00"
	work_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
	loading_time = 3.0
	departure_time = "2018-08-14 10:00"
	loading_same_day = False
	schedule = getSchedule(work_beg,work_end,work_days,loading_time,departure_time,loading_same_day)
	print("--> Example #2")
	print('		Loading Schedule is: {0}'.format(schedule))
	print('		Expected to be: 	 {0}'.format("2018-08-13 13:00:00"))
	return

def TestCase1(getSchedule):
	work_beg = "08:00"
	work_end = "14:00"
	work_days = ['Monday','Tuesday','Wednesday','Thursday','Friday']
	loading_time = 3.0
	departure_time = "2018-08-15 14:00"
	loading_same_day = False
	schedule = getSchedule(work_beg,work_end,work_days,loading_time,departure_time,loading_same_day)
	print("--> TestCase #1")
	print('		Loading Schedule is: {0}'.format(schedule))
	print('		Expected to be: 	 {0}'.format("2018-08-15 11:00:00"))
	return

def TestCase2(getSchedule):
	work_beg = "08:00"
	work_end = "14:00"
	work_days = ['Monday','Tuesday','Wednesday','Thursday','Friday']
	loading_time = 3.0
	departure_time = "2018-08-15 14:00"
	loading_same_day = True
	schedule = getSchedule(work_beg,work_end,work_days,loading_time,departure_time,loading_same_day)
	print("--> TestCase #2")
	print('		Loading Schedule is: {0}'.format(schedule))
	print('		Expected to be: 	 {0}'.format("2018-08-15 11:00:00"))
	return


def TestCase3(getSchedule):
	work_beg = "12:00"
	work_end = "18:00"
	work_days = ['Monday','Wednesday','Friday']
	loading_time = 3.0
	departure_time = "2018-08-15 10:00"
	loading_same_day = False
	schedule = getSchedule(work_beg,work_end,work_days,loading_time,departure_time,loading_same_day)
	print("--> TestCase #3")
	print('		Loading Schedule is: {0}'.format(schedule))
	print('		Expected to be: 	 {0}'.format("2018-08-13 15:00:00"))
	return

def TestCase4(getSchedule):
	work_beg = "08:00"
	work_end = "14:00"
	work_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
	loading_time = 3.5
	departure_time = "2018-08-14 10:00"
	loading_same_day = False
	schedule = getSchedule(work_beg,work_end,work_days,loading_time,departure_time,loading_same_day)
	print("--> TestCase #4")
	print('		Loading Schedule is: {0}'.format(schedule))
	print('		Expected to be: 	 {0}'.format("2018-08-13 12:30:00"))
	return

def TestCase5(getSchedule):
	work_beg = "08:00"
	work_end = "14:00"
	work_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
	loading_time = 3.5
	departure_time = "2018-08-14 10:00"
	loading_same_day = True
	schedule = getSchedule(work_beg,work_end,work_days,loading_time,departure_time,loading_same_day)
	print("--> TestCase #5")
	print('		Loading Schedule is: {0}'.format(schedule))
	print('		Expected to be: 	 {0}'.format("2018-08-13 10:30:00"))
	return

