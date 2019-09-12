# from .IUserInterface import IUserInterface
# from framework.common.Utilities import execution_status
# from framework.common.ParameterKeys import ParameterKeys
# from framework.presentation.ResponseExecutionCode import ResponseExecutionCode

# from PyQt5 import QtCore, QtWidgets
# from PyQt5.QtWidgets import QMainWindow, QFileDialog
# from PyQt5.QtCore import QCoreApplication


# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(404, 509)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.IdentifySpecie = QtWidgets.QCheckBox(self.centralwidget)
#         self.IdentifySpecie.setGeometry(QtCore.QRect(30, 50, 111, 41))
#         self.IdentifySpecie.setObjectName("IdentifySpecie")
#         self.DetectMutations = QtWidgets.QCheckBox(self.centralwidget)
#         self.DetectMutations.setGeometry(QtCore.QRect(30, 90, 111, 41))
#         self.DetectMutations.setObjectName("DetectMutations")
#         self.ForwardPrimer = QtWidgets.QLineEdit(self.centralwidget)
#         self.ForwardPrimer.setGeometry(QtCore.QRect(160, 240, 181, 20))
#         self.ForwardPrimer.setObjectName("ForwardPrimer")
#         self.Run = QtWidgets.QPushButton(self.centralwidget)
#         self.Run.setGeometry(QtCore.QRect(210, 430, 131, 23))
#         self.Run.setObjectName("Run")
#         self.Cancel = QtWidgets.QPushButton(self.centralwidget)
#         self.Cancel.setGeometry(QtCore.QRect(30, 430, 131, 23))
#         self.Cancel.setObjectName("Cancel")
#         self.specie_label = QtWidgets.QLabel(self.centralwidget)
#         self.specie_label.setGeometry(QtCore.QRect(90, 140, 47, 21))
#         self.specie_label.setObjectName("specie_label")
#         self.gene_label = QtWidgets.QLabel(self.centralwidget)
#         self.gene_label.setGeometry(QtCore.QRect(90, 190, 47, 16))
#         self.gene_label.setObjectName("gene_label")
#         self.forward_primer_label = QtWidgets.QLabel(self.centralwidget)
#         self.forward_primer_label.setGeometry(QtCore.QRect(56, 240, 81, 20))
#         self.forward_primer_label.setObjectName("forward_primer_label")
#         self.steps_info = QtWidgets.QLabel(self.centralwidget)
#         self.steps_info.setGeometry(QtCore.QRect(30, 20, 151, 21))
#         self.steps_info.setObjectName("steps_info")
#         self.reverse_primer_label = QtWidgets.QLabel(self.centralwidget)
#         self.reverse_primer_label.setGeometry(QtCore.QRect(60, 290, 81, 20))
#         self.reverse_primer_label.setObjectName("reverse_primer_label")
#         self.ReversePrimer = QtWidgets.QLineEdit(self.centralwidget)
#         self.ReversePrimer.setGeometry(QtCore.QRect(160, 290, 181, 20))
#         self.ReversePrimer.setObjectName("ReversePrimer")
#         self.specie_options = QtWidgets.QComboBox(self.centralwidget)
#         self.specie_options.setGeometry(QtCore.QRect(160, 140, 181, 22))
#         self.specie_options.setObjectName("specie_options")
#         self.specie_options.addItems(["", "Candida albicans", "Candida glabrata", "Candida parapsilosis", "Candida tropicalis"])
#         self.gene_options = QtWidgets.QComboBox(self.centralwidget)
#         self.gene_options.setGeometry(QtCore.QRect(160, 190, 181, 22))
#         self.gene_options.setObjectName("gene_options")
#         self.gene_options.addItems(["", "ERG11", "FKS1", "FKS2"])
#         self.folder_identification = QtWidgets.QToolButton(self.centralwidget)
#         self.folder_identification.setGeometry(QtCore.QRect(310, 60, 31, 21))
#         self.folder_identification.setObjectName("folder_identification")
#         self.directory_id = QtWidgets.QLineEdit(self.centralwidget)
#         self.directory_id.setGeometry(QtCore.QRect(160, 60, 131, 20))
#         self.directory_id.setObjectName("directory_id")
#         self.folder_detection = QtWidgets.QToolButton(self.centralwidget)
#         self.folder_detection.setGeometry(QtCore.QRect(310, 100, 31, 21))
#         self.folder_detection.setObjectName("folder_detection")
#         self.directory_detect = QtWidgets.QLineEdit(self.centralwidget)
#         self.directory_detect.setGeometry(QtCore.QRect(160, 100, 131, 20))
#         self.directory_detect.setObjectName("directory_detect")
#         self.status_result_box = QtWidgets.QTextEdit(self.centralwidget)
#         self.status_result_box.setGeometry(QtCore.QRect(160, 350, 181, 51))
#         self.status_result_box.setObjectName("status_result_box")
#         self.status_label = QtWidgets.QLabel(self.centralwidget)
#         self.status_label.setGeometry(QtCore.QRect(60, 360, 71, 31))
#         self.status_label.setObjectName("status_label")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 404, 21))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "Identification and Detection - Candida sp."))
#         self.IdentifySpecie.setText(_translate("MainWindow", "Identify specie"))
#         self.DetectMutations.setText(_translate("MainWindow", "Detect resistance"))
#         self.Run.setText(_translate("MainWindow", "Run"))
#         self.Cancel.setText(_translate("MainWindow", "Cancel"))
#         self.specie_label.setText(_translate("MainWindow", "   Specie"))
#         self.gene_label.setText(_translate("MainWindow", "     Gene"))
#         self.forward_primer_label.setText(_translate("MainWindow", " Forward Primer"))
#         self.steps_info.setText(_translate("MainWindow", "Select the steps to execute"))
#         self.reverse_primer_label.setText(_translate("MainWindow", "Reverse Primer"))
#         self.folder_identification.setText(_translate("MainWindow", "..."))
#         self.folder_detection.setText(_translate("MainWindow", "..."))
#         self.status_label.setText(_translate("MainWindow", "Results status"))


# class GuiView(QMainWindow):

#     def __init__(self, controller):
#         QMainWindow.__init__(self)
#         self.__ui = Ui_MainWindow()
#         self.__ui.setupUi(self)

#         self.__ui.Run.clicked.connect(self.display)
#         self.__ui.Cancel.clicked.connect(self.__close_app)
#         self.__ui.folder_identification.clicked.connect(
#             self.__dialog_box_identification_process
#         )
#         self.__ui.folder_detection.clicked.connect(self.__dialog_box_detection_process)
#         self.__controller = controller

#     def display(self):
#         while True:
#             params = self.__user_options()
#             self.show_specie_identification(params)
#             self.show_antifungal_resistance_detection(params)


#     def show_antifungal_resistance_detection(self, params):
#         result = self.__controller.execute_specie_identification(params)
#         if result:
#             status = execution_status(result, ResponseExecutionCode.STATUS)
#             self.__ui.status_result_box.append(status)

#     def show_specie_identification(self, params):

#         result = self.__controller.execute_antifungal_resistance_detection(params)
#         if result:
#             status = execution_status(result, ResponseExecutionCode.STATUS)
#             self.__ui.status_result_box.append(status)

#     def __close_app(self):
#         QCoreApplication.instance().quit()

#     def __dialog_box_identification_process(self):
#         return self.__ui.directory_id.setText(QFileDialog.getExistingDirectory())

#     def __dialog_box_detection_process(self):
#         return self.__ui.directory_detect.setText(QFileDialog.getOpenFileName()[0])

#     def __user_options(self):
#         params = {}

#         params[ParameterKeys.DETECTION_KEY] = self.__ui.DetectMutations.isChecked()
#         params[ParameterKeys.IDENTIFICATION_KEY] = self.__ui.IdentifySpecie.isChecked()
#         params[ParameterKeys.FORWARD_PRIMER] = self.__ui.ForwardPrimer.text()
#         params[ParameterKeys.REVERSE_PRIMER] = self.__ui.ReversePrimer.text()
#         params[ParameterKeys.SPECIE_NAME] = self.__ui.specie_options.currentText()
#         params[ParameterKeys.GENE_NAME] = self.__ui.gene_options.currentText()
#         params[ParameterKeys.FILEPATH_IDENTIFICATION] = self.__ui.directory_id.text()
#         params[ParameterKeys.FILEPATH_DETECTION] = self.__ui.directory_detect.text()

#         return params
