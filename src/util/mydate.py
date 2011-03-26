# -*- coding: utf-8 -*-
from datetime import datetime,timedelta
#
F1 = '%Y-%m-%d %H:%M:%S'
F2 = '%Y-%m-%d %H:%M'
F3 = '%Y年%m月%d日'
F4 = '%Y%m%d'


def now():
	return datetime.now()

def yesterday():
	return day_ago(1)

def tomorrow():
	return day_after(1)
	
def day_ago(x):
	return now()-timedelta(days=x)
	
def day_after(x):
	return now()+timedelta(days=x)
	
def toString1(date):
	return datetime.strftime(date,F1)

def toString2(date):
	return datetime.strftime(date,F2)
	
def toString3(date):
	return datetime.strftime(date,F2)
	
def toInt(date):
	return datetime.strftime(date,F4)

def toTime1(date):
	return datetime.strptime(date,F1)

def toTime2(date):
	return datetime.strptime(date,F2)

def toTime3(date):
	return datetime.strptime(date,F3)

def toTime4(date):
	return datetime.strptime(str(date),F4)

if __name__ == '__main__':
	print now()
	print day_ago(10)
	print day_after(10)
	
	print toString1(now())
	print toString2(now())
	print toString3(now())
	print toInt(now())

	print toTime1('2010-11-12 10:10:09');
	print toTime2('2010-11-12 10:10');
	print toTime3('2010年11月12日');
	print toTime4('20101112');


