# -*- coding: utf-8 -*-

import sys, math, random

from PyQt5.QtWidgets import  (QApplication, QMainWindow,QDialog,QWidget,
                           QFontDialog,QColorDialog,QLabel)

from PyQt5.QtCore import  pyqtSlot,Qt,QMargins

from PyQt5.QtGui import QPainter,QPen,QColor,QBrush,QFont

from PyQt5.QtChart import QChart,QLineSeries,QValueAxis

from high_school import Ui_Form
from myChartView import QmyChartView
from math import sqrt

class QmyMainWindow(QWidget): 

   def __init__(self, parent=None):
      super().__init__(parent)   #调用父类构造函数，创建窗体
      self.ui=Ui_Form()    #创建UI对象
      self.ui.setupUi(self)      #构造UI界面
      self.__buildStatusBar()    #创建状态栏QLabel组件

      self.setWindowTitle("一元二次方程示意图")

      self.ui.para_a.setText("1")
      self.ui.para_b.setText("0")
      self.ui.para_c.setText("0")

      self.params_a = float(self.ui.para_a.text())
      self.params_b = float(self.ui.para_b.text())
      self.params_c = float(self.ui.para_c.text())

      #self.chartView = QmyChartView(self)
      #self.chartView.setRenderHint(QPainter.Antialiasing)
      #self.chartView.setCursor(Qt.CrossCursor)  #设置鼠标指针为十字星
      #self.chartView.mouseMove.connect(self.do_chartView_mouseMove)

      self.__createChart() #创建图表
      self.__prepareData()    #为序列设置数据

      self.ui.slider_a.valueChanged.connect(self.do_valueChanged)
      self.ui.slider_b.valueChanged.connect(self.do_valueChanged)
      self.ui.slider_c.valueChanged.connect(self.do_valueChanged)
      pass


##  ==============自定义功能函数========================
   def __createChart(self):
      chart = QChart()
      chart.legend().setVisible(True)
      self.ui.graphicsView.setChart(chart)

      pen=QPen()
      pen.setWidth(2)

      seriesLine = QLineSeries()
      seriesLine.setName("LineSeries折线")
      seriesLine.setPointsVisible(False)     #数据点不可见
      pen.setColor(Qt.red)
      seriesLine.setPen(pen)
      seriesLine.hovered.connect(self.do_series_hovered)  #信号 hovered
      seriesLine.clicked.connect(self.do_series_clicked)  #信号 clicked
      chart.addSeries(seriesLine)   #添加到chart

      ##  创建缺省坐标轴
      chart.createDefaultAxes()  #创建缺省坐标轴并与序列关联
      chart.axisX().setTitleText("time(secs)")
      chart.axisX().setRange(-20,20)
      chart.axisX().applyNiceNumbers()

      chart.axisY().setTitleText("value")
      chart.axisY().setRange(-50,50)
      chart.axisY().applyNiceNumbers()
      

   def __prepareData(self):  ##为序列设置数据点
      series0=self.ui.graphicsView.chart().series()[0]  # QLineSeries
      series0.clear()

      t=-20
      intv=0.05
      pointCount=1000  #数据点个数较少，比较QLineSeries和QSplineSeries的差别
      for i in range(pointCount):
        y1 = self.params_a*t**2 + self.params_b*t + self.params_c
        series0.append(t,y1)     # QLineSeries
        t=t+intv
      pass


   def __updateFromChart(self):
      pass

   def __buildStatusBar(self):
      #self.ui.labChartXY = QLabel("Chart X=,  Y=  ")   #图表坐标
      self.ui.labChartXY.setMinimumWidth(200)

      #self.ui.labHoverXY = QLabel("Hovered X=,  Y=  ") #序列hover点坐标
      self.ui.labHoverXY.setMinimumWidth(200)

      #self.ui.labClickXY = QLabel("Clicked X=,  Y=  ") #序列click点坐标
      self.ui.labClickXY.setMinimumWidth(200)
      
##  ==============event处理函数==========================


##  ==========由connectSlotsByName()自动连接的槽函数============        
      
##========工具栏上的几个按钮的Actions==============
   @pyqtSlot()   
   def on_btn_calc_clicked(self):  
      try:
         self.params_a = float(self.ui.para_a.text())
         self.params_b = float(self.ui.para_b.text())
         self.params_c = float(self.ui.para_c.text())
         self.sec_func(self.params_a, self.params_b, self.params_c)
         self.__createChart() #创建图表
         self.__prepareData()    #为序列设置数据
      except EOFError as e:
         self.show_result(e)

   @pyqtSlot()   
   def do_valueChanged(self):  
      try:
         self.ui.para_a.setText(str(self.ui.slider_a.value()))
         self.ui.para_b.setText(str(self.ui.slider_b.value()))
         self.ui.para_c.setText(str(self.ui.slider_c.value()))

         self.params_a = float(self.ui.slider_a.value())
         self.params_b = float(self.ui.slider_b.value())
         self.params_c = float(self.ui.slider_c.value())
         self.sec_func(self.params_a, self.params_b, self.params_c)
         self.__createChart() #创建图表
         self.__prepareData()    #为序列设置数据
      except EOFError as e:
         self.show_result(e)

   @pyqtSlot()   
   def on_btn_clear_clicked(self):  
      self.ui.plainTextEdit.clear()

##  =============自定义槽函数===============================        
   def do_chartView_mouseMove(self,point):   ##鼠标移动
      pt=self.chartView.chart().mapToValue(point)  #QPointF 转换为图表的数值
      hint="Chart X=%.2f,Y=%.2f"%(pt.x(),pt.y())
      self.ui.labChartXY.setText(hint)  #状态栏显示

   def do_series_hovered(self,point,state):  ##序列的hovered信号
      if state:
         hint="Hovered X=%.2f,Y=%.2f"%(point.x(),point.y())
         self.ui.labHoverXY.setText(hint)
      else:
         self.ui.labHoverXY.setText("Series X=, Y=")

   def do_series_clicked(self,point):     ##序列的click信号
      hint="Clicked X=%.2f,Y=%.2f"%(point.x(),point.y())
      self.ui.labClickXY.setText(hint)   

##  =============自定义函数===============================   
   def is_sqr(self, x):  # 判断δ开方后是否为整数
      num1 = sqrt(x)
      return int(num1) == num1

   def sqr(self, x):     # 将开方后的δ取整
      num2 = sqrt(x)
      return int(num2)
   
   def show_result(self, str_cont):
      self.ui.plainTextEdit.appendPlainText(str_cont)

   def sec_func(self, a, b, c):
      ret = {"ret_val": "未计算", "ret_data":[]}

      d = b ** 2 - a * c * 4  # 判断δ情况
      a0 = a * 2

      if d < 0:
         self.show_result("此方程无实数根")
      elif d == 0:
         self.show_result("此方程仅有一个实数根")
         self.show_result("      "+ str(-b) + "\n" + "X =-------" + "\n" + "      " + str(2 * a))    # 强制转化为分数形式
      elif d > 0:
         self.show_result("此方程有两个实数根")
         if self.is_sqr(d):   # 当δ为能开尽时
               s1 = -b + self.sqr(d)
               s2 = -b - self.sqr(d)
               x1 = s1 / a0    # 方程的根1
               x2 = s2 / a0    # 方程的根2
               if s1 % a0 == 0 and s2 % a0 == 0:   # 两根都是整数
                  self.show_result("X1 = "+ str(x1) + "\n")
                  self.show_result("X2 = "+ str(x2) + "\n")
               elif s1 % a0 == 0 and s2 % a0 != 0:     # 有一根为整数
                  self.show_result("X1 = "+ str(x1)+ "\n")
                  self.show_result("      "+ str(-b - sqrt(d))+ "\n"+ "X2 =-------"+ "\n"+ "      "+ str(a0)+ "\n")
               elif s1 % a0 != 0 and s2 % a0 == 0:     # 有一根为整数
                  self.show_result("      "+ str(-b + sqrt(d))+ "\n"+ "X1 =-------"+ "\n"+ "      "+ str(a0)+ "\n")
                  self.show_result("X2 = "+ str(x2)+ "\n")
               else:       # 两根都为浮点数时
                  self.show_result("      "+ str(-b + sqrt(d))+ "\n"+ "X1 =-------"+ "\n"+ "      "+ str(a0)+ "\n")
                  self.show_result("      "+ str(-b - sqrt(d))+ "\n"+ "X2 =-------"+ "\n"+ "      "+ str(a0)+ "\n")
         else:       # 当δ为开不尽时
               self.show_result("      "+ str(-b)+ "+ √"+ str(d)+ "\n"+ "X1 =-------"+ "\n"+ "      "+ str(a0)+ "\n")
               self.show_result("      "+ str(-b)+ "- √"+ str(d)+ "\n"+ "X2 =-------"+ "\n"+ "      "+ str(a0)+ "\n")
      return ret

##  ============窗体测试程序 ================================
if  __name__ == "__main__":        #用于当前窗体测试
   app = QApplication(sys.argv)    #创建GUI应用程序
   form=QmyMainWindow()            #创建窗体
   form.show()
   sys.exit(app.exec_())
