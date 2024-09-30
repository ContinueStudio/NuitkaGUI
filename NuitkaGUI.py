import sys

import loguru
from PySide6.QtNetwork import QLocalSocket, QLocalServer
from PySide6.QtWidgets import QApplication, QMessageBox

from src.config import cfg
from src.presenter.main_presenter import MainPresenter
from src.presenter.welcome_presenter import WelcomePresenter


def is_already_running():
    socket = QLocalSocket()
    socket.connectToServer("UniqueApplicationIdentifier")
    running = socket.waitForConnected(500)
    socket.close()
    return running


@loguru.logger.catch(reraise=True)
def main():
    if is_already_running():
        loguru.logger.warning("Application is already running.")
        sys.exit(0)

    server = QLocalServer()
    server.listen("UniqueApplicationIdentifier")
    app = QApplication([])
    is_first_run: bool = cfg.get(cfg.is_first_run)
    if is_first_run:
        welcome_presenter = WelcomePresenter()
        welcome_presenter.view.show()
    else:
        main_presenter = MainPresenter()
        main_presenter.view.show()
    app.exec()


if __name__ == "__main__":
    main()
