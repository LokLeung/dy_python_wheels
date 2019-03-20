import os, sys, xlrd,shutil

def open_xls(file):
		fh=xlrd.open_workbook(file)
		return fh

def hasTitle(row):
	for c in tCols:
		if(not c in row):
			return False
	return True
	
def get_title_row(table):
	for row in range(0,table.nrows):
		r = table.row_values(row)
		if(hasTitle(r)):
			return row
	return -1		
dict=[]
reduntRoot=r'C:\Users\10347\Desktop\coding'
#读取文件内容并返回行内容
def get_file(dir,fn,file):
	count=len(dict)
	fh=open_xls(file)
	print("processing file:",dir,str(file))
	tables=fh.sheets()
	snames = fh.sheet_names()
	  
	for n in range(0,len(tables)):
		print("processing table:" + snames[n])
		if('问题' in snames[n] or '重复' in snames[n]or '冷僻字' in snames[n]):
			continue
		
		table = tables[n]
		title_row_index = get_title_row(table)
		if(title_row_index == -1):
			shutil.copy(file,reduntRoot)
			continue
		
		title_row = table.row_values(title_row_index)
		index_id = title_row.index('门牌id')
		# index_pcs = title_row.index('派出所')
		# index_gbk =  title_row.index('全球唯一码')
		# index_mp =  title_row.index('门牌名称')
		# index_mpsize =  title_row.index('门牌规格')
		# index_cjph =  title_row.index('厂家批号')
		
		for r in range(title_row_index+1,table.nrows):
			row = table.row_values(r)
			#dict[row[index_id]] = str(row[index_pcs])+','+str(row[index_gbk])+','+str(row[index_mp])+','+str(row[index_mpsize])+','+str(row[index_cjph])
			strrow = ''
			# strrow+= dir+','#批号
			# strrow+= fn+','#文件名
			# strrow+= fn.split('_')[0]+','#区号
			# strrow+= fn.split('_')[1]+','#清单号
			
			for r in row:
				strrow+=str(r)
				strrow+=','
			#dict[strrow[:-1]] = 1
			dict.append(strrow[:-1])
		print(len(dict)-count)
		
pDir = r'C:\Users\10347\Desktop\platedata\合同1'
#tCols = ["门牌id","派出所","全球唯一码","门牌名称","门牌规格","厂家批号"]
tCols = ["文件名","门牌id","行政区","派出所","街路巷","门牌名称","门牌号","门牌规格","钉挂方式","烧制厂家","烧制日期(格式YYYY-MM-DD)","安装厂家","厂家批号","厂家序号","申请人","联系电话","跳号说明","补漏制作","门牌类型","全球唯一码"]
#title = ['文件名','区号','清单号',"门牌id","行政区","派出所","街路巷","门牌名称","门牌号","门牌规格","钉挂方式","烧制厂家","烧制日期(格式YYYY-MM-DD)","安装厂家","厂家批号","厂家序号","申请人","联系电话","跳号说明","补漏制作","门牌类型","全球唯一码"]
title = ['文件名',"门牌id","行政区","派出所","街路巷","门牌名称","门牌号","门牌规格","钉挂方式","烧制厂家","烧制日期(格式YYYY-MM-DD)","安装厂家","厂家批号","厂家序号","申请人","联系电话","跳号说明","补漏制作","门牌类型","全球唯一码"]
#process every excel files
for (root, dirs, files) in os.walk(pDir):
	for filename in files:
		print(filename)
		if(filename.endswith('.xls') or filename.endswith('.xlsx')):
			try:
				get_file(root.split('\\')[-1],filename,os.path.join(root,filename))
			except:
				shutil.copy(os.path.join(root,filename),reduntRoot)
				print('无法识别！')

print("len:"+str(len(dict)))
#output csv!

#新的Excel文件
newFile=r'C:\Users\10347\Desktop\platedata\合同1\合同1.csv'
mycsv=open(newFile,'a+',encoding='utf-8')

for t in range(0,len(title)-1):
	mycsv.writelines(title[t]+',')
mycsv.writelines(title[-1]+'\n')
for d in dict:
	#mycsv.writelines(str(d)+','+str(dict[d])+'\n')
	mycsv.writelines(d+'\n')
print("正在合并，唔好心急")

mycsv.close()
	