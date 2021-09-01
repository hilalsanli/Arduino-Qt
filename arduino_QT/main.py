from PyQt5 import QtWidgets,QtCore
import sys
from arayuz import Ui_MainWindow
import serial
import csv
import time
import datetime
import serial.tools.list_ports
from PyQt5.QtCore import QTimer
import numpy as np
global say,say2

class serialThreadClass(QtCore.QThread):  # Seri Porttan veri okuma işlemi için QThread Kullanıldı.

    message = QtCore.pyqtSignal(str)
    def __init__(self,parent = None):

        super(serialThreadClass,self).__init__(parent)
        self.serialPort = serial.Serial()

class arduino(QtWidgets.QMainWindow):
    def __init__(self):
        super(arduino, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer_veri=QTimer()
        self.timer_veri.timeout.connect(self.kaydet)
        self.ui.btn_kaydet_3.clicked.connect(self.veri_timer)
        self.ui.btn_baglan.clicked.connect(self.baglan)
        self.ui.btn_kaydet_3.clicked.connect(self.kaydet)
        self.ui.btn_baglanti_kes_3.clicked.connect(self.baglanti_kes)
        self.ui.btn_baglanti_kes_3.setEnabled(False)

        ports=serial.tools.list_ports.comports()
        for i in ports:
            self.ui.cmb_com_3.addItem(str(i))

        baud = ["300", "1200", "2400", "4800", "9600", "19200", "38400", "57600", "74880",
                         "115200", "230400", "250000", "500000", "1000000", "2000000"]
        for i in baud:
            self.ui.cmb_baud_3.addItem(str(i))
        self.ui.cmb_baud_3.setCurrentText(baud[9])

        self.mySerial = serialThreadClass()
        self.mySerial.start()




    def baglan(self):
        self.portText=self.ui.cmb_com_3.currentText()
        self.port=self.portText.split()
        self.baudrate = self.ui.cmb_baud_3.currentText()
        print(self.baudrate)

        self.mySerial.serialPort.baudrate = int(self.baudrate)
        self.mySerial.serialPort.port = self.port[0]

        try:
            self.mySerial.serialPort.open()
        except:
            self.ui.txt_log_3.append("Bağlantı Hatası")
        if (self.mySerial.serialPort.isOpen()):
            self.ui.txt_log_3.append("Bağlantı Başarılı")
            self.ui.btn_baglanti_kes_3.setEnabled(True)
        print(self.mySerial)

    def baglanti_kes(self):
         if self.mySerial.serialPort.isOpen():
             self.mySerial.serialPort.close()
             if self.mySerial.serialPort.isOpen() == False:
                 self.ui.txt_log_3.append("Bağlantı Sonlandırıldı!!!")

    def kaydet(self):
        global veri
        global f

        now = datetime.datetime.now()
        t = now.strftime('%H:%M:%S')

        veri = str(t+"   "+self.mySerial.serialPort.readline().decode().strip())
        veri_array=np.array(veri)
        print(veri_array)
        self.ui.txt_log_3.append(str(veri_array))
        with open ('veri.csv', 'a') as f:
                f.write(str(veri_array)+ "\n")
        f.close()

    def veri_timer(self):
        self.timer_veri.start(0)
def app():
    app=QtWidgets.QApplication(sys.argv)
    win=arduino()
    win.show()
    sys.exit(app.exec_())
app()