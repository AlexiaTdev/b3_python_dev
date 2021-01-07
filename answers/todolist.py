import PyQt5.QtWidgets as qtw
import json
import os
import glob


class MainWindow(qtw.QWidget):

	def __init__(self):
		super().__init__()
		self.setWindowTitle("my pyQt app")
		self.setLayout(qtw.QVBoxLayout())
		self.setUI()
		self.show()
	
        
	def setUI(self):
		
		#create 2 widget containers and grids
		self.container = qtw.QWidget()
		self.container.setLayout(qtw.QGridLayout())

		self.container2 = qtw.QWidget()
		self.container2.setLayout(qtw.QGridLayout())

		#create object containing operation data value
		self.taskList = []

		#create combobox of todo's list
		#self.screen = qtw.QLabel("")
		self.combobox = qtw.QComboBox()
		

		#create button to load selected taskList from combobox
		self.btn_loadTaskList = qtw.QPushButton("load taskList", clicked = self.loadSelectedTaskList)

		#create equal and reset buttons
		btn_val = qtw.QPushButton("validate", clicked = self.onClickValidate)

		# create new task button
		btn_newtask = qtw.QPushButton("new task", clicked = self.onClickCreateTask)

		# add combobox of todo's list to layout
		self.container.layout().addWidget(self.combobox, 0, 0, 1, 3)
		self.container.layout().addWidget(self.btn_loadTaskList, 0, 4, 1, 3)

		# add validation and new task button to layout
		self.container.layout().addWidget(btn_val, 1, 0, 1, 2)
		self.container.layout().addWidget(btn_newtask, 1, 3, 1, 2)

        # add both containers to widget
		self.layout().addWidget(self.container)
		self.layout().addWidget(self.container2)

		MainWindow.loadExistingTaskListsList(self)


	def loadExistingTaskListsList(self):
		#currentpath = os.path.dirname(os.path.realpath(__file__))
		#arr = os.listdir('.')
		#print(glob.glob(currentpath+"/*.txt"))

		arr_txt = [x for x in os.listdir() if x.endswith(".txt")]

		for i in arr_txt :
			self.combobox.addItem(i)


    #onClick button actions
	def loadSelectedTaskList(self):
		with open(self.combobox.currentText()) as json_file :
			self.taskList = json.load(json_file)
	
	#def saveCurrentTaskList(self):


	def onClickCreateTask(self):
		#creation d'un checkbox et d'un input
		self.checkbox = qtw.QCheckBox()
		self.checkbox.stateChanged.connect(self.checkboxStateChanged)
		#self.checkbox.setText(str(len(self.taskList)))

		self.input1 = qtw.QLineEdit()

		#stockage de l'ensemble [checkbox, input] nouvellement créé dans la liste tasklist
		self.taskList.append([self.checkbox, self.input1])

		#on affiche le nouvel état de la liste (liste précédente avec nouvel element)
		MainWindow.display(self)
	
	def onClickValidate(self):
		MainWindow.discardLastTaskList(self)
		for element in self.taskList:
			if element[0].isChecked() :
				self.taskList.remove(element)
		
		#on affiche le nouvel état de la liste (liste précédente avec nouvel element)
		MainWindow.display(self)
	
	def discardLastTaskList(self):
		#on retire le parent de l'ensemble des elements du layout de container2 (a pour effet de detruire l element)
		for i in reversed(range(self.container2.layout().count())) :
			self.container2.layout().itemAt(i).widget().setParent(None)

		
	def display(self):
		MainWindow.discardLastTaskList(self)

		i=self.container2.layout().count()
		for element in self.taskList :
			print("intheloop")
			self.container2.layout().addWidget(element[0], i, 0, 1, 1)
			self.container2.layout().addWidget(element[1], i, 1, 1, 2)
			i=i+1
	
	def checkboxStateChanged(self, state):
		print(str(self.sender().text()) + " : " + str(state))



	


app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
