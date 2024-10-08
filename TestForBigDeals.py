import math
import sys
from PyQt5 import QtWidgets
from calculator import Ui_widget



class WidgetAR(QtWidgets.QWidget, Ui_widget):
    def __init__(self, *args, obj=None, **kwargs):
        super(WidgetAR, self).__init__(*args, **kwargs)
        self.setupUi(self)


        self.oneButton.clicked.connect(self.num_one)
        self.twoButton.clicked.connect(self.num_two)
        self.threeButton.clicked.connect(self.num_three)
        self.fourButton.clicked.connect(self.num_four)
        self.fifeButton.clicked.connect(self.num_fife)
        self.sixButton.clicked.connect(self.num_six)
        self.sevenButton.clicked.connect(self.num_seven)
        self.eightButon.clicked.connect(self.num_eight)
        self.nineButton.clicked.connect(self.num_nine)
        self.zeroButton.clicked.connect(self.num_zero)

        self.delAllButton.clicked.connect(self.clear_all)
        self.delLastSymbolButton.clicked.connect(self.clear_last_symbol)
        self.openBracketButton.clicked.connect(self.open_bracket)
        self.closeBracketButton.clicked.connect(self.close_bracket)
        self.PiButton.clicked.connect(self.Pi_func)

        self.plusButton.clicked.connect(self.addition)
        self.minusButton.clicked.connect(self.subtraction)
        self.divisionButton.clicked.connect(self.division_func)
        self.eButton.clicked.connect(self.value_e)
         self.rootOfButton.clicked.connect(self.sqrt_func)
        self.multiplicationButton.clicked.connect(self.multiplication_func)
        self.degreeButton.clicked.connect(self.degree_func)
        self.oneOfButton.clicked.connect(self.one_of_func)
        self.dotButton.clicked.connect(self.dot)
        
        self.equalsButton.clicked.connect(self.equals_func)
    
    def equals_func(self):
        a = self.label.text()
        
        if '√' or '^' or 'x' in a:
            b = [x.replace('^', '**') for x in a]
            b = [x.replace('√', '0.5 **') for x in b] 
            b = [x.replace('x', '*') for x in b]
            c = ''

            for x in b:
               c += x

            a = c
            
        try:
            values = str(eval(a))
            if len(values) >= 34:
                values[0:34]
            self.label.setText(values)
        except ZeroDivisionError:
            self.label.setText('0')
        except SyntaxError:
            self.label.setText('Invalid syntaxis. Try again')

        
         

      
    def sqrt_func(self):
          a = self.label.text()
          self.label.setText(a + '√')

          if len(a) >= 34:
              self.label.setText(a[:-1])

    def addition(self):
        a = self.label.text()
        self.label.setText(a + '+')
        if len(a) >= 34:
            self.label.setText(a[:-1])

    def subtraction(self): 
        a = self.label.text()
        self.label.setText(a + '-')
        if len(a) >= 34:
            self.label.setText(a[:-1])

    def multiplication_func(self):
        a = self.label.text()
        self.label.setText(a + 'x')
        if len(a) >= 34:
            self.label.setText(a[:-1])

    def division_func(self):
        a = self.label.text()
        self.label.setText(a + '/')
        if len(a) >= 34:
            self.label.setText(a[:-1])

    def degree_func(self):
        a = self.label.text()
        self.label.setText(a + '^')
        if len(a) >= 34:
            self.label.setText(a[:-1])

    def one_of_func(self): 
        a = self.label.text()
        self.label.setText(a + '^(-1)')
        if len(a) >= 30:
            self.label.setText(a)

    def Pi_func(self):
        a = self.label.text()
        self.label.setText(a + str(math.pi)) 
        if len(a) >= 18:
            self.label.setText(a)

    def value_e(self):
        a = self.label.text()
        self.label.setText(a + '2.71828182845')
        if len(a) >= 26:
            self.label.setText(a)
    
    def clear_all(self):
        self.label.setText('')

    def clear_last_symbol(self):
        a = self.label.text()
        self.label.setText(a[:-1])

    def open_bracket(self):
        a = self.label.text()
        self.label.setText(a + '(')
        if len(a) >= 34:
            self.label.setText(a[:-1])

    def close_bracket(self):
        a = self.label.text()
        self.label.setText(a + ')')
        if len(a) >= 34:
            self.label.setText(a[:-1])
    
    def dot(self):
        a = self.label.text()
        self.label.setText(a + '.')
        if len(a) >= 34:
            self.label.setText(a[:-1])

    def num_one(self):
        a = self.label.text()
        self.label.setText(a + '1')
        if len(a) >= 34:
            self.label.setText(a[:-1])

    def num_two(self):
        a = self.label.text()
        self.label.setText(a + '2')
        if len(a) >= 34:
            self.label.setText(a[:-1])

    def num_three(self):
        a = self.label.text()
        self.label.setText(a + '3')
        if len(a) >= 34:
            self.label.setText(a[:-1])

    def num_four(self):
        a = self.label.text()
        self.label.setText(a + '4')
        if len(a) >= 34:
            self.label.setText(a[:-1])

    def num_fife(self):
        a = self.label.text()
        self.label.setText(a + '5')
        if len(a) >= 34:
            self.label.setText(a[:-1])

    def num_six(self):
        a = self.label.text()
        self.label.setText(a + '6')
        if len(a) >= 34:
            self.label.setText(a[:-1])

    def num_seven(self):
        a = self.label.text()
        self.label.setText(a + '7')
        if len(a) >= 34:
            self.label.setText(a[:-1])

    def num_eight(self):
        a = self.label.text()
        self.label.setText(a + '8')
        if len(a) >= 34:
            self.label.setText(a[:-1])

    def num_nine(self):
        a = self.label.text()
        self.label.setText(a + '9')
        if len(a) >= 34:
            self.label.setText(a[:-1])

    def num_zero(self):
        a = self.label.text()
        self.label.setText(a + '0')
        if len(a) >= 34:
            self.label.setText(a[:-1])

appee = QtWidgets.QApplication(sys.argv)

win = WidgetAR()
win.show()

appee.exec()