import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def main():
    app = QApplication(sys.argv)
    win = QWidget()

    e1 = QLineEdit()
    e1.setValidator(QIntValidator())
    e1.setMaxLength(4)
    e1.setAlignment(Qt.AlignmentFlag.AlignRight)
    e1.setFont(QFont("Arial", 20))

    e2 = QLineEdit()
    e2.setValidator(QDoubleValidator(0.99, 99.99, 2))

    flo = QFormLayout()
    flo.addRow("Integer validator", e1)
    flo.addRow("Double validator", e2)

    e3 = QLineEdit()
    e3.setInputMask("+99_99999")
    flo.addRow("Input mask", e3)

    e4 = QLineEdit()
    e4.textChanged.connect(textChanged)
    flo.addRow("Text changed", e4)

    win.setLayout(flo)
    win.setWindowTitle("Nam_Test")
    win.show()
    sys.exit(app.exec_())

def textChanged(text):
    print(text)


if __name__ == "__main__":
    main()