# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

import toSelectus

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(433, 432)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"../style/cnu.ico", QSize(), QIcon.Normal, QIcon.Off)
        Widget.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(Widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridFrame = QFrame(Widget)
        self.gridFrame.setObjectName(u"gridFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.gridFrame.sizePolicy().hasHeightForWidth())
        self.gridFrame.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.OMNI = QRadioButton(self.gridFrame)
        self.OMNI.setObjectName(u"OMNI")

        self.horizontalLayout.addWidget(self.OMNI)

        self.Other = QRadioButton(self.gridFrame)
        self.Other.setObjectName(u"Other")

        self.horizontalLayout.addWidget(self.Other)

        self.Clear = QPushButton(self.gridFrame)
        self.Clear.setObjectName(u"Clear")

        self.horizontalLayout.addWidget(self.Clear)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.LoadText = QPlainTextEdit(self.gridFrame)
        self.LoadText.setObjectName(u"LoadText")
        self.LoadText.setFrameShape(QFrame.HLine)
        self.LoadText.setFrameShadow(QFrame.Plain)
        self.LoadText.setLineWidth(1)

        self.verticalLayout.addWidget(self.LoadText)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Copy = QPushButton(self.gridFrame)
        self.Copy.setObjectName(u"Copy")

        self.horizontalLayout_2.addWidget(self.Copy)

        self.Paste = QPushButton(self.gridFrame)
        self.Paste.setObjectName(u"Paste")

        self.horizontalLayout_2.addWidget(self.Paste)

        self.Transform = QPushButton(self.gridFrame)
        self.Transform.setObjectName(u"Transform")
        self.Transform.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.Transform)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.gridFrame, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        self.Transform.clicked.connect(self.transform)
        self.Copy.clicked.connect(self.copy)
        self.Paste.clicked.connect(self.paste)
        self.Clear.clicked.connect(self.clear)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Load Maker", None))
        self.OMNI.setText(QCoreApplication.translate("Widget", u"OMNI", None))
        self.Other.setText(QCoreApplication.translate("Widget", u"Other", None))
        self.Clear.setText(QCoreApplication.translate("Widget", u"Clear", None))
        self.Copy.setText(QCoreApplication.translate("Widget", u"Copy", None))
        self.Paste.setText(QCoreApplication.translate("Widget", u"Paste", None))
        self.Transform.setText(QCoreApplication.translate("Widget", u"Transform", None))
    # retranslateUi

    def transform(self):
           raw_txt = self.LoadText.toPlainText()
           self.LoadText.clear()
           result = toSelectus.transform(raw_txt)
           self.LoadText.setPlainText(result)


    def copy(self):
        self.LoadText.selectAll()
        self.LoadText.copy()

    def paste(self):
        self.LoadText.clear()
        self.LoadText.paste()
        self.transform()

    def clear(self):
        self.LoadText.clear()


