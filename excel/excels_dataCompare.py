import os,sys,shutil,xlrd

def open_xls(file):
      fh=xlrd.open_workbook(file)
      return fh


piCount={}
redunt=[]
'''read dict'''
fp1=r'C:\Users\10347\Desktop\platedata\data\正式合同3处理\合同2的3-4.xlsx'
fh1=open_xls(fp1)
table1=fh1.sheets()[0]
idDict1={}
total=0
for n in range(1,table1.nrows):
	row = table1.row_values(n)
	pi = str(row[0])+row[5]+row[10]
	# if('.' in str(row[1])):
		# if('_' in row[0]):
			# id = row[0].split('_')[0]+row[0].split('_')[1]+','+str(row[1]).split('.')[0]
		# else:
			# id = row[0]+','+str(row[1]).split('.')[0]
	# else:
		# if('_' in row[0]):
			# id = row[0].split('_')[0]+row[0].split('_')[1]+','+row[1]
		# else:
			# id = row[0]+','+row[1]
	#init the count dict
	if(pi in piCount):
		total+=1
		piCount[pi][1]+=1
	else:
		#init pi key
		total+=1
		piCount[pi] = [0,1]
	if('.' in str(row[4])):
		if('_' in row[1]):
			id = row[1].split('_')[0]+row[1].split('_')[1]+','+str(row[4]).split('.')[0]
		else:
			id = row[1]+','+str(row[4]).split('.')[0]
	else:
		if('_' in row[1]):
			id = row[1].split('_')[0]+row[1].split('_')[1]+','+row[4]
		else:
			id = row[1]+','+row[4]
	#id+=str(row[0])
	#id+=str(row[10])
	if(id in idDict1):
		redunt.append(row)
	idDict1[id] = 0
	
print(len(idDict1))
print(total)


# fp2=r'C:\Users\10347\Desktop\platedata\data\hetong\ht1-zhengshi.xlsx'
# fh2=open_xls(fp2)
# table2=fh2.sheets()[0]
# idDict2={}
# for n in range(1,table2.nrows):
	# row = table2.row_values(n)
	# if('.' in str(row[1])):
		# if('_' in row[0]):
			# id = row[0].split('_')[0]+row[0].split('_')[1]+','+str(row[1]).split('.')[0]
		# else:
			# id = row[0]+','+str(row[1]).split('.')[0]
	# else:
		# if('_' in row[0]):
			# id = row[0].split('_')[0]+row[0].split('_')[1]+','+row[1]
		# else:
			# id = row[0]+','+row[1]
	# id+=str(row[10])
	# if(id in idDict2):
		# redunt.append(row)
	# idDict2[id] = 0
	# id+=str(row[10])
# print(len(idDict2))

fp=r'C:\Users\10347\Desktop\platedata\data\正式合同3处理\原始的3-4.xlsx'
fh=open_xls(fp)
table=fh.sheets()[0]

count = 0
newFile=r'C:\Users\10347\Desktop\platedata\data\append_zhengsh777.csv'
csv = open(newFile,'a+',encoding='utf-8')
csv.writelines('与合同匹对\n')#title
for n in range(1,table.nrows):
	row = table.row_values(n)
	
	pi = str(row[0])+row[5]+row[10]
	if('.' in str(row[4])):
		if('_' in row[1]):
			id = row[1].split('_')[0]+row[1].split('_')[1]+','+str(row[4]).split('.')[0]
		else:
			id = row[1]+','+str(row[4]).split('.')[0]
	else:
		if('_' in row[1]):
			id = row[1].split('_')[0]+row[1].split('_')[1]+','+row[4]
		else:
			id = row[1]+','+row[4]
	#id+=str(row[0])
	#id+=str(row[10])
	if(id in idDict1):
		# if(sizeCount[row[5]][0] >= sizeCount[row[5]][1]):
			# csv.writelines('未匹对\n')
			# continue
		if(pi in piCount):
			theCount = piCount[pi]
			if(theCount[0] >= theCount[1]):
				csv.writelines('未匹对\n')#当合同2的多了，放去第三批
			else:
				csv.writelines('在合同2中\n')
			theCount[0]+=1
		else:
			csv.writelines('不在字典中\n')
	else:
		csv.writelines('不在合同2\n')
	# elif(id in idDict2):
		# csv.writelines('在合同1中\n')

# for i in idDict2:
	# if(idDict2[i] == 0):
		# csv.writelines(str(i)+'\n')
csv.close()

print("len:"+str(len(redunt)))
	