# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scorecal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(503, 405)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 20, 361, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox1 = QtWidgets.QComboBox(Dialog)
        self.comboBox1.setGeometry(QtCore.QRect(70, 70, 111, 22))
        self.comboBox1.setMinimumSize(QtCore.QSize(111, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.comboBox1.setFont(font)
        self.comboBox1.setEditable(False)
        self.comboBox1.setObjectName("comboBox1")
        import sqlite3
        MyTeam = sqlite3.connect('cricket.db')
        curteam=MyTeam.cursor()
        sql="select Name from teams"
        cur=curteam.execute(sql)
        teams=[]
        for row in cur:
            self.comboBox1.addItem(row[0])        
        MyTeam.close()
        #self.comboBox1.addItem("")
        #self.comboBox1.addItem("")
        self.comboBox2 = QtWidgets.QComboBox(Dialog)
        self.comboBox2.setGeometry(QtCore.QRect(310, 70, 111, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.comboBox2.setFont(font)
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("match2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 110, 441, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.horizontalLayout.addWidget(self.label2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.horizontalLayout.addWidget(self.label3)
        self.ptlabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.ptlabel.setObjectName("ptlabel")
        self.horizontalLayout.addWidget(self.ptlabel)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 170, 441, 201))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget1 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.listWidget1.setFont(font)
        self.listWidget1.setObjectName("listWidget1")
        self.horizontalLayout_2.addWidget(self.listWidget1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.listWidget2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.listWidget2.setFont(font)
        self.listWidget2.setObjectName("listWidget2")
        self.horizontalLayout_2.addWidget(self.listWidget2)
        self.pb = QtWidgets.QPushButton(Dialog)
        self.pb.setGeometry(QtCore.QRect(200, 370, 121, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pb.setFont(font)
        self.pb.setObjectName("pb")
        self.pb.clicked.connect(self.calculate_score)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def calculate_score(self):
        import sqlite3
        MyTeam= sqlite3.connect('cricket.db')
        curteam=MyTeam.cursor()
        team=self.comboBox1.currentText()
        self.listWidget1.clear()
        sql="select Players, Value from teams where Name='"+team+"'"
        cur=curteam.execute(sql)
        row=cur.fetchone()
        selected=row[0].split(',')
        self.listWidget1.addItems(selected)
        team_total=0
        self.listWidget2.clear()
        match=self.comboBox2.currentText()
        for i in range(self.listWidget1.count()-1):
            total=0
            batscore=0
            bowlscore=0
            fieldscore=0
            nm=self.listWidget1.item(i).text()
            cur=curteam.execute("select * from "+match+" where Player='"+nm+"'")
            row=cur.fetchone()
            batscore=row[1]//2
            if batscore>=50: batscore+=5
            if batscore>=100: batscore+=10
            if row[1]>0:
                strike_rate=row[1]/row[2]
                if strike_rate>=80 and strike_rate<100: batscore+=2
                if strike_rate>=100:batscore+=4
            batscore=batscore+row[3]
            batscore=batscore+2*row[4]
            bowlscore=row[8]*10
            if row[8]>=3: bowlscore=bowlscore+5
            if row[8]>=5: bowlscore=bowlscore=bowlscore+10
            if row[7]>0:
                economy_rate=6*row[7]/row[5]
                if economy_rate<=2: bowlscore=bowlscore+10
                if economy_rate>2 and economy_rate<=3.5: bowlscore=bowlscore+7
                if economy_rate>3.5 and economy_rate<=4.5: bowlscore=bowlscore+4
            fieldscore=(row[9]+row[10]+row[11])*10            
            total=batscore+bowlscore+fieldscore
            self.listWidget2.addItem(str(total))
            team_total=team_total+total
            
        
        self.ptlabel.setText(str(team_total))
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Evaluate the performance of your fantasy team "))
        self.comboBox1.setItemText(0, _translate("Dialog", "Select Team"))
        self.comboBox1.setItemText(1, _translate("Dialog", "team1"))
        self.comboBox2.setItemText(0, _translate("Dialog", "Select Match"))
        self.comboBox2.setItemText(1, _translate("Dialog", "match"))
        self.label2.setText(_translate("Dialog", "  Players  "))
        self.label3.setText(_translate("Dialog", "Points"))
        self.ptlabel.setText(_translate("Dialog", " "))
        self.pb.setText(_translate("Dialog", "Calculate Score"))

        self.ptlabel.setText(_translate("Dialog", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
