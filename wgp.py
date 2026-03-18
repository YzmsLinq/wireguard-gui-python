from os import _exit, geteuid
from sys import argv

from PyQt6.QtCore import QTranslator
from PyQt6 import QtWidgets

from views.main import Ui_MainView

if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    app.setApplicationName("wgp")

    #Load the corresponding language support file
    translatorsys = QTranslator(app)
    translator = QTranslator(app)
    translatorsys.load("translations/qt_zh_CN.qm")
    translator.load("translations/wgp_zh_CN.qm")
    app.installTranslator(translatorsys)
    app.installTranslator(translator)

    if geteuid() != 0:
        err = QtWidgets.QApplication.translate("wgp", "Error")
        msg = QtWidgets.QApplication.translate("wgp", "You need root privileges")
        return_code = QtWidgets.QMessageBox(
            QtWidgets.QMessageBox.Icon.Critical, err, msg
        ).exec()

        _exit(return_code)
    else:
        ui = Ui_MainView()
        ui.show()
        return_code = app.exec()

        _exit(return_code)
