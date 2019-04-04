import pandas as pd 
import numpy as np
from datetime import datetime,timedelta
import calendar
import sys
import os
sys.path.append(os.getcwd())
from testcases.testcases import *



def getSchedule(work_beg,work_end,work_days,loading_time,departure_time,loading_same_day):
	'''
	Function to find the schedule for a given loader

	This functions is implemented through brutal force search
	The search starts from truck departure time with increment of 0.5 hours
	Each time is checkes the following:
	1. if during worker working hours
	2. if during workdays
	3. if during the same day
	
	Before the search, a decison is made based on if the departure day has enough work
	hours to load everything and two different strategy is used based on this decision

	'''
	# 1. clean string formats
	work_beg = datetime.strptime(work_beg,'%H:%M')
	work_end = datetime.strptime(work_end,'%H:%M')
	departure_time = datetime.strptime(departure_time,'%Y-%m-%d %H:%M')
	work_end = work_end.replace(year = departure_time.year)
	work_end = work_end.replace(month = departure_time.month)
	work_end = work_end.replace(day = departure_time.day)


	# find decision based on if could load on departure day
	can_load_departure_day = None

	if departure_time.hour - work_beg.hour < loading_time:
		can_load_departure_day = False
	else:
		can_load_departure_day = True

	# if can't load at the same say and has to be continuous 
	if can_load_departure_day is False and loading_same_day is True:
		# print("--> go back to previous work day and work on loading")
		newDate = work_end
		while True:
			delta1D = timedelta(days=1)
			newDate = newDate - delta1D
			dayofweek = calendar.day_name[newDate.weekday()]
			
			if dayofweek in work_days:
				deltaLoading = timedelta(hours=loading_time)
				begin_loading_time = newDate - deltaLoading
				return begin_loading_time
				break

	else:
		# look forward 0.5 h per instance to find the location where 
		# the total amount of time satisfy the loarding_time
		newDate = departure_time
		inc = timedelta(hours=0.5)
		while loading_time > 0:
			loading_time -= 0.5
			newDate = newDate - inc
			dayofweek = calendar.day_name[newDate.weekday()]
			while newDate.hour < work_beg.hour or newDate.hour >= work_end.hour \
				or ( dayofweek not in work_days):
				newDate = newDate - inc
				dayofweek = calendar.day_name[newDate.weekday()]
		return newDate 

	return




if __name__ == '__main__':
	
	Example1(getSchedule)
	Example2(getSchedule)
	TestCase1(getSchedule)
	TestCase2(getSchedule)
	TestCase3(getSchedule)
	TestCase4(getSchedule)
	TestCase5(getSchedule)









