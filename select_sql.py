#!/usr/bin/python3
import pymysql
import sys
conn = pymysql.connect(host='192.168.0.1',
                       port=3306,
                       user='root',
                       password='123456',
                       db='test',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()
# 相关查询
sql = 'select substr(gmt_create, 1,10) as mytime,round(sum(video_length)/ 60)  from ai_document where enable_modules like "%label%"  and task_status ="SUCCESS"  and  content_type ="VIDEO" GROUP BY  mytime order by mytime desc limit 8;'
sql1 = 'SELECT substr(gmt_create,  1,10)as mytime ,sum(TIMESTAMPDIFF(MINUTE, gmt_create , end_time )) as atime FROM ai_document WHERE enable_modules LIKE "%transform%" and task_status="SUCCESS" GROUP BY mytime ORDER BY mytime desc  limit 8;'
sql2 = 'SELECT substr(gmt_create,  1,10)as mytime ,sum(TIMESTAMPDIFF(MINUTE, gmt_create , end_time )) as atime FROM ai_document WHERE enable_modules LIKE "%detext%" and task_status="SUCCESS" GROUP BY mytime ORDER BY mytime desc  limit 8;'
sql3 = 'SELECT substr(gmt_create,  1,10)as mytime ,sum(TIMESTAMPDIFF(MINUTE, gmt_create , end_time )) as atime FROM ai_document WHERE enable_modules LIKE "%delogo%" and task_status="SUCCESS" GROUP BY mytime ORDER BY mytime desc  limit 8;'
#a = str(input("输入你要查询的算法调用量情况: sql=label,sql1=横转竖，sql2=去字幕，sql3=去水印\n 请输入：%s" %a))
#cursor.execute(str(sys.argv[1]))
cursor.execute(sql)
result = cursor.fetchall()
print(result)
