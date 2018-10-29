import csv
import os
title ="python learning "
with open("pyhton learning.txt","a+") as f:
	f.write(title)
	f.close()

with open("pyhton learning.txt","r",encoding ="UTF-8") as f:
	text=f.read()
	print(text)
	f.close()

print(os.getcwd())
with open(R"D:\Software\GitHubRepository\spider\test.csv","r",encoding="UTF-8") as csvfile:
	 csv_reader = csv.reader(csvfile)
	 for row in csv_reader:
	 	# print(row)
	 	print(row[0])#读取第一列
	 	print(row[1])#读取第二列	
	 csvfile.close()

outputlist=["A","B","C","D"]
with open("test.csv","a+",encoding="UTF-8",newline="") as csvfile:
	csv_writer = csv.writer(csvfile)
	csv_writer.writerow(outputlist)
