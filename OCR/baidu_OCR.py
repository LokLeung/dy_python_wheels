from aip import AipOcr
import cv2
import numpy as np
""" 你的 APPID AK SK """
APP_ID = '11745295'
API_KEY = '11zFL3QlD4GgusgARTMUs1tt'
SECRET_KEY = 'Rp63NVlFrufoB4nVM2gcGDTz4aZYB1Zh'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
#鼠标事件
def get_rect(im, title='get_rect'):   #   (a,b) = get_rect(im, title='get_rect')
	mouse_params = {'tl': None, 'br': None, 'current_pos': None,
		'released_once': False}

	cv2.namedWindow(title)
	cv2.moveWindow(title, 100, 100)

	def onMouse(event, x, y, flags, param):

		param['current_pos'] = (x, y)

		if param['tl'] is not None and not (flags & cv2.EVENT_FLAG_LBUTTON):
			param['released_once'] = True

		if flags & cv2.EVENT_FLAG_LBUTTON:
			if param['tl'] is None:
				param['tl'] = param['current_pos']
			elif param['released_once']:
				param['br'] = param['current_pos']

	cv2.setMouseCallback(title, onMouse, mouse_params)
	cv2.imshow(title, im)

	while mouse_params['br'] is None:
		im_draw = np.copy(im)

		if mouse_params['tl'] is not None:
			cv2.rectangle(im_draw, mouse_params['tl'],
				mouse_params['current_pos'], (255, 0, 0))

		cv2.imshow(title, im_draw)
		_ = cv2.waitKey(10)

	cv2.destroyWindow(title)

	x1,y1 = (min(mouse_params['tl'][0], mouse_params['br'][0]),
		min(mouse_params['tl'][1], mouse_params['br'][1]))
	x2,y2 = (max(mouse_params['tl'][0], mouse_params['br'][0]),
		max(mouse_params['tl'][1], mouse_params['br'][1]))
	print("y1,x1,y2,x2",y1,x1,y2,x2)
	roi = im[y1:y2,x1:x2]
	
	return (roi)  #tl=(y1,x1), br=(y2,x2)
	
	
image = get_file_content(r'C:\Users\10347\Desktop\coding\ocr\imgOCR\IMG20171115153052.jpg')
#im = cv2.imread(r'C:\Users\10347\Desktop\imgOCR\1.jpg')
#roi = get_rect(im)
#cv2.imshow("roi",roi)
#cv2.waitKey()

""" 调用通用文字识别, 图片参数为本地图片 """
res = client.basicGeneral(image)

print(res)

input("key in sth")

