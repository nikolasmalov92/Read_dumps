import subprocess
import time
import serial.tools.list_ports
import sys
import os
from subprocess import check_output
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton, QTextEdit, QFileDialog


ports = serial.tools.list_ports.comports()
astrah_path = 'astrah.exe'

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.combo = QComboBox(self)
        self.combo.move(10, 40)
        result = []
        for port in ports:
            self.p = port.device
            result.append(self.p)
            self.combo.addItem(self.p)
        self.send_btn_stop = QPushButton('Остановить',self)
        self.send_btn_stop.move(50,115)
        self.send_btn_stop.clicked.connect(self.act)
        self.send_btn_activate = QPushButton('Активация', self)
        self.send_btn_activate.move(175, 115)
        self.send_btn_activate.clicked.connect(self.act_2)
        self.send_btn_deactivate = QPushButton('Деактивация', self)
        self.send_btn_deactivate.move(305, 115)
        self.send_btn_deactivate.clicked.connect(self.act_3)
        self.qlabel_0 = QLabel('Выбор COM-porta:',self)
        self.qlabel_0.move(10, 10)
        self.qlabel = QLabel('Остановка системы',self)
        self.qlabel.move(50, 90)
        self.qlabel_2 = QLabel('Активация диска',self)
        self.qlabel_2.move(185, 90)
        self.qlabel_3 = QLabel('Деактивация диска',self)
        self.qlabel_3.move(305, 90)
        self.text = QTextEdit(self)
        self.text.move(5,155)
        self.text.resize(410, 70)
        # command = 'net STOP msscore'
        # get_command = os.system(command)
        self.setGeometry(50, 50, 420, 230)
        self.setWindowTitle("Изменение виртуальных дисков")
        self.show()


    def act(self):
        combo_port = ports[self.combo.currentIndex()]
        combo_port_d = combo_port.device
        byte_0 = "Custom"
        byte_0_0 = "\\\.\\"
        byte_1 = "FF"
        byte_2 = "C000"
        cmd = check_output(astrah_path + ' ' + byte_0 + ' ' + byte_0_0 + combo_port_d + 
                        ' ' + byte_1 + ' ' + byte_2, universal_newlines=True)  
            
        self.text.append(" -- Система остановлена -- " + cmd)
        return cmd


    def act_2(self):
        byte_0 = "Custom"
        byte_1 = "FF"
        byte_2 = "C04301"
        byte_0_0 = "\\\.\\"
        combo_port = ports[self.combo.currentIndex()]
        combo_port_d = combo_port.device
        cmd = check_output(astrah_path + ' ' + byte_0 + ' ' + byte_0_0 + combo_port_d + 
                        ' ' + byte_1 + ' ' + byte_2, universal_newlines=True)   
        self.text.append(" -- Команда активирования виртуальных дисков -- " + cmd)
        return cmd
        
    def act_3(self):
        byte_0 = "Custom"
        byte_1 = "FF"
        byte_2 = "А40201"
        byte_0_0 = "\\\.\\"
        combo_port = ports[self.combo.currentIndex()]
        combo_port_d = combo_port.device
        cmd = check_output(astrah_path + ' ' + byte_0 + ' ' + byte_0_0 + combo_port_d + 
                        ' ' + byte_1 + ' ' + byte_2, universal_newlines=True)
        self.text.append(" -- Команда деактивирования виртуальных дисков -- " + cmd)
        return cmd

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
