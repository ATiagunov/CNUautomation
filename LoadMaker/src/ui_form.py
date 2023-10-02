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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
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
        self.textEdit = QTextEdit(self.gridFrame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFrameShape(QFrame.HLine)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setLineWidth(1)

        self.verticalLayout.addWidget(self.textEdit)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.gridFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.gridFrame, 0, 0, 1, 1)


        self.retranslateUi(Widget)
        self.pushButton.clicked.connect(self.transform_txt)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.textEdit.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Type info</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Transform", None))
    # retranslateUi

    def transform_txt(self):
        raw_txt = self.textEdit.toPlainText()
        result = toSelectus.transform(raw_txt)
        self.textEdit.setText(result)








