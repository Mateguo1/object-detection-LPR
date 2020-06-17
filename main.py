import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage,QPixmap
import cv2
from Ui_CG import Ui_Form
import imageio
from PIL import Image
import numpy as np
import re 
import time


file_path = None

class MyWindow(QWidget,Ui_Form):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        #public
        self.path = None
        #1
        self.btn_poc.clicked.connect(self.poc)
        self.btn_pos.clicked.connect(self.pos)
        self.btn_por.clicked.connect(self.por)
        self.btn_poy.clicked.connect(self.poy)
        self.po1.setScene(None)
        self.po2.setScene(None)
        #2
        self.btn_plc.clicked.connect(self.plc)
        self.btn_pls.clicked.connect(self.pls)
        self.btn_plr.clicked.connect(self.plr)
        self.btn_ply.clicked.connect(self.ply)
        self.pl1.setScene(None)
        self.pl2.setScene(None)
        #3
        self.btn_voc.clicked.connect(self.voc)
        self.btn_vos.clicked.connect(self.vos)
        self.btn_vor.clicked.connect(self.vor)
        self.btn_voy.clicked.connect(self.voy)
        #4
        self.btn_vlc.clicked.connect(self.vlc)
        self.btn_vls.clicked.connect(self.vls)
        self.btn_vlr.clicked.connect(self.vlr)
        self.btn_vly.clicked.connect(self.vly)


    '''
    picture object detection function
    '''
    def poc(self):
        self.path = QFileDialog.getOpenFileName(self, "选择文件", "./", 'Images(*.png *jpg *JPG *gif *tif *.ppm)')
        paths = self.path
        global file_path
        file_path = paths[0]
        if paths[0] is "":
            return
        img1 = cv2.imread(paths[0])
        img = cv2.resize(img1,(480,270))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        x = img.shape[1]                                      
        y = img.shape[0]
        showImage = QImage(img,x,y,QImage.Format_RGB888)
        pix = QPixmap.fromImage(showImage)
        self.item = QGraphicsPixmapItem(pix)
        self.scene = QGraphicsScene()
        self.scene.addItem(self.item)
        self.po1.setScene(self.scene)
        self.textshow.setText("正在选择图像目标检测文件\n选择文件路径为：{}".format(paths[0]))

    def pos(self):
        # print(self.path)
        global file_path
        text = self.textshow.toPlainText()
        if len(text.split("："))==2:
            file_path = text.split("：")[1]
            print(file_path)
        time.sleep(1)
        if re.search(r"png|jpg|JPG|gif|tif|ppm$",file_path):
            self.textshow.setText("正在使用 SSD模型 进行图像目标检测,请稍候")

            self.textshow.append("选择文件正确,路径为:{}".format(file_path))
        else:
            self.textshow.setText("选择文件错误,路径为:{}".format(file_path))
        
    def por(self):
        global file_path
        text = self.textshow.toPlainText()
        if len(text.split("："))==2:
            file_path = text.split("：")[1]
            print(file_path)
        time.sleep(1)
        if re.search(r"png|jpg|JPG|gif|tif|ppm$",file_path):
            self.textshow.setText("正在使用 Retinanet模型 进行图像目标检测,请稍候")
            self.textshow.append("选择文件正确,路径为:{}".format(file_path))
        else:
            self.textshow.setText("选择文件错误,路径为:{}".format(file_path))
    #yolov3进行目标检测
    def poy(self):
        
        global file_path
        text = self.textshow.toPlainText()
        if len(text.split("："))==2:
            file_path = text.split("：")[1]
            print(file_path)
        time.sleep(1)
        if re.search(r"png|jpg|JPG|gif|tif|ppm$",file_path):
            yolo = YOLO()
            self.textshow.setText("正在使用 YoloV3模型 进行图像目标检测,请稍候")
            self.textshow.append("选择文件正确,路径为:{}".format(file_path))
        else:
            self.textshow.setText("选择文件错误,路径为:{}".format(file_path))
        
    '''
    video object detection function
    '''
    def voc(self):
        self.path = QFileDialog.getOpenFileName(self, "选择文件", "./", 'Videos(*.mp4 *.avi)')
        paths = self.path
        if paths[0] is "":
            return
        self.textshow.setText("正在选择视频目标检测文件\n选择文件路径为：{}".format(paths[0]))
    
    def vos(self):
        global file_path
        text = self.textshow.toPlainText()
        if len(text.split("："))==2:
            file_path = text.split("：")[1]
            print(file_path)
        time.sleep(1)
        if re.search(r"mp4|avi$",file_path):
            self.textshow.setText("正在使用 SSD模型 进行视频目标检测,请稍候\n")
            self.textshow.append("选择文件正确,路径为:{}".format(file_path))
        else:
            self.textshow.setText("选择文件错误,路径为:{}".format(file_path))

    def vor(self):
        global file_path
        text = self.textshow.toPlainText()
        if len(text.split("："))==2:
            file_path = text.split("：")[1]
            print(file_path)
        time.sleep(1)
        if re.search(r"mp4|avi$",file_path):
            self.textshow.setText("正在使用 Retinanet模型 进行视频目标检测,请稍候")
            # demo()
            self.textshow.append("选择文件正确,路径为:{}".format(file_path))
        else:
            self.textshow.setText("选择文件错误,路径为:{}".format(file_path))

    def voy(self):
        global file_path
        text = self.textshow.toPlainText()
        if len(text.split("："))==2:
            file_path = text.split("：")[1]
            print(file_path)
        time.sleep(1)
        if re.search(r"mp4|avi$",file_path):
            self.textshow.setText("正在使用 YoloV3模型 进行视频目标检测,请稍候")
            self.textshow.append("选择文件正确,路径为:{}".format(file_path))
        else:
            self.textshow.setText("选择文件错误,路径为:{}".format(file_path))

    '''
    picture license plate function
    '''
    def plc(self):
        self.path = QFileDialog.getOpenFileName(self, "选择文件", "./", 'Images(*.png *jpg *JPG *gif *tif *.ppm)')
        paths = self.path
        if paths[0] is "":
            return
        img1 = cv2.imread(paths[0])
        img = cv2.resize(img1,(480,270))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        x = img.shape[1]                                      
        y = img.shape[0]
        showImage = QImage(img,x,y,QImage.Format_RGB888)
        pix = QPixmap.fromImage(showImage)
        self.item = QGraphicsPixmapItem(pix)
        self.scene = QGraphicsScene()
        self.scene.addItem(self.item)
        self.pl1.setScene(self.scene)
        self.textshow.setText("正在选择图像车牌识别文件\n选择文件路径为：{}".format(paths[0]))

    def pls(self):
        global file_path
        text = self.textshow.toPlainText()
        if len(text.split("："))==2:
            file_path = text.split("：")[1]
            print(file_path)
        time.sleep(1)
        if re.search(r"png|jpg|JPG|gif|tif|ppm$",file_path):
            self.textshow.setText("正在使用 SSD模型 进行图像车牌识别,请稍候")
            self.textshow.append("选择文件正确,路径为:{}".format(file_path))
        else:
            self.textshow.setText("选择文件错误,路径为:{}".format(file_path))

    def plr(self):
        global file_path
        text = self.textshow.toPlainText()
        if len(text.split("："))==2:
            file_path = text.split("：")[1]
            print(file_path)
        time.sleep(1)
        if re.search(r"png|jpg|JPG|gif|tif|ppm$",file_path):
            self.textshow.setText("正在使用 Retinanet模型 进行图像车牌识别,请稍候")
            self.textshow.append("选择文件正确,路径为:{}".format(file_path))
        else:
            self.textshow.setText("选择文件错误,路径为:{}".format(file_path))

    def ply(self):
        global file_path
        text = self.textshow.toPlainText()
        if len(text.split("："))==2:
            file_path = text.split("：")[1]
            print(file_path)
        time.sleep(1)
        if re.search(r"png|jpg|JPG|gif|tif|ppm$",file_path):
            self.textshow.setText("正在使用 YoloV3模型 进行图像车牌识别,请稍候")
            self.textshow.append("选择文件正确,路径为:{}".format(file_path))
        else:
            self.textshow.setText("选择文件错误,路径为:{}".format(file_path))
            
    '''
    video license plate function
    '''
    def vlc(self):
        self.path = QFileDialog.getOpenFileName(self, "选择文件", "./", 'Videos(*.mp4 *.avi)')
        paths = self.path
        if paths[0] is "":
            return
        self.textshow.setText("正在选择视频车牌识别文件\n选择文件路径为：{}".format(paths[0]))
    
    def vls(self):
        global file_path
        text = self.textshow.toPlainText()
        if len(text.split("："))==2:
            file_path = text.split("：")[1]
            print(file_path)
        time.sleep(1)
        if re.search(r"mp4|avi$",file_path):
            self.textshow.setText("正在使用 SSD模型 进行视频车牌识别,请稍候")
            # demo()
            self.textshow.append("选择文件正确,路径为:{}".format(file_path))
        else:
            self.textshow.setText("选择文件错误,路径为:{}".format(file_path))
        
    def vlr(self):
        global file_path
        text = self.textshow.toPlainText()
        if len(text.split("："))==2:
            file_path = text.split("：")[1]
            print(file_path)
        time.sleep(1)
        if re.search(r"mp4|avi$",file_path[0]):
            self.textshow.setText("正在使用 Retinanet模型 进行视频车牌识别,请稍候")
            # demo()
            self.textshow.append("选择文件正确,路径为:{}".format(file_path))
        else:
            self.textshow.setText("选择文件错误,路径为:{}".format(file_path))
        
    def vly(self):
        global file_path
        text = self.textshow.toPlainText()
        if len(text.split("："))==2:
            file_path = text.split("：")[1]
            print(file_path)
        time.sleep(1)
        if re.search(r"mp4|avi$",file_path):
            self.textshow.setText("正在使用 YoloV3模型 进行视频车牌识别,请稍候")
            # demo()
            self.textshow.append("选择文件正确,路径为:{}".format(file_path))
        else:
            self.textshow.setText("选择文件错误,路径为:{}".format(file_path))
        
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.resize(1400,1100)
    w.show()
    sys.exit(app.exec_())