from date_time_retrieving import input_age_reformulation
import os, sys, subprocess, time

failed = False
def switch_to_console() :
    switch_to_cli = input("Do you want to switch to the CLI interface (yes(y)/no(n))")
    if (switch_to_cli.lower() in["yes", "y"]  ) :
        print("Falling back to console mode ...")
        import no_gui_run
        sys.exit(0)
    else :  
        sys.exit(1)

def init_gui_modules() :
        global QtWidgets, Qt, QtGui
        import PySide6.QtWidgets as QtWidgets 
        from PySide6.QtCore import Qt
        import PySide6.QtGui as QtGui## this is where we will use Qfont
def call_flip_flop_restarter():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    flip_and_flop_path = os.path.join(current_directory, "flip_and_flop.py")
    print("attempting to restart...")
    time.sleep(5)
    subprocess.Popen([sys.executable, flip_and_flop_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
    sys.exit()
def linux_package_fallback():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    install_package_linux_path = os.path.join(current_directory, "install_package_linux.sh")
    time.sleep(5)
    subprocess.Popen([sys.executable, install_package_linux_path])
    sys.exit()

try :
    if sys.platform.startswith("linux") :
        if "DISPLAY" not in os.environ :
            failed = True
            print("Error, no graphic server detected !!")
            switch_to_console()
        else :
            init_gui_modules()
    else :
        init_gui_modules()
    
except :
    failed = True
    print("Error, the Pyside6 module is required to make the app work, without it you can't use the graphic interface !!")
    install_package = input("DO you want to install the Pyside6 python pack??")
    if install_package.lower() in ("Y, y, yes, YES") :
        """The package installation process should depend on the OS type, which are only two:
        if the targeted operating system is windows, then it is enought to use the following command : "python -m pip install PySide6
        - if this is a linux-targeted operating system, then the guaranteed working method is by creating an python environement then installing the 
        required package, and this is done via a bash
        """
        if sys.platform.startswith("linux") :
            linux_package_fallback()
        elif sys.platform.startswith("win"):
            subprocess.run("python -m pip install PySide6", shell=True)
            print("package installed !! attempting to restart.... ")
            call_flip_flop_restarter()
            sys.exit()
        else :
            failed = True
            print("Incompatible Platform, you may figure about how to install the package...")
            switch_to_console()
    else :
        switch_to_console()
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("Count My Lifetime V2.0 2026")
        self.resize(900, 500)
        self.font = QtGui.QFont("Arial", 25)
        self.label = QtWidgets.QLabel("Let's Count your lifetime !!!")
        self.label.setFont(self.font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.Layout = QtWidgets.QWidget.layout(self)
        self.Layout.addWidget(self.label)
        self.setCentralWidget(self.label)
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
