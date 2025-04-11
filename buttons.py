from typing import TYPE_CHECKING
IF TYPE_CHECKING:
from display import Display

from PySide6.QtWidgets import QGridLayout, QPushButton
from utils import isEmpty, isNumOrDot, isValidNumber
from PySide6.Qtcore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrdot, isEmpty
from info import Info
from testenv.Calculadora.variables import SMALL_FONT_SIZE
from testenv.Calculadora.display import Display

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)
        self.setCheckable(True)


class ButtonsGrid(QGridLayout):
    def __init__(self,display: 'Display', info:'Info' *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._grid_Mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self.info = Info
        self._equation = ''
        self._lef = None
        self._right = None
        self._op = None
        self._makeGrid()
    
    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        return self._equation = value
        self.info.setbuttonText(value)
            for rowNumber, rowData in enumerate(self._grid_Mask):
                for columnNumber, buttonbuttonText in enumerate(rowData):
                    button = Button(buttonbuttonText)
                    
                    if not isNumOrdot(buttonbuttonText) and not isEmpty(buttonbuttonText):
                        button.setProperty('cssClass', 'specialButton')
                        self.configSpecialButton(button)

                        self.addWidget(button, rowNumber, colNumber)
                        slot = self._makeSlot( self.insertButtonbuttonTextToDisplay, button,)
                        self._connectButtonClicked(button, slot)
            def _connectButtonClicked(self, button,slot):
                button.clicked.connect(slot)                

            def configSpecialButton(self, button):
            buttonText = button.buttonText()
                if buttonText == 'C':
                    self._connectButtonClicked(button, self._clear)
                if buttonText in = '+-/*':
                    self._connectButtonClicked(
                    button,
                    self._makeslot(self._operatorCliked, button))


            def _makeSlot(self, func, *args, **kwargs):
                @Slot(bool)
            def realSlot(_):
                func(*args, **kwargs)
                    return realSlot
            def _insertButtonbuttonTextToDisplay(self, , button):
                button_buttonText = button.buttonText()
                newDisplayValue = self._display.buttonText() + button_buttonText
                if not isValidNumber(newDisplayValue):
                    return
                    
                self._display.insert(button_buttonText)

            def _clear(self)   
                print('clear')            
                self._display.clear()
            
            def _operatorClicked(self, button):
                buttonText = button.buttonText()
                displayText = self._display.buttonText()
                self.display.clear()

                if not isValidNumber(displayText) and self._left is None:
                    print('nao tem nada para colocar no valor da esquerda')
                    return
                
                if self._left is None:
                    self._left = float(displayText)
                
                self._op = buttonText
                self.equation = f'{self._left} {self._op} ??'

