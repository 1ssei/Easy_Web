import csv
import os
from datetime import datetime as dt
import pytz
import re
import time


def csv2list(csv_file_path):
    csv_content = []
    with open(csv_file_path, 'r') as testCsv:
        tracker = csv.DictReader(testCsv)
        for row in tracker:
            csv_content.append(row)
    return csv_content

def csv2list_no_header(csv_file_path):
    csv_content = []
    with open(csv_file_path, "r",encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            csv_content.append(row)
    return csv_content


def getFileFromFolder(folderPath,extension='anymatch'):
    file_list = []
    for (root, dirs, fileNames) in os.walk(folderPath):
        for file in fileNames:
            target = os.path.join(root,file)
            if os.path.isfile(target):
                if(extension == 'anymatch' or target.__contains__(extension)):
                    file_list.append(target)
    return file_list


def str2date(str):
    try:
        jst = pytz.timezone('UTC')
        return dt.strptime(str, '%Y-%m-%d').replace(tzinfo=jst)
    except:
        return ''

def str2date_notimestamp(tstr):
    try:
        return dt.strptime(tstr, '%Y-%m-%d')

    except:
        print(str,'this is not date')
        return ''

def date2str(date):
    return date.strftime('%Y , %m , %d')

def calc_last_date(dates):
    last_date = str2date('2011-1-1')
    for date in dates:
        try:
            if last_date < date :
                last_date = date
        except:
            pass
    return last_date

def file2List(filePath,unicode='utf-8'):
    f = open(filePath, 'r', -1, unicode)
    list = []
    for line in f:
        line = re.sub('\\n','',line)
        list.append(line)
    f.close()
    return list


def delete_items_from_str(arg_str, deleteitems):
    for item in deleteitems:
        arg_str = re.sub(item, '', arg_str)
    return arg_str

def date2unixtime(arg_time):
    return int(time.mktime(arg_time.timetuple()))*1000

