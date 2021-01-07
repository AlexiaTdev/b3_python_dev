import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):

	def __init__(self):
		super().__init__()
		self.setWindowTitle("my pyQt app")
		self.setLayout(qtw.QVBoxLayout())
		self.setUI()
		self.show()
	
        
	def setUI(self):
		
		#create widget and grid
		container = qtw.QWidget()
		container.setLayout(qtw.QGridLayout())

		#create object containing operation data value
		self.operationObject = [0, "", 0]

		#create screen
		self.screen = qtw.QLabel("")

		#create equal and reset buttons
		btn_equal = qtw.QPushButton("enter", clicked = self.onClickEqual)
		btn_reset = qtw.QPushButton("clear", clicked = self.onClickReset)

		# create number buttons
		btn_1 = qtw.QPushButton('1', clicked = self.onClickNumber)
		btn_2 = qtw.QPushButton('2', clicked = self.onClickNumber)
		btn_3 = qtw.QPushButton('3', clicked = self.onClickNumber)
		btn_4 = qtw.QPushButton('4', clicked = self.onClickNumber)
		btn_5 = qtw.QPushButton('5', clicked = self.onClickNumber)
		btn_6 = qtw.QPushButton('6', clicked = self.onClickNumber)
		btn_7 = qtw.QPushButton('7', clicked = self.onClickNumber)
		btn_8 = qtw.QPushButton('8', clicked = self.onClickNumber)
		btn_9 = qtw.QPushButton('9', clicked = self.onClickNumber)
		btn_0 = qtw.QPushButton('0', clicked = self.onClickNumber)

		#create operation sign button
		btn_plus = qtw.QPushButton("+", clicked = self.onClickOperation)
		btn_minus = qtw.QPushButton("-", clicked = self.onClickOperation)
		btn_times = qtw.QPushButton("*", clicked = self.onClickOperation)
		btn_div = qtw.QPushButton("/", clicked = self.onClickOperation)
		
		# add screen to layout
		container.layout().addWidget(self.screen, 0, 0, 1, 3)

		# add line2 = and reset
		container.layout().addWidget(btn_equal, 1, 0, 1, 2)
		container.layout().addWidget(btn_reset, 1, 2, 1, 2)

		# add operation sign button
		container.layout().addWidget(btn_plus, 2, 3 )
		container.layout().addWidget(btn_minus, 3, 3 )
		container.layout().addWidget(btn_times, 4, 3 )
		container.layout().addWidget(btn_div, 5, 3 )

		# add number buttons to layout
		container.layout().addWidget(btn_7, 2, 0 )
		container.layout().addWidget(btn_8, 2, 1 )
		container.layout().addWidget(btn_9, 2, 2 )

		container.layout().addWidget(btn_4, 3, 0 )
		container.layout().addWidget(btn_5, 3, 1 )
		container.layout().addWidget(btn_6, 3, 2 )

		container.layout().addWidget(btn_1, 4, 0 )
		container.layout().addWidget(btn_2, 4, 1 )
		container.layout().addWidget(btn_3, 4, 2 )

		container.layout().addWidget(btn_0, 5, 0, 1, 3 )

        # add container to widget
		self.layout().addWidget(container)
	

	def onClickNumber(self):
		numberChange = self.screen.text()+ self.sender().text()
		self.screen.setText(numberChange)

	def onClickOperation(self):
		self.operationObject[0] = self.screen.text()
		self.operationObject[1] = self.sender().text()
		self.screen.setText("")
	
	def onClickEqual(self):
		self.operationObject[2] = self.screen.text()
		if self.operationObject[1]=="+" :
			self.screen.setText(str(int(self.operationObject[0])+int(self.operationObject[2])))
		elif self.operationObject[1]=="-" :
			self.screen.setText(str(int(self.operationObject[0])-int(self.operationObject[2])))
		elif self.operationObject[1]=="*" :
			self.screen.setText(str(int(self.operationObject[0])*int(self.operationObject[2])))
		elif (self.operationObject[1]=="/" and self.operationObject[2]!="0") :
			self.screen.setText(str(int(self.operationObject[0])/int(self.operationObject[2])))
		else :
			self.screen.setText("error : division by 0 not aloud")
	
	def onClickReset(self):
		self.operationObject = [0, "", 0]
		self.screen.setText("")

	


app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
