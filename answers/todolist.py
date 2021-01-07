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
		
		####create elements
		#create 2 widget containers and grids
		self.container = qtw.QWidget()
		self.container.setLayout(qtw.QGridLayout())

		self.container2 = qtw.QWidget()
		self.container2.setLayout(qtw.QGridLayout())

		#create object containing operation data value
		self.taskList = []
		self.taskListValues = []

		#create combobox of todo's list
			#self.screen = qtw.QLabel("")
		self.combobox = qtw.QComboBox()
		
		#create button to load selected taskList from combobox
		self.btn_loadTaskList = qtw.QPushButton("load taskList", clicked = self.loadSelectedTaskList)

		#create button to save current taskList in selected taskList from combobox
		self.btn_saveTaskList = qtw.QPushButton("save current taskList", clicked = self.saveCurrentTaskList)

		#create validate button to clear all checked tasks
		btn_val = qtw.QPushButton("validate", clicked = self.onClickValidate)

		# create new task button
		btn_newtask = qtw.QPushButton("new task", clicked = self.onClickCreateTask)

		####add elements to containers
		# add combobox of todo's list to layout
		self.container.layout().addWidget(self.combobox, 0, 0, 1, 3)
		self.container.layout().addWidget(self.btn_loadTaskList, 0, 4, 1, 3)
		self.container.layout().addWidget(self.btn_saveTaskList, 1, 4, 1, 3)

		# add validation and new task button to layout
		self.container.layout().addWidget(btn_val, 2, 0, 1, 2)
		self.container.layout().addWidget(btn_newtask, 2, 3, 1, 2)

        # add both containers to widget
		self.layout().addWidget(self.container)
		self.layout().addWidget(self.container2)

		MainWindow.loadExistingTaskListsList(self)


    #onClick button actions

	def onClickCreateTask(self):
		#creation d'un checkbox et d'un input
		self.checkbox = qtw.QCheckBox()
			#self.checkbox.stateChanged.connect(self.checkboxStateChanged)
			#self.checkbox.setText(str(len(self.taskList)))

		self.input1 = qtw.QLineEdit()

		#stockage de l'ensemble [checkbox, input] nouvellement créé dans la liste tasklist
		self.taskList.append([self.checkbox, self.input1])

		#on affiche le nouvel état de la liste (liste précédente avec nouvel element)
		MainWindow.display(self)
	
	def onClickValidate(self):
		#on vide le layout du container2 contenant seulement les tasks
		MainWindow.discardLastTaskList(self)

		#on enleve les taches de la tasklist qui sont cochées par l'utilisateur
		for element in self.taskList:
			if element[0].isChecked() :
				self.taskList.remove(element)
		
		#on affiche le nouvel état de la liste (liste précédente avec nouvel element)
		MainWindow.display(self)
	
	
		
	def display(self):
		MainWindow.discardLastTaskList(self)

		i=self.container2.layout().count()
		for element in self.taskList :
			self.container2.layout().addWidget(element[0], i, 0, 1, 1)
			self.container2.layout().addWidget(element[1], i, 1, 1, 2)
			i=i+1
	
	def discardLastTaskList(self):
		#on retire le parent de l'ensemble des elements du layout de container2 (a pour effet de detruire l element)
		for i in reversed(range(self.container2.layout().count())) :
			self.container2.layout().itemAt(i).widget().setParent(None)



	####save and load data into json file; load jsonfile list of tasklists
	def loadExistingTaskListsList(self):
		arr_txt = [x for x in os.listdir() if x.endswith(".txt")]
		for i in arr_txt :
			self.combobox.addItem(i)
	
	def loadSelectedTaskList(self):
		for element in self.taskListValues :
			self.taskListValues.pop(element)

		with open(self.combobox.currentText()) as json_file :
			self.taskListValues = json.load(json_file)
		
		MainWindow.convertTaskListValues_to_taskList(self)
	
	def convertTaskListValues_to_taskList(self) :
		for element in self.taskListValues :
			self.checkbox = qtw.QCheckBox()
			if element[0]:
				self.checkbox.setChecked(True)
			
			self.input2 = qtw.QLineEdit()
			self.input2.insert(element[1])
			self.taskList.append([self.checkbox, self.input2])
		
		#on affiche le nouvel état de la liste (liste précédente avec nouvel element)
		MainWindow.display(self)
	
	def saveCurrentTaskList(self):
		for element in self.taskListValues :
			self.taskListValues.pop(element)
		for element1 in self.taskList :
			self.taskListValues.append([element1[0].isChecked(), element1[1].text()])
		with open(self.combobox.currentText(), 'w') as outfile:
			del json
			json.dump(self.taskListValues, outfile)

	



app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
