import sys
from PyQt5 import QtWidgets, QtGui

def window():
	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QWidget()
	l1 = QtWidgets.QLabel(w)
	l2 = QtWidgets.QLabel(w)
	b = QtWidgets.QPushButton(w)
	b.setText("Push me")
	l1.setText("Demo")
	l2.setPixmap(QtGui.QPixmap('re.jpg'))
	w.setWindowTitle("Demo")
	l1.move(100, 50)
	l2.move(120, 90)
	b.move(100,30)
	w.show()
	sys.exit(app.exec_())
	
window()