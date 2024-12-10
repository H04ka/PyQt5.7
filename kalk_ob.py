from PyQt5 import QtWidgets
import bobr_kurwa


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = bobr_kurwa.Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.sum)
        self.ui.pushButton_2.clicked.connect(self.clear)

    def sum(self):
        a = float(self.ui.lineEdit.text())
        b = float(self.ui.lineEdit_2.text())
        c = float(self.ui.lineEdit_3.text())
        d = a * b * c
        self.ui.label_5.setText(f"Сумма = {str(d)}")
    
    def clear(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.label_5.setText(f"ОТВЕТ = ")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())