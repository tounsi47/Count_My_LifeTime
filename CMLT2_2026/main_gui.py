import os, sys
failed = False
def switch_to_console() :
    switch_to_cli = input("Do you want to switch to the CLI interface (yes(y)/no(n))")
    if (switch_to_cli.lower() in["yes", "y"]  ) :
        import no_gui_run
        sys.exit(0)
    else :  
        sys.exit(1)

def init_module() :
        global QtWidgets, Qt, QtGui
        import PyQt6.QtWidgets as QtWidgets 
        from PyQt6.QtCore import Qt
        import PyQt6.QtGui as QtGui## this is where we will use Qfont


try : 
    if sys.platform.startswith("linux") :
        if "DISPLAY" not in os.environ :
            failed = True
            print("Error, no graphic server detected !!")
            switch_to_console()
        else :
            init_module()
            
    
    
    else :
        init_module()
except ModuleNotFoundError:
    failed = True
    print("Error, the PyQt6 module is required to make the app work, without it you can't use the graphic interface !!")
    switch_to_console()
    sys.exit(0)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("Cout My Lifetime V2.0 2026")
        self.resize(1300, 700)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
