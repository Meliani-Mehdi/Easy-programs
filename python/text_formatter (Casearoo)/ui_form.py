# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_text_ft_main(object):
    def setupUi(self, text_ft_main):
        if not text_ft_main.objectName():
            text_ft_main.setObjectName(u"text_ft_main")
        text_ft_main.resize(800, 600)
        text_ft_main.setMinimumSize(QSize(800, 600))
        text_ft_main.setStyleSheet(u"/* Qt Dark Theme Style Sheet */\n"
"\n"
"QWidget {\n"
"    background-color: #2b2b2b;\n"
"    color: #ffffff;\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"}\n"
"\n"
"QFrame {\n"
"    background-color: #3a3a3a;\n"
"    border: 1px solid #555;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #3a3a3a;\n"
"    border: 1px solid #555;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #505050;\n"
"    border: 1px solid #777;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #666;\n"
"    border: 1px solid #888;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #3a3a3a;\n"
"    border: 1px solid #555;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #777;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    back"
                        "ground-color: #3a3a3a;\n"
"    border: 1px solid #555;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #777;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #3a3a3a;\n"
"    border: 1px solid #555;\n"
"    selection-background-color: #505050;\n"
"    color: white;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2b2b2b;\n"
"    width: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #505050;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #666;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(text_ft_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(text_ft_main)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(16, 16, 16, 16)
        self.text_holder = QFrame(self.widget)
        self.text_holder.setObjectName(u"text_holder")
        self.text_holder.setStyleSheet(u"")
        self.text_holder.setFrameShape(QFrame.StyledPanel)
        self.text_holder.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.text_holder)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.main_text = QTextEdit(self.text_holder)
        self.main_text.setObjectName(u"main_text")

        self.verticalLayout_4.addWidget(self.main_text)


        self.verticalLayout_2.addWidget(self.text_holder)

        self.horizontalWidget_4 = QWidget(self.widget)
        self.horizontalWidget_4.setObjectName(u"horizontalWidget_4")
        self.horizontalWidget_4.setMinimumSize(QSize(0, 210))
        self.horizontalWidget_4.setMaximumSize(QSize(16777215, 210))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.formatter_holder = QFrame(self.horizontalWidget_4)
        self.formatter_holder.setObjectName(u"formatter_holder")
        self.formatter_holder.setMinimumSize(QSize(762, 200))
        self.formatter_holder.setMaximumSize(QSize(16777215, 200))
        self.formatter_holder.setSizeIncrement(QSize(0, 0))
        self.formatter_holder.setStyleSheet(u"")
        self.formatter_holder.setFrameShape(QFrame.StyledPanel)
        self.formatter_holder.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.formatter_holder)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sentenceCase = QPushButton(self.formatter_holder)
        self.sentenceCase.setObjectName(u"sentenceCase")
        self.sentenceCase.setMinimumSize(QSize(200, 40))
        self.sentenceCase.setMaximumSize(QSize(200, 40))

        self.horizontalLayout.addWidget(self.sentenceCase)

        self.lowerCase = QPushButton(self.formatter_holder)
        self.lowerCase.setObjectName(u"lowerCase")
        self.lowerCase.setMinimumSize(QSize(200, 40))
        self.lowerCase.setMaximumSize(QSize(200, 40))

        self.horizontalLayout.addWidget(self.lowerCase)

        self.upperCase = QPushButton(self.formatter_holder)
        self.upperCase.setObjectName(u"upperCase")
        self.upperCase.setMinimumSize(QSize(200, 40))
        self.upperCase.setMaximumSize(QSize(200, 40))

        self.horizontalLayout.addWidget(self.upperCase)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.capitalizedCase = QPushButton(self.formatter_holder)
        self.capitalizedCase.setObjectName(u"capitalizedCase")
        self.capitalizedCase.setMinimumSize(QSize(200, 40))
        self.capitalizedCase.setMaximumSize(QSize(200, 40))

        self.horizontalLayout_2.addWidget(self.capitalizedCase)

        self.altCase = QPushButton(self.formatter_holder)
        self.altCase.setObjectName(u"altCase")
        self.altCase.setMinimumSize(QSize(200, 40))
        self.altCase.setMaximumSize(QSize(200, 40))

        self.horizontalLayout_2.addWidget(self.altCase)

        self.titleCase = QPushButton(self.formatter_holder)
        self.titleCase.setObjectName(u"titleCase")
        self.titleCase.setMinimumSize(QSize(200, 40))
        self.titleCase.setMaximumSize(QSize(200, 40))

        self.horizontalLayout_2.addWidget(self.titleCase)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.inverseCase = QPushButton(self.formatter_holder)
        self.inverseCase.setObjectName(u"inverseCase")
        self.inverseCase.setMinimumSize(QSize(200, 40))
        self.inverseCase.setMaximumSize(QSize(200, 40))

        self.horizontalLayout_3.addWidget(self.inverseCase)

        self.reverseCase = QPushButton(self.formatter_holder)
        self.reverseCase.setObjectName(u"reverseCase")
        self.reverseCase.setMinimumSize(QSize(200, 40))
        self.reverseCase.setMaximumSize(QSize(200, 40))

        self.horizontalLayout_3.addWidget(self.reverseCase)

        self.downloadBtn = QPushButton(self.formatter_holder)
        self.downloadBtn.setObjectName(u"downloadBtn")
        self.downloadBtn.setMinimumSize(QSize(200, 40))
        self.downloadBtn.setMaximumSize(QSize(200, 40))

        self.horizontalLayout_3.addWidget(self.downloadBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addWidget(self.formatter_holder)

        self.horizontalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.horizontalWidget_4)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(text_ft_main)

        QMetaObject.connectSlotsByName(text_ft_main)
    # setupUi

    def retranslateUi(self, text_ft_main):
        text_ft_main.setWindowTitle(QCoreApplication.translate("text_ft_main", u"text_ft_main", None))
        self.sentenceCase.setText(QCoreApplication.translate("text_ft_main", u"Sentence case", None))
        self.lowerCase.setText(QCoreApplication.translate("text_ft_main", u"lower case", None))
        self.upperCase.setText(QCoreApplication.translate("text_ft_main", u"UPPER CASE", None))
        self.capitalizedCase.setText(QCoreApplication.translate("text_ft_main", u"Capitalized Case", None))
        self.altCase.setText(QCoreApplication.translate("text_ft_main", u"aLtErNaTiNg cAsE", None))
        self.titleCase.setText(QCoreApplication.translate("text_ft_main", u"Title Case", None))
        self.inverseCase.setText(QCoreApplication.translate("text_ft_main", u"InVeRsE CaSe", None))
        self.reverseCase.setText(QCoreApplication.translate("text_ft_main", u"Reverse Case", None))
        self.downloadBtn.setText(QCoreApplication.translate("text_ft_main", u"Download", None))
    # retranslateUi

