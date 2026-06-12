from date_time_retrieving import input_age_reformulation
import os, sys

failed = False
def switch_to_console() :
    switch_to_cli = input("Do you want to switch to the CLI interface (yes(y)/no(n))")
    if (switch_to_cli.lower() in["yes", "y"]  ) :
        import no_gui_run
        sys.exit(0)
    else :  
        sys.exit(1)

def init_gui_modules() :
        global QtWidgets, Qt, QtGui
        import PySide6.QtWidgets as QtWidgets 
        from PySide6.QtCore import Qt
        import PySide6.QtGui as QtGui## this is where we will use Qfont


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
        
except ModuleNotFoundError:
    failed = True
    print("Error, the Pyside6 module is required to make the app work, without it you can't use the graphic interface !!")
    install_package = input("DO you want to install the Pyside6 python package??")
    if install_package.lower() in ("Y, y, yes, YES") :
        pass

    else :
        switch_to_console()
    sys.exit(0)





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
