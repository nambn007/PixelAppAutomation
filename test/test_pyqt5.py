import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def main():
    app = QApplication(sys.argv)
    win = QWidget()

    l1 = QLabel()
    l2 = QLabel()
    l3 = QLabel()
    l4 = QLabel()

    l1.setText('Hello world')
    l2.setText('Hello world 2')
    l3.setText('Hello world 3')
    l4.setText('Hello world 4')

    l1.setAlignment(Qt.AlignmentFlag.AlignCenter)
    l3.setAlignment(Qt.AlignmentFlag.AlignCenter)
    l4.setAlignment(Qt.AlignmentFlag.AlignRight)

    vbox = QVBoxLayout()
    vbox.addWidget(l1)
    vbox.addStretch()
    vbox.addWidget(l2)
    vbox.addStretch()
    vbox.addWidget(l3)
    vbox.addStretch()
    vbox.addWidget(l4)

    l1.setOpenExternalLinks(True)
    l4.linkActivated.connect(clicked)
    l2.linkHovered.connect(hovered)
    win.setLayout(vbox)

    win.setWindowTitle("Namdztest")
    win.show()
    sys.exit(app.exec_())

def hovered():
    print("Hovering")

def clicked():
    print("Clicked")


if __name__ == "__main__":
    main()