from .IUserInterface import IUserInterface
from framework.common.Utilities import execution_status
from framework.common.ParameterKeys import ParameterKeys
from framework.presentation.ResponseExecutionCode import ResponseExecutionCode
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QErrorMessage
from PyQt5.QtCore import QCoreApplication


qt_creator_file = "framework/presentation/userinterface.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)


class GuiView(IUserInterface, QMainWindow, Ui_MainWindow):
    
    def __init__(self, controller):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Run.clicked.connect(self.display)
        self.Cancel.clicked.connect(self.__close_app)
        self.folder_identification.clicked.connect(self.__dialog_box_identification_process)
        self.folder_detection.clicked.connect(self.__dialog_box_detection_process)
        self.__controller = controller

    def display(self):
        while True:
            params = self.__user_options()
            result_identification, result_resistance = self.__controller.execute(params)
            self.status_result_box.append(execution_status(result_identification, ResponseExecutionCode.STATUS))
            self.status_result_box.append(execution_status(result_resistance, ResponseExecutionCode.STATUS))

    def __close_app(self):
        QCoreApplication.instance().quit()

    def __dialog_box_identification_process(self):
        return self.directory_id.setText(QFileDialog.getExistingDirectory())

    def __dialog_box_detection_process(self):
        return self.directory_detect.setText(QFileDialog.getOpenFileName()[0])

    def __user_options(self):
        params = {}

        params[ParameterKeys.DETECTION_KEY] = self.DetectMutations.isChecked()
        params[ParameterKeys.IDENTIFICATION_KEY] = self.IdentifySpecie.isChecked()
        params[ParameterKeys.FORWARD_PRIMER] = self.ForwardPrimer.text()
        params[ParameterKeys.REVERSE_PRIMER] = self.ReversePrimer.text()
        params[ParameterKeys.SPECIE_NAME] = self.specie_options.currentText()
        params[ParameterKeys.GENE_NAME] = self.gene_options.currentText()
        params[ParameterKeys.FILEPATH_IDENTIFICATION] = self.directory_id.text()
        params[ParameterKeys.FILEPATH_DETECTION] = self.directory_detect.text()

        return params