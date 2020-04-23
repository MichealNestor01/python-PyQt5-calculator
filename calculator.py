from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        #Though this layout was created in qt designer I have tried to make the code smaller through saving styles in variables for example
        #the style for the number button styles
        numberButtonStyle = ("QPushButton{\n"
        "    color: white;\n"
        "    background: black;\n"
        "}\n"
        "QPushButton:hover:!pressed{\n"
        "    color: black;\n"
        "    background: white;\n"
        "}")
        functionButtonStyle = ("QPushButton{\n"
        "    color:magenta;\n"
        "    background: black;\n"
        "}\n"
        "QPushButton:hover:!pressed{\n"
        "    color: black;\n"
        "    background: white;\n"
        "}")
        lcdANDlabelStyle = ("\n"
        "    color:magenta;\n"
        "    background: black;\n"
        "")
        #below is the creation of the layout, all of the buttons, labels and lcd screens
        Calculator.setObjectName("Calculator")
        Calculator.resize(600, 569)
        Calculator.setMinimumSize(QtCore.QSize(600, 569))
        Calculator.setMaximumSize(QtCore.QSize(600, 569))
        self.calculator = QtWidgets.QWidget(Calculator)
        self.calculator.setObjectName("calculator")
        self.PrimaryLcd = QtWidgets.QLCDNumber(self.calculator)
        self.PrimaryLcd.setGeometry(QtCore.QRect(440, 0, 161, 31))
        self.PrimaryLcd.setAutoFillBackground(False)
        self.PrimaryLcd.setStyleSheet(lcdANDlabelStyle)
        self.PrimaryLcd.setFrameShadow(QtWidgets.QFrame.Plain)
        self.PrimaryLcd.setLineWidth(2)
        self.PrimaryLcd.setDigitCount(10)
        self.PrimaryLcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.PrimaryLcd.setObjectName("PrimaryLcd")
        self.SecondaryLcd = QtWidgets.QLCDNumber(self.calculator)
        self.SecondaryLcd.setGeometry(QtCore.QRect(440, 60, 161, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.SecondaryLcd.setFont(font)
        self.SecondaryLcd.setAutoFillBackground(False)
        self.SecondaryLcd.setStyleSheet(lcdANDlabelStyle)
        self.SecondaryLcd.setFrameShadow(QtWidgets.QFrame.Plain)
        self.SecondaryLcd.setLineWidth(2)
        self.SecondaryLcd.setDigitCount(10)
        self.SecondaryLcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.SecondaryLcd.setObjectName("SecondaryLcd")
        self.FunctionLabel = QtWidgets.QLabel(self.calculator)
        self.FunctionLabel.setGeometry(QtCore.QRect(440, 30, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.FunctionLabel.setFont(font)
        self.FunctionLabel.setAutoFillBackground(False)
        self.FunctionLabel.setStyleSheet(lcdANDlabelStyle)
        self.FunctionLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.FunctionLabel.setLineWidth(2)
        self.FunctionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FunctionLabel.setObjectName("FunctionLabel")
        self.seven = QtWidgets.QPushButton(self.calculator)
        self.seven.setGeometry(QtCore.QRect(0, 90, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(100)
        self.seven.setFont(font)
        self.seven.setStyleSheet(numberButtonStyle)
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(self.calculator)
        self.eight.setGeometry(QtCore.QRect(120, 90, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(100)
        self.eight.setFont(font)
        self.eight.setStyleSheet(numberButtonStyle)
        self.eight.setObjectName("eight")
        self.nine = QtWidgets.QPushButton(self.calculator)
        self.nine.setGeometry(QtCore.QRect(240, 90, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(100)
        self.nine.setFont(font)
        self.nine.setStyleSheet(numberButtonStyle)
        self.nine.setObjectName("nine")
        self.addition = QtWidgets.QPushButton(self.calculator)
        self.addition.setGeometry(QtCore.QRect(360, 90, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(50)
        self.addition.setFont(font)
        self.addition.setStyleSheet(functionButtonStyle)
        self.addition.setObjectName("addition")
        self.subtraction = QtWidgets.QPushButton(self.calculator)
        self.subtraction.setGeometry(QtCore.QRect(480, 90, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(50)
        self.subtraction.setFont(font)
        self.subtraction.setStyleSheet(functionButtonStyle)
        self.subtraction.setObjectName("subtraction")
        self.six = QtWidgets.QPushButton(self.calculator)
        self.six.setGeometry(QtCore.QRect(0, 210, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(100)
        self.six.setFont(font)
        self.six.setStyleSheet(numberButtonStyle)
        self.six.setObjectName("six")
        self.five = QtWidgets.QPushButton(self.calculator)
        self.five.setGeometry(QtCore.QRect(120, 210, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(100)
        self.five.setFont(font)
        self.five.setStyleSheet(numberButtonStyle)
        self.five.setObjectName("five")
        self.four = QtWidgets.QPushButton(self.calculator)
        self.four.setGeometry(QtCore.QRect(240, 210, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(100)
        self.four.setFont(font)
        self.four.setStyleSheet(numberButtonStyle)
        self.four.setObjectName("four")
        self.divides = QtWidgets.QPushButton(self.calculator)
        self.divides.setGeometry(QtCore.QRect(360, 210, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(50)
        self.divides.setFont(font)
        self.divides.setStyleSheet(functionButtonStyle)
        self.divides.setObjectName("divides")
        self.multiply = QtWidgets.QPushButton(self.calculator)
        self.multiply.setGeometry(QtCore.QRect(480, 210, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(50)
        self.multiply.setFont(font)
        self.multiply.setStyleSheet(functionButtonStyle)
        self.multiply.setObjectName("multiply")
        self.three = QtWidgets.QPushButton(self.calculator)
        self.three.setGeometry(QtCore.QRect(0, 330, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(100)
        self.three.setFont(font)
        self.three.setStyleSheet(numberButtonStyle)
        self.three.setObjectName("three")
        self.two = QtWidgets.QPushButton(self.calculator)
        self.two.setGeometry(QtCore.QRect(120, 330, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(100)
        self.two.setFont(font)
        self.two.setStyleSheet(numberButtonStyle)
        self.two.setObjectName("two")
        self.one = QtWidgets.QPushButton(self.calculator)
        self.one.setGeometry(QtCore.QRect(240, 330, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(100)
        self.one.setFont(font)
        self.one.setStyleSheet(numberButtonStyle)
        self.one.setObjectName("one")
        self.percentage = QtWidgets.QPushButton(self.calculator)
        self.percentage.setGeometry(QtCore.QRect(360, 330, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(50)
        self.percentage.setFont(font)
        self.percentage.setStyleSheet(functionButtonStyle)
        self.percentage.setObjectName("percentage")
        self.pulsMinus = QtWidgets.QPushButton(self.calculator)
        self.pulsMinus.setGeometry(QtCore.QRect(480, 330, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(50)
        self.pulsMinus.setFont(font)
        self.pulsMinus.setStyleSheet(functionButtonStyle)
        self.pulsMinus.setObjectName("pulsMinus")
        self.zero = QtWidgets.QPushButton(self.calculator)
        self.zero.setGeometry(QtCore.QRect(120, 450, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(100)
        self.zero.setFont(font)
        self.zero.setStyleSheet(numberButtonStyle)
        self.zero.setObjectName("zero")
        self.AC = QtWidgets.QPushButton(self.calculator)
        self.AC.setGeometry(QtCore.QRect(0, 450, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(50)
        self.AC.setFont(font)
        self.AC.setStyleSheet(functionButtonStyle)
        self.AC.setObjectName("AC")
        self.C = QtWidgets.QPushButton(self.calculator)
        self.C.setGeometry(QtCore.QRect(240, 450, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(50)
        self.C.setFont(font)
        self.C.setStyleSheet(functionButtonStyle)
        self.C.setObjectName("C")
        self.decimal = QtWidgets.QPushButton(self.calculator)
        self.decimal.setGeometry(QtCore.QRect(360, 450, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(50)
        self.decimal.setFont(font)
        self.decimal.setStyleSheet(functionButtonStyle)
        self.decimal.setObjectName("decimal")
        self.equals = QtWidgets.QPushButton(self.calculator)
        self.equals.setGeometry(QtCore.QRect(480, 450, 120, 120))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(50)
        self.equals.setFont(font)
        self.equals.setStyleSheet(functionButtonStyle)
        self.equals.setObjectName("equals")
        self.MainLcd = QtWidgets.QLCDNumber(self.calculator)
        self.MainLcd.setGeometry(QtCore.QRect(0, 0, 441, 90))
        self.MainLcd.setStyleSheet(lcdANDlabelStyle)
        self.MainLcd.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MainLcd.setLineWidth(2)
        self.MainLcd.setDigitCount(10)
        self.MainLcd.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.MainLcd.setProperty("value", 0.0)
        self.MainLcd.setObjectName("MainLcd")
        Calculator.setCentralWidget(self.calculator)
        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

        #These lines link all of the push buttons to class methods
        self.AC.clicked.connect(self.ACFunction)
        self.C.clicked.connect(self.clearMain)
        self.zero.clicked.connect(self.zeroMethod)
        self.one.clicked.connect(self.oneMethod)
        self.two.clicked.connect(self.twoMethod)
        self.three.clicked.connect(self.threeMethod)
        self.four.clicked.connect(self.fourMethod)
        self.five.clicked.connect(self.fiveMethod)
        self.six.clicked.connect(self.sixMethod)
        self.seven.clicked.connect(self.sevenMethod)
        self.eight.clicked.connect(self.eightMethod)
        self.nine.clicked.connect(self.nineMethod)
        self.addition.clicked.connect(self.additionMethod)
        self.equals.clicked.connect(self.equalsMethod)
        self.subtraction.clicked.connect(self.subtractionMethod)
        self.pulsMinus.clicked.connect(self.plusMinusFunction)
        self.multiply.clicked.connect(self.multiplicationFunction)
        self.divides.clicked.connect(self.divideFunction)
        self.percentage.clicked.connect(self.percentageFunction)
        self.decimal.clicked.connect(self.decimalFunction)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.FunctionLabel.setText(_translate("Calculator", "-------------------------"))
        self.seven.setText(_translate("Calculator", "7"))
        self.eight.setText(_translate("Calculator", "8"))
        self.nine.setText(_translate("Calculator", "9"))
        self.addition.setText(_translate("Calculator", "+"))
        self.subtraction.setText(_translate("Calculator", "-"))
        self.six.setText(_translate("Calculator", "6"))
        self.five.setText(_translate("Calculator", "5"))
        self.four.setText(_translate("Calculator", "4"))
        self.divides.setText(_translate("Calculator", "/"))
        self.multiply.setText(_translate("Calculator", "x"))
        self.three.setText(_translate("Calculator", "3"))
        self.two.setText(_translate("Calculator", "2"))
        self.one.setText(_translate("Calculator", "1"))
        self.percentage.setText(_translate("Calculator", "%"))
        self.pulsMinus.setText(_translate("Calculator", "+/-"))
        self.zero.setText(_translate("Calculator", "0"))
        self.AC.setText(_translate("Calculator", "A/C"))
        self.C.setText(_translate("Calculator", "C"))
        self.decimal.setText(_translate("Calculator", "."))
        self.equals.setText(_translate("Calculator", "="))
        #mode refers to whether or not the user is inputing a float or integer
        self.mode = 'normal'
        self.decimalTyped = False
        #function refers to the selected operator function
        self.function = ''
        #answer refers to whether or not an answer is being displayed on the main lcd display
        self.answer = False

    #This method calculates an answer depending on the selected function
    def equalsMethod(self):
        #the second value entered is stored in the number variable
        number = self.MainLcd.value()
        self.SecondaryLcd.display(float(number))
        answer = number
        #the first value entered is stored in the secondNumber variable
        secondNumber = self.PrimaryLcd.value()
        if self.function == 'addition':
            answer = number + secondNumber
        if self.function == 'subtraction':
            answer = secondNumber - number
        if self.function == 'multiplication':
            answer = secondNumber * number     
        if self.function == 'division':
            answer = secondNumber / number  
        if self.function == 'percentage':
            answer = (secondNumber/100) * number
        #the answer is displayed on the main lcd display
        self.MainLcd.display(answer)
        self.answer = True                    

    #this is a function that is makes the code more efficient since it is used in all of the math operator functions
    def functionChangeDisplay(self):
        self.mode = 'normal'
        self.decimalTyped = False
        number = self.MainLcd.value()
        self.MainLcd.display(0)
        self.PrimaryLcd.display(float(number))

    #this prepares the calculator to take 'n' percent of the next number entered into the display
    def percentageFunction(self):
        self.function = 'percentage'
        self.functionChangeDisplay()
        self.FunctionLabel.setText('Percent of: ')

    #this prepares the calculator to divide the number entered into the main lcd by another number
    def divideFunction(self):
        self.function = 'division'
        self.functionChangeDisplay()
        self.FunctionLabel.setText('Divided By:')

    #this prepares the calculator to multiply the number entered into the main lcd by another number
    def multiplicationFunction(self):
        self.function = 'multiplication'
        self.functionChangeDisplay()
        self.FunctionLabel.setText('Multiplied by:') 

    #this prepares the calculator to subtract the number entered into the main lcd by another number
    def subtractionMethod(self):
        self.function = 'subtraction'
        self.functionChangeDisplay()
        self.FunctionLabel.setText('Subtract:')

    #this prepares the calculator to add the number entered into the main lcd to another number
    def additionMethod(self):
        self.function = 'addition'
        self.functionChangeDisplay()
        self.FunctionLabel.setText('Added to:')

    #this function allows users to input a decimal number into the main lcd
    def decimalFunction(self):
        self.mode = 'decimal'

    #this fuction reverses the sign on the number entered into the main lcd screen
    def plusMinusFunction(self):
        number = str(self.MainLcd.value())
        if number[0] == '-':
            length = len(number)
            number = number[1:length]
            self.MainLcd.display(float(number))
        else:
            number = '-' + number
            self.MainLcd.display(float(number))

    #this is the classic clean all function, it clears all the lcd displays and it clears the fuction selection and label
    def ACFunction(self):
        self.MainLcd.display(0)
        self.SecondaryLcd.display(0)
        self.PrimaryLcd.display(0)
        self.FunctionLabel.setText('-------------------------')
        self.function = ''
        self.decimalTyped = False
        self.mode = 'normal'

    #this is the classic clear function and it clears just the contents of the main lcd display
    def clearMain(self):
        self.MainLcd.display(0)
        self.decimalTyped = False
        self.mode = 'normal'

    #below are all of the functions for the number butons
    def zeroMethod(self):
        self.postAnswerClick()
        self.formatMain(0)

    def oneMethod(self):
        self.postAnswerClick()
        self.formatMain(1)

    def twoMethod(self):
        self.postAnswerClick()
        self.formatMain(2)

    def threeMethod(self):
        self.postAnswerClick()
        self.formatMain(3)

    def fourMethod(self):
        self.postAnswerClick()
        self.formatMain(4)

    def fiveMethod(self):
        self.postAnswerClick()
        self.formatMain(5)

    def sixMethod(self):
        self.postAnswerClick()
        self.formatMain(6)

    def sevenMethod(self):
        self.postAnswerClick()
        self.formatMain(7)

    def eightMethod(self):
        self.postAnswerClick()
        self.formatMain(8)

    def nineMethod(self):
        self.postAnswerClick()
        self.formatMain(9)

    #this code was repeated in all of the 'numberMethod' functions so to make the code more efficient I put it in its own function
    def postAnswerClick(self):
        if self.answer == True:
            self.mode = 'normal'
            self.decimalTyped = False
            self.MainLcd.display(0)
            self.answer = False

    #this is the function that formats the main lcd display it
    def formatMain(self, number):
        #formats the main screen for non decimal numbers:
        if self.mode == 'normal':
            displaycontents = self.MainLcd.intValue()
            #this formats the first pressed number
            if displaycontents == 0:
                self.MainLcd.display(number)
            #this formats numbers after the first has been typed
            else:
                if len(str(displaycontents)) < 9:
                    new = str(displaycontents) + str(number)
                    self.MainLcd.display(float(new))
        #formats decimal numbers: 
        else:
            #formats the first number after the decimal point
            if self.decimalTyped == False:
                self.decimalTyped = True
                displaycontents = self.MainLcd.intValue()
                if len(str(displaycontents)) < 9:
                    new = str(displaycontents) + '.' + str(number)
                    self.MainLcd.display(float(new))
            #formats the rest of the numbers after the decimal point
            else:
                displaycontents = self.MainLcd.value()
                if len(str(displaycontents)) < 9:
                    new = str(displaycontents) + str(number)
                    self.MainLcd.display(float(new))

#main function that runs the calculator window
def main():
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    app.exec_()

#runs the main function 
if __name__ == "__main__":
    main()


