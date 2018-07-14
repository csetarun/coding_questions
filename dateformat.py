import datetime
try:
	date_text = '12/2/2017'
	dt = datetime.datetime.strptime(date_text, '%m/%d/%Y')
	print dt.strftime('%Y%m%d')
except ValueError:
	raise ValueError("Incorrect data format, should be M/D/YYYY")