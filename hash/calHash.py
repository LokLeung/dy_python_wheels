import os
import hashlib


def CalcMD5(filepath):
	with open(filepath,'rb') as f:
		md5obj = hashlib.md5()
		 .update(f.read())
		hash = md5obj.hexdigest()
		print(hash)
		f.close()
		return hash

def recDir(dirPath):
	print(dirPath)
	for (root, dirs, files) in os.walk(dirPath): 
		for filename in files:
			if filename.startswith("PCS") and (filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.png')or filename.endswith('.png')):
				global count
				filePath = os.path.join(root,filename)
				new_context = CalcMD5(filePath) + "\n"
				textDict.writelines(new_context)
				count = count+1
				print("file:",count)
		print("here")
		print(len(dirs))
		if len(dirs)>0:
			for dir in dirs:
				recDir(os.path.join(root,dir))
				
def filecountrecDir(dirPath):
	global totalcount
	for (root, dirs, files) in os.walk(dirPath): 
		for filename in files:
			#if filename.endswith('.jpg') or filename.endswith('.png'):
			if filename.startswith("PCS"):
				if not filename in filenameDict:
					#filecount = filecount+1
					#print("counting:%d"%filecount)
					filenameDict[filename] = [os.path.join(root,filename)]
					#filePaths.append(os.path.join(root,filename))
				else:
					global filecount
					filecount = filecount+1
					print("counting:%d"%filecount)
					filenameDict[filename].append(os.path.join(root,filename))
					print("重复："+os.path.join(root,filename))
				totalcount+=1

count = 0
filecount = 0
totalcount = 0
dirPath = "H:\照片2017\临时门牌"
dirPath = dirPath.encode("utf-8").decode('utf-8')
filenameDict={}
filePaths = []		


textDict=open(r"H:\照片2017\临时门牌\重复文件字典.txt","a+")
filecountrecDir(dirPath)
print("Total PCS files%d"%totalcount)
input("we have PCS files:"+str(filecount))
for key in filenameDict:
	if len(filenameDict[key])>1:
		new_context = str(filenameDict[key])+"\n"
		textDict.writelines(new_context)
		count = count+1
		print(" processing:	%d / %d"%(count, filecount))
	
textDict.close()