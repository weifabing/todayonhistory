# -*- coding: utf8 -*-
# --weifabing@gmail.com
import os,sys,re
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')
print 'Start'

file_name="history.dat"
re_history = re.compile(r'^##\d{8}')
re_date  = re.compile(r'^##(\d{8}) (.*)$')
re_dd = re.compile(r'^(\d{4})(\d{2})(\d{2})')

i=0
j=0
for line in file(file_name):
    i=i+1
    if i==1:
        _content=""
        _title =""
        _year =""
        _month =""
        _day =""
        new_year=""
        new_month=""
        new_day=""
        new_title=""
        new_content=""
    if re_history.match(line):
        new_line = True
        _year  = new_year
        _month  = new_month
        _day  = new_day
        _title = new_title
        _content= new_content.replace("\'","\\\'")
        dd=re_date.findall(line)[0]
        ee=list(re_dd.match(dd[0]).groups())
        new_year = ee[0]
        new_month = ee[1]
        new_day = ee[2]
        new_title= dd[1]
        new_content = ""
    else:
        new_line=False
    if (i-1) % 5000==0:
        j=j+1
        sql_file="history_"+str(j)+'.sql'
        file_object = open(sql_file, 'w')
        print "New sql file: "+sql_file

    if i>1:
        if new_line:
            sql="Insert into history (year,month,day,title,content) values ('%s','%s','%s','%s','%s');\n" % (_year,_month,_day, _title, _content)
            file_object.write(sql)
        else:
            new_content = new_content + line.strip(' ')
file_object.close()
print "all insert" + str(i)
