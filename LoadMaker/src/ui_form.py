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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

import toSelectus


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(452, 421)
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
        self.plainTextEdit = QPlainTextEdit(self.gridFrame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setFrameShape(QFrame.HLine)
        self.plainTextEdit.setFrameShadow(QFrame.Plain)
        self.plainTextEdit.setLineWidth(1)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.gridFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.clicked.connect(self.transform_txt)
        self.verticalLayout.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.gridFrame, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Load Maker", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Transform", None))
    # retranslateUi

    def transform_txt(self):
           raw_txt = self.plainTextEdit.toPlainText()
           self.plainTextEdit.clear()
           result = toSelectus.transform(raw_txt)
           self.plainTextEdit.setPlainText(result)


