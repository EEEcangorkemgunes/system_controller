# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auto_offline_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1080, 720)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1080, 720))
        self.horizontalLayoutWidget = QWidget(self.layoutWidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 640, 1081, 80))
        self.ButtonsLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.ButtonsLayout.setSpacing(10)
        self.ButtonsLayout.setObjectName(u"ButtonsLayout")
        self.ButtonsLayout.setContentsMargins(0, 0, 0, 0)
        self.backToMainScreenButton = QPushButton(self.horizontalLayoutWidget)
        self.backToMainScreenButton.setObjectName(u"backToMainScreenButton")

        self.ButtonsLayout.addWidget(self.backToMainScreenButton)

        self.buttonSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.ButtonsLayout.addItem(self.buttonSpacer)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.ButtonsLayout.addWidget(self.pushButton_2)

        self.nextButton = QPushButton(self.horizontalLayoutWidget)
        self.nextButton.setObjectName(u"nextButton")

        self.ButtonsLayout.addWidget(self.nextButton)

        self.verticalLayoutWidget = QWidget(self.layoutWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 1081, 641))
        self.topLayot = QVBoxLayout(self.verticalLayoutWidget)
        self.topLayot.setObjectName(u"topLayot")
        self.topLayot.setContentsMargins(0, 0, 0, 0)
        self.titleLayout = QHBoxLayout()
        self.titleLayout.setObjectName(u"titleLayout")
        self.titleLayout.setContentsMargins(-1, 30, -1, -1)
        self.titleLabel = QLabel(self.verticalLayoutWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.titleLabel.setWordWrap(True)

        self.titleLayout.addWidget(self.titleLabel)


        self.topLayot.addLayout(self.titleLayout)

        self.mainboardLayout = QHBoxLayout()
        self.mainboardLayout.setObjectName(u"mainboardLayout")
        self.mainboardComboBox = QComboBox(self.verticalLayoutWidget)
        self.mainboardComboBox.addItem("")
        self.mainboardComboBox.addItem("")
        self.mainboardComboBox.addItem("")
        self.mainboardComboBox.addItem("")
        self.mainboardComboBox.addItem("")
        self.mainboardComboBox.addItem("")
        self.mainboardComboBox.setObjectName(u"mainboardComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainboardComboBox.sizePolicy().hasHeightForWidth())
        self.mainboardComboBox.setSizePolicy(sizePolicy)
        self.mainboardComboBox.setMinimumSize(QSize(90, 40))

        self.mainboardLayout.addWidget(self.mainboardComboBox)


        self.topLayot.addLayout(self.mainboardLayout)

        self.swNameDescriptionLayout_2 = QVBoxLayout()
        self.swNameDescriptionLayout_2.setObjectName(u"swNameDescriptionLayout_2")
        self.swNameDescriptionLayout_2.setContentsMargins(-1, -1, 10, 20)
        self.swNameDescriptionLayout = QHBoxLayout()
        self.swNameDescriptionLayout.setObjectName(u"swNameDescriptionLayout")
        self.swNameDescriptionLabel = QLabel(self.verticalLayoutWidget)
        self.swNameDescriptionLabel.setObjectName(u"swNameDescriptionLabel")
        self.swNameDescriptionLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.swNameDescriptionLayout.addWidget(self.swNameDescriptionLabel)


        self.swNameDescriptionLayout_2.addLayout(self.swNameDescriptionLayout)

        self.swNameLayout = QHBoxLayout()
        self.swNameLayout.setObjectName(u"swNameLayout")
        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.swNameLayout.addWidget(self.lineEdit)

        self.oldSwNameComboBox = QComboBox(self.verticalLayoutWidget)
        self.oldSwNameComboBox.setObjectName(u"oldSwNameComboBox")

        self.swNameLayout.addWidget(self.oldSwNameComboBox)

        self.swNameLayout.setStretch(0, 1)
        self.swNameLayout.setStretch(1, 1)

        self.swNameDescriptionLayout_2.addLayout(self.swNameLayout)


        self.topLayot.addLayout(self.swNameDescriptionLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.backToMainScreenButton.setText(QCoreApplication.translate("Dialog", u"Ana Men\u00fcye D\u00f6n", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Geri", None))
        self.nextButton.setText(QCoreApplication.translate("Dialog", u"\u0130leri", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"L\u00fctfen Offline Y\u00fcklemek \u0130stedi\u011fini \u015easiyi Se\u00e7in", None))
        self.mainboardComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"GB", None))
        self.mainboardComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"GY", None))
        self.mainboardComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"AN", None))
        self.mainboardComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"GO", None))
        self.mainboardComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"GX", None))
        self.mainboardComboBox.setItemText(5, QCoreApplication.translate("Dialog", u"GL", None))

        self.swNameDescriptionLabel.setText(QCoreApplication.translate("Dialog", u"L\u00fctfen USB i\u00e7erisindeki offline yaz\u0131l\u0131m\u0131n ismini girin", None))
        self.lineEdit.setText(QCoreApplication.translate("Dialog", u"fusion_writer.bin", None))
    # retranslateUi

