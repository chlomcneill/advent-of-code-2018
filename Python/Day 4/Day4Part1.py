import datetime as dt
import substring as ss
import re
from datetime import timedelta

f = open("/Users/mcneillc/Documents/advent-of-code-2018/Day 4/Day4input.txt","r")
records = f.readlines()
f.close()

records.sort()

datetime_format = '[%Y-%m-%d %H:%M]'
date1 = records[0][:18]
date2 = records[1][:18]
diff = dt.datetime.strptime(date2, datetime_format) - dt.datetime.strptime(date1, datetime_format)

diff_in_mins = diff.minute

print(diff_in_mins)

# def split_record(record):
#     date_time = ss.substringByChar(record, startChar='[', endChar=']')
#     detail = ss.substringByInd(record, startInd=19)
#     new_record = [date_time,detail]
#     return new_record

# records = [split_record(record) for record in records]

def find_guard_ID(record):
    if record[1].startswith('G'):
        guard_ID = re.findall(r'\d+', record[1])
        guard_ID = int(guard_ID[0])
    return guard_ID

def get_minutes(record):
    minutes = record[0][15:17]
    return minutes

def get_time(record):
    time = record[0][12:17]
    return time

# def get_time_slept(guard_ID):
#     for i in range(len(records)):
#         if guard_ID in records[i][1]:

        
    


# print(find_start_time(records[0]))

