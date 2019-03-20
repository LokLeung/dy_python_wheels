import os,sys,shutil,xlrd,xlwt

def open_xls(file):
      fh=xlrd.open_workbook(file)
      return fh

cnums={"一":1,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9}
def get_mp_num(mp):
	if(mp[0] in cnums):
		return cnums[mp[0]]

	print(mp)
	num = "0,1,2,3,4,5,6,7,8,9"
	nums=num.split(",")
	first=-1
	last=-1
	for n in range(0,len(mp)):
		if(mp[n] in nums):
			first = n
			break
	
	for n in range(first+1,len(mp)):
		if(not mp[n] in nums):
			last = n
			break
		
	if(last == -1):#single num
		#print(mp[first:first+1])
		return mp[first:first+1].replace(" ","")
	#print(mp[first:last])
	return mp[first:last].replace(" ","")
	  
def sortByMph(elem):
	mp = elem.split(",")[4]
	return mp
	# try:
		# print(elem.split(",")[2])
	# except:
		# print("fuck")
	# if("." in mp):
		# return int(mp.split('.')[0])
	# else:
		# return int(get_mp_num(mp))

def xlwt_write_commaSplit_row(table,row,str):
	ts = str.split(",")
	
	#the last one is mph, drop
	for n in range(0,len(ts)-1):
		table.write(row,n,ts[n])	

print("loading xls data...")
'''read dict'''
fp1=r'C:\Users\10347\Desktop\platedata\data\hetong\ht1-zs.xlsx'
fh1=open_xls(fp1)
table1=fh1.sheets()[0]
print("load sucess!")

quId= 2
pcsId = 3
streetId = 4
mpId = 5
mphId = 6
sizeId = 7

#序号 区 派出所 门牌名称 规格 备注(空)
data={}
streetDict={}
qus={}
titleRow = table1.row_values(0)
#table1.nrows
for n in range(1,table1.nrows):
	row = table1.row_values(n)
	qu = row[quId][3:]
	pcs = row[pcsId].replace("广东省","").replace("广州市公安局","")[5:]
	street = row[streetId]
	mp = row[mpId]
	mph = row[mphId]
	size = row[sizeId]
	
	
	if(pcs==""):
		pcs = qu[3:]+"分局"
	
	#不是派出所，是XX分局
	if(not qu in qus):
		qus[qu] = {}
	
	
	_str=qu+","+pcs+","+str(mp)+','+size+','+str(mph)
	if(pcs in qus[qu]):
		if(street in qus[qu][pcs]):
			qus[qu][pcs][street].append(_str)
		else:
			qus[qu][pcs][street] = [_str]
	else:
		qus[qu][pcs] = {}
		qus[qu][pcs][street] = [_str]

# for i in streetDict:
	# streetDict[i].sort(key = sortByMph)

	
pdir=r'C:\Users\10347\Desktop\platedata\New folder\正式合同一安装确认单'
for theQu in qus:
	print("processing "+theQu+" dir:")
	quPath = os.path.join(pdir,theQu)
	if( not os.path.exists(quPath)):
		os.makedirs(quPath)
	
	#for each pcs in the Qu
	for thePcs in qus[theQu]:
		print("creating "+thePcs+" xls file:")
		#create xls file for the current
		file = xlwt.Workbook()
		table = file.add_sheet("Sheet1")
		
		#write title
		title = "序号,区域,派出所,门牌名称,规格,mph"
		xlwt_write_commaSplit_row(table,0,title)
		
		rowId = 1
		#for each street in pcs
		redunts=[]
		cd={}
		for theStreet in qus[theQu][thePcs]:
			rows = qus[theQu][thePcs][theStreet]
			rows.sort(key = sortByMph)
			
			#for each data row in street
			for theRow in rows:
				if(theRow in cd):
					redunts.append(theRow)
					continue
				cd[theRow]=1
				theRow_str = str(rowId)+","+theRow
				xlwt_write_commaSplit_row(table,rowId,theRow_str)
				rowId+=1
			
		rowId2 = 1
		#if pcs has redunts data:
		if(len(redunts)>0):
			print("hi!")
			table = file.add_sheet("Sheet2")
			#write title
			title = "序号,区域,派出所,门牌名称,规格,mph"
			xlwt_write_commaSplit_row(table,0,title)
			for theRow in redunts:
				theRow_str = str(rowId2)+","+theRow
				xlwt_write_commaSplit_row(table,rowId2,theRow_str)
				rowId2+=1		
		
		#save as xls
		pcs_file_path=r'C:\Users\10347\Desktop\platedata\合同1\合同1确认单按区分\\'+theQu+"\\"+thePcs+"_"+str(rowId+rowId2-2)+".xls"
		file.save(pcs_file_path)
			
