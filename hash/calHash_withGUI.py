from tkinter import *
import tkinter.messagebox as messagebox
import os
import hashlib


def CalcMD5(filepath):
	with open(filepath,'rb') as f:
		md5obj = hashlib.md5()
		md5obj.update(f.read())
		hash = md5obj.hexdigest()
		print(hash)
		f.close()
		return hash

count = 0
dirPath = "F:\门牌"
dirPath = dirPath.encode("utf-8").decode('utf-8')
def recDir(dirPath):
	"""foreach imagefile, deployment ORC tech"""
	print(dirPath)
	for (root, dirs, files) in os.walk(dirPath): 
		for filename in files:
			if filename.endswith('.jpg') or filename.endswith('.png'):
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

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.pathLabel = Label(self, text='请输入路径')
		self.pathLabel.pack(side = LEFT)
		self.nameInput = Entry(self, width=30)
		self.nameInput.pack(side = LEFT)
		self.alertButton = Button(self, text='提取照片特征码', command=self.hello)
		self.alertButton.pack()

	def hello(self):
		dirPath = self.nameInput.get()
		
		recDir(dirPath)		
		textDict.close()
		messagebox.showinfo('Message', 'Finish')

textDict=open(dirPath+"md5字典.txt","a+")
root = Tk()
root.title('提取照片特征码小程序')
root.geometry('400x200')
app = Application(root)
# 主消息循环:
app.mainloop()