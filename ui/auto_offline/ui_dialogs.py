# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialogs.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_layoutWidget(object):
    def setupUi(self, layoutWidget):
        if not layoutWidget.objectName():
            layoutWidget.setObjectName(u"layoutWidget")
        layoutWidget.resize(1080, 720)
        self.verticalLayoutWidget = QWidget(layoutWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 1081, 121))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.verticalLayoutWidget)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.middleWidget = QWidget(layoutWidget)
        self.middleWidget.setObjectName(u"middleWidget")
        self.middleWidget.setGeometry(QRect(0, 120, 1081, 541))
        self.horizontalLayoutWidget = QWidget(layoutWidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 660, 1081, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 0, 20, 20)
        self.backToMainScreenButton = QPushButton(self.horizontalLayoutWidget)
        self.backToMainScreenButton.setObjectName(u"backToMainScreenButton")

        self.horizontalLayout.addWidget(self.backToMainScreenButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.backButton = QPushButton(self.horizontalLayoutWidget)
        self.backButton.setObjectName(u"backButton")

        self.horizontalLayout.addWidget(self.backButton)

        self.nextButton = QPushButton(self.horizontalLayoutWidget)
        self.nextButton.setObjectName(u"nextButton")

        self.horizontalLayout.addWidget(self.nextButton)


        self.retranslateUi(layoutWidget)

        QMetaObject.connectSlotsByName(layoutWidget)
    # setupUi

    def retranslateUi(self, layoutWidget):
        layoutWidget.setWindowTitle(QCoreApplication.translate("layoutWidget", u"Form", None))
        self.title.setText("")
        self.backToMainScreenButton.setText(QCoreApplication.translate("layoutWidget", u"Ana Men\u00fcye D\u00f6n", None))
        self.backButton.setText(QCoreApplication.translate("layoutWidget", u"Geri", None))
        self.nextButton.setText(QCoreApplication.translate("layoutWidget", u"\u0130leri", None))
    # retranslateUi

