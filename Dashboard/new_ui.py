# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dashboard/gui_stripped.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1297, 847)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.navbar = QtWidgets.QWidget(self.centralwidget)
        self.navbar.setGeometry(QtCore.QRect(0, 0, 1301, 91))
        self.navbar.setObjectName("navbar")
        self.navbar_background = QtWidgets.QLabel(self.navbar)
        self.navbar_background.setGeometry(QtCore.QRect(-10, -10, 1321, 101))
        self.navbar_background.setStyleSheet("background: lightgrey;\n"
"border: 1px solid grey;")
        self.navbar_background.setText("")
        self.navbar_background.setObjectName("navbar_background")
        self.navbar_profile = QtWidgets.QLabel(self.navbar)
        self.navbar_profile.setGeometry(QtCore.QRect(1230, 20, 50, 50))
        self.navbar_profile.setStyleSheet("background: grey;\n"
"border-radius: 25px;\n"
"border: 1px solid black;")
        self.navbar_profile.setText("")
        self.navbar_profile.setObjectName("navbar_profile")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.navbar)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 791, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nav_env = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.nav_env.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 10px;\n"
"text-align: center;\n"
"font-weight: bold; height: auto;")
        self.nav_env.setObjectName("nav_env")
        self.horizontalLayout.addWidget(self.nav_env)
        self.nav_model_list = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.nav_model_list.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 10px;\n"
"text-align: center;\n"
"font-weight: bold; height: auto;")
        self.nav_model_list.setObjectName("nav_model_list")
        self.horizontalLayout.addWidget(self.nav_model_list)
        self.nav_model_create = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.nav_model_create.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 10px;\n"
"text-align: center;\n"
"font-weight: bold; height: auto;")
        self.nav_model_create.setObjectName("nav_model_create")
        self.horizontalLayout.addWidget(self.nav_model_create)
        self.loading = QtWidgets.QWidget(self.centralwidget)
        self.loading.setEnabled(False)
        self.loading.setGeometry(QtCore.QRect(0, 0, 1311, 851))
        self.loading.setObjectName("loading")
        self.logo_cont = QtWidgets.QLabel(self.loading)
        self.logo_cont.setGeometry(QtCore.QRect(0, -10, 1311, 861))
        self.logo_cont.setStyleSheet("background: white")
        self.logo_cont.setText("")
        self.logo_cont.setObjectName("logo_cont")
        self.content_window = QtWidgets.QWidget(self.centralwidget)
        self.content_window.setGeometry(QtCore.QRect(-1, 90, 1301, 761))
        self.content_window.setObjectName("content_window")
        self.content_background = QtWidgets.QLabel(self.content_window)
        self.content_background.setGeometry(QtCore.QRect(-6, 5, 1311, 751))
        self.content_background.setStyleSheet("background: white;")
        self.content_background.setText("")
        self.content_background.setObjectName("content_background")
        self.model_creation_window = QtWidgets.QWidget(self.content_window)
        self.model_creation_window.setGeometry(QtCore.QRect(-1, 0, 1301, 751))
        self.model_creation_window.setStyleSheet("background: white;")
        self.model_creation_window.setObjectName("model_creation_window")
        self.steps_window = QtWidgets.QWidget(self.model_creation_window)
        self.steps_window.setGeometry(QtCore.QRect(20, 20, 301, 721))
        self.steps_window.setStyleSheet("background: whitesmoke; border-radius: 20px; border: 1px solid lightgrey;")
        self.steps_window.setObjectName("steps_window")
        self.pushButton_2 = QtWidgets.QPushButton(self.steps_window)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 30, 259, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.steps_window)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 90, 259, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.steps_window)
        self.pushButton.setGeometry(QtCore.QRect(20, 150, 259, 41))
        self.pushButton.setObjectName("pushButton")
        self.steps_desc_window = QtWidgets.QWidget(self.model_creation_window)
        self.steps_desc_window.setGeometry(QtCore.QRect(340, 20, 941, 721))
        self.steps_desc_window.setStyleSheet("background: whitesmoke; border-radius: 20px; border: 1px solid lightgrey;")
        self.steps_desc_window.setObjectName("steps_desc_window")
        self.steps_1 = QtWidgets.QWidget(self.steps_desc_window)
        self.steps_1.setGeometry(QtCore.QRect(20, 20, 901, 681))
        self.steps_1.setStyleSheet("border: none;")
        self.steps_1.setObjectName("steps_1")
        self.step1_model_name = QtWidgets.QLabel(self.steps_1)
        self.step1_model_name.setGeometry(QtCore.QRect(32, 40, 200, 31))
        self.step1_model_name.setObjectName("step1_model_name")
        self.step1_model_name_enter = QtWidgets.QLineEdit(self.steps_1)
        self.step1_model_name_enter.setGeometry(QtCore.QRect(30, 80, 551, 31))
        self.step1_model_name_enter.setStyleSheet("border: 1px grey solid;\n"
"background: white;")
        self.step1_model_name_enter.setObjectName("step1_model_name_enter")
        self.step1_model_desc = QtWidgets.QLabel(self.steps_1)
        self.step1_model_desc.setGeometry(QtCore.QRect(32, 150, 200, 31))
        self.step1_model_desc.setObjectName("step1_model_desc")
        self.step1_model_desc_enter = QtWidgets.QTextEdit(self.steps_1)
        self.step1_model_desc_enter.setGeometry(QtCore.QRect(30, 190, 551, 151))
        self.step1_model_desc_enter.setStyleSheet("background: white; border-radius: 0px;")
        self.step1_model_desc_enter.setObjectName("step1_model_desc_enter")
        self.scrollArea = QtWidgets.QScrollArea(self.steps_1)
        self.scrollArea.setGeometry(QtCore.QRect(30, 430, 841, 211))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 841, 211))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.step1_env_choose = QtWidgets.QLabel(self.steps_1)
        self.step1_env_choose.setGeometry(QtCore.QRect(31, 381, 200, 30))
        self.step1_env_choose.setObjectName("step1_env_choose")
        self.steps_2 = QtWidgets.QWidget(self.steps_desc_window)
        self.steps_2.setGeometry(QtCore.QRect(19, 19, 901, 681))
        self.steps_2.setStyleSheet("border: none;")
        self.steps_2.setObjectName("steps_2")
        self.step2_head = QtWidgets.QLabel(self.steps_2)
        self.step2_head.setGeometry(QtCore.QRect(33, 41, 200, 31))
        self.step2_head.setObjectName("step2_head")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.steps_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 90, 451, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.hyperparams_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.hyperparams_layout.setContentsMargins(0, 0, 0, 0)
        self.hyperparams_layout.setObjectName("hyperparams_layout")
        self.hyperparam_1 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.hyperparam_1.setObjectName("hyperparam_1")
        self.hyperparam_label_1 = QtWidgets.QLabel(self.hyperparam_1)
        self.hyperparam_label_1.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.hyperparam_label_1.setObjectName("hyperparam_label_1")
        self.hyperparam_value_1 = QtWidgets.QLineEdit(self.hyperparam_1)
        self.hyperparam_value_1.setGeometry(QtCore.QRect(10, 40, 241, 31))
        self.hyperparam_value_1.setObjectName("hyperparam_value_1")
        self.hyperparam_info_1 = QtWidgets.QPushButton(self.hyperparam_1)
        self.hyperparam_info_1.setGeometry(QtCore.QRect(410, 10, 31, 28))
        self.hyperparam_info_1.setObjectName("hyperparam_info_1")
        self.hyperparams_layout.addWidget(self.hyperparam_1)
        self.hyperparam_2 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.hyperparam_2.setObjectName("hyperparam_2")
        self.hyperparam_label_2 = QtWidgets.QLabel(self.hyperparam_2)
        self.hyperparam_label_2.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.hyperparam_label_2.setObjectName("hyperparam_label_2")
        self.hyperparam_value_2 = QtWidgets.QLineEdit(self.hyperparam_2)
        self.hyperparam_value_2.setGeometry(QtCore.QRect(10, 40, 241, 31))
        self.hyperparam_value_2.setObjectName("hyperparam_value_2")
        self.hyperparam_info_2 = QtWidgets.QPushButton(self.hyperparam_2)
        self.hyperparam_info_2.setGeometry(QtCore.QRect(410, 10, 31, 28))
        self.hyperparam_info_2.setObjectName("hyperparam_info_2")
        self.hyperparams_layout.addWidget(self.hyperparam_2)
        self.hyperparam_3 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.hyperparam_3.setObjectName("hyperparam_3")
        self.hyperparam_label_3 = QtWidgets.QLabel(self.hyperparam_3)
        self.hyperparam_label_3.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.hyperparam_label_3.setObjectName("hyperparam_label_3")
        self.hyperparam_value_3 = QtWidgets.QLineEdit(self.hyperparam_3)
        self.hyperparam_value_3.setGeometry(QtCore.QRect(10, 40, 241, 31))
        self.hyperparam_value_3.setObjectName("hyperparam_value_3")
        self.hyperparam_info_3 = QtWidgets.QPushButton(self.hyperparam_3)
        self.hyperparam_info_3.setGeometry(QtCore.QRect(410, 10, 31, 28))
        self.hyperparam_info_3.setObjectName("hyperparam_info_3")
        self.hyperparams_layout.addWidget(self.hyperparam_3)
        self.hyperparam_4 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.hyperparam_4.setObjectName("hyperparam_4")
        self.hyperparam_label_4 = QtWidgets.QLabel(self.hyperparam_4)
        self.hyperparam_label_4.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.hyperparam_label_4.setObjectName("hyperparam_label_4")
        self.hyperparam_value_4 = QtWidgets.QLineEdit(self.hyperparam_4)
        self.hyperparam_value_4.setGeometry(QtCore.QRect(10, 40, 241, 31))
        self.hyperparam_value_4.setObjectName("hyperparam_value_4")
        self.hyperparam_info_4 = QtWidgets.QPushButton(self.hyperparam_4)
        self.hyperparam_info_4.setGeometry(QtCore.QRect(410, 10, 31, 28))
        self.hyperparam_info_4.setObjectName("hyperparam_info_4")
        self.hyperparams_layout.addWidget(self.hyperparam_4)
        self.steps_3 = QtWidgets.QWidget(self.steps_desc_window)
        self.steps_3.setGeometry(QtCore.QRect(19, 19, 901, 681))
        self.steps_3.setStyleSheet("border: none;")
        self.steps_3.setObjectName("steps_3")
        self.step3_model_name = QtWidgets.QLabel(self.steps_3)
        self.step3_model_name.setGeometry(QtCore.QRect(33, 41, 200, 31))
        self.step3_model_name.setObjectName("step3_model_name")
        self.step3_code_editor = QtWidgets.QTextEdit(self.steps_3)
        self.step3_code_editor.setGeometry(QtCore.QRect(30, 84, 791, 441))
        self.step3_code_editor.setStyleSheet("border: 1px solid grey;\n"
"border-radius: 10px;\n"
"background: white;")
        self.step3_code_editor.setObjectName("step3_code_editor")
        self.step_3_training = QtWidgets.QPushButton(self.steps_3)
        self.step_3_training.setGeometry(QtCore.QRect(682, 550, 141, 31))
        self.step_3_training.setStyleSheet("border: 1px solid black;")
        self.step_3_training.setObjectName("step_3_training")
        self.step_3_validate = QtWidgets.QPushButton(self.steps_3)
        self.step_3_validate.setGeometry(QtCore.QRect(532, 550, 131, 31))
        self.step_3_validate.setStyleSheet("border: 1px solid black;")
        self.step_3_validate.setObjectName("step_3_validate")
        self.steps_3.raise_()
        self.steps_1.raise_()
        self.steps_2.raise_()
        self.steps_desc_window.raise_()
        self.steps_window.raise_()
        self.model_training_window = QtWidgets.QWidget(self.content_window)
        self.model_training_window.setGeometry(QtCore.QRect(-11, -1, 1311, 761))
        self.model_training_window.setObjectName("model_training_window")
        self.mode_trianing_Cont = QtWidgets.QWidget(self.model_training_window)
        self.mode_trianing_Cont.setGeometry(QtCore.QRect(30, 20, 1261, 721))
        self.mode_trianing_Cont.setStyleSheet("background: whitesmoke; border-radius: 30px")
        self.mode_trianing_Cont.setObjectName("mode_trianing_Cont")
        self.pygame = QtWidgets.QLabel(self.mode_trianing_Cont)
        self.pygame.setGeometry(QtCore.QRect(10, 10, 611, 441))
        self.pygame.setStyleSheet("background: lightgrey;")
        self.pygame.setText("")
        self.pygame.setObjectName("pygame")
        self.matplotlib = QtWidgets.QLabel(self.mode_trianing_Cont)
        self.matplotlib.setGeometry(QtCore.QRect(639, 10, 611, 441))
        self.matplotlib.setStyleSheet("background: lightgrey;")
        self.matplotlib.setText("")
        self.matplotlib.setObjectName("matplotlib")
        self.stop_training_button = QtWidgets.QPushButton(self.mode_trianing_Cont)
        self.stop_training_button.setGeometry(QtCore.QRect(526, 480, 200, 60))
        self.stop_training_button.setStyleSheet("background: lightgrey; cursor: pointer;")
        self.stop_training_button.setObjectName("stop_training_button")
        self.model_training_window.raise_()
        self.content_background.raise_()
        self.model_creation_window.raise_()
        self.loading.raise_()
        self.navbar.raise_()
        self.content_window.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.steps_1.raise)
        self.pushButton_3.clicked.connect(self.steps_2.raise)
        self.pushButton.clicked.connect(self.steps_3.raise)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nav_env.setText(_translate("MainWindow", "Environments"))
        self.nav_model_list.setText(_translate("MainWindow", "Your Models"))
        self.nav_model_create.setText(_translate("MainWindow", "Create Models"))
        self.pushButton_2.setText(_translate("MainWindow", "Step1"))
        self.pushButton_3.setText(_translate("MainWindow", "Step2"))
        self.pushButton.setText(_translate("MainWindow", "Step3"))
        self.step1_model_name.setText(_translate("MainWindow", "Enter Model Name"))
        self.step1_model_desc.setText(_translate("MainWindow", "Enter Model Description"))
        self.step1_env_choose.setText(_translate("MainWindow", "Select a track"))
        self.step2_head.setText(_translate("MainWindow", "Hyperparameters"))
        self.hyperparam_label_1.setText(_translate("MainWindow", "Learning rate (LR)"))
        self.hyperparam_info_1.setText(_translate("MainWindow", "i"))
        self.hyperparam_label_2.setText(_translate("MainWindow", "Hidden Layer Size"))
        self.hyperparam_info_2.setText(_translate("MainWindow", "i"))
        self.hyperparam_label_3.setText(_translate("MainWindow", "epsilon"))
        self.hyperparam_info_3.setText(_translate("MainWindow", "i"))
        self.hyperparam_label_4.setText(_translate("MainWindow", "gamma"))
        self.hyperparam_info_4.setText(_translate("MainWindow", "i"))
        self.step3_model_name.setText(_translate("MainWindow", "Customize Reward Function"))
        self.step_3_training.setText(_translate("MainWindow", "Begin Training"))
        self.step_3_validate.setText(_translate("MainWindow", "Validate"))
        self.stop_training_button.setText(_translate("MainWindow", "STOP TRAINING"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
