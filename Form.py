import sys
from PyQt5 import QtWidgets, QtGui

def window():
	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QWidget()
	l1 = QtWidgets.QLabel("Push me")
	#l2 = QtWidgets.QLabel(w)
	b = QtWidgets.QPushButton("Demo")
	h_box = QtWidgets.QHBoxLayout()
	h_box.addStretch()
	h_box.addWidget(l1)
	h_box.addStretch()

	v_box = QtWidgets.QVBoxLayout()
	v_box.addWidget(b)
	v_box.addLayout(h_box)
	w.setLayout(v_box)
	#l2.setPixmap(QtGui.QPixmap('re.jpg'))
	w.setWindowTitle("Demo")
	#l1.move(100, 50)
	#l2.move(120, 90)
	#b.move(100,30)
	w.show()
	sys.exit(app.exec_())
	
window()