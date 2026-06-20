from date_time_retrieving import input_age_reformulation
from time_unites import TimeUnites
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
        global QtWidgets, Qt, QtGui, QDate
        import PySide6.QtWidgets as QtWidgets 
        from PySide6.QtCore import Qt
        from PySide6.QtCore import QDate
        import PySide6.QtGui as QtGui
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

    

#defining a few buttons' action :
def quit():
    app.quit()
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
        self.setWindowTitle("Count My LifeTime V2.0 2026")
        self.resize(1000, 500)
        central_widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
    

        sub_layout1 = QtWidgets.QHBoxLayout()
        btn_quit = QtWidgets.QPushButton("exit")
        btn_quit.clicked.connect(quit)
        btn_about = QtWidgets.QPushButton("about CMLT")
        sb1_elements = [btn_quit, btn_about]  # sb1_elemnts = sub_layout_1 elemnts
        for i in sb1_elements :
            sub_layout1.addWidget(i, alignment=Qt.AlignmentFlag.AlignTop)
        
        sub_layout2 = QtWidgets.QHBoxLayout()
        order_text = QtWidgets.QLabel("Please enter your birthdate , then choose one of the conversion options below :  ")
        self.birthday_list = QtWidgets.QDateEdit()
        submit = QtWidgets.QPushButton("Submit")
        submit.clicked.connect(self.fetch_data)
        sb2_elements = [order_text, self.birthday_list, submit]
        for i in sb2_elements :
            sub_layout2.addWidget(i, alignment = Qt.AlignmentFlag.AlignVCenter)
        
        sub_layout3 = QtWidgets.QHBoxLayout()
        
        btn_seconds = QtWidgets.QPushButton("Convert to Seconds")
        btn_seconds.clicked.connect(self.convert_to_seconds)
        
        btn_minutes = QtWidgets.QPushButton("Convert to Minutes")
        btn_minutes.clicked.connect(self.convert_to_minutes)

        btn_hours = QtWidgets.QPushButton("Convert to Hours")
        btn_hours.clicked.connect(self.convert_to_hours)

        sb3_elements = [btn_seconds, btn_minutes, btn_hours]
        for i in sb3_elements :
            sub_layout3.addWidget(i)

        sub_layout4 = QtWidgets.QHBoxLayout()
        btn_days = QtWidgets.QPushButton("Convert to Days")
        btn_days.clicked.connect(self.convert_to_days)

        btn_weeks = QtWidgets.QPushButton("Convert to Weeks")
        btn_weeks.clicked.connect(self.convert_to_weeks)
        btn_months = QtWidgets.QPushButton("Convert to Months")
        btn_months.clicked.connect(self.convert_to_months)
        sb4_elements = [btn_days, btn_weeks, btn_months]
        for i in sb4_elements :
            sub_layout4.addWidget(i)
        

        sub_layouts = [sub_layout1, sub_layout2, sub_layout3 , sub_layout4]
        for i in sub_layouts  :
            layout.addLayout(i)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    def fetch_data(self):
        
        qdate =  self.birthday_list.date()

        day = int(qdate.day())
        month = int(qdate.month())
        year = int(qdate.year())
        self.birthdate = input_age_reformulation(year, month, day)
        self.input_age = self.birthdate.retrieve_input_age()
        self.birth_year = self.birthdate.year


        self.total_age = self.input_age[0]
        self.rest_of_days = self.input_age[1]
        print(self.total_age, self.rest_of_days)
        return self.input_age
    def convert_to_seconds(self):
        age_in_seconds = TimeUnites(self.input_age).convert_to_seconds()
        
        print(age_in_seconds)
    def convert_to_minutes(self):
        age_in_minutes = TimeUnites(self.input_age).convert_to_minutes()
        print(age_in_minutes)
    def convert_to_hours(self):
        age_in_hours = TimeUnites(self.input_age).convert_to_hours()
        print(age_in_hours)
    def convert_to_days(self):
        age_in_days = TimeUnites(self.input_age).convert_to_days(self.birth_year)
        print(age_in_days)
    def convert_to_weeks(self):
        age_in_weeks  = TimeUnites(self.input_age).convert_to_weeks()
        print(age_in_weeks)
    def convert_to_months(self):
        age_in_months = TimeUnites(self.input_age).convert_to_months()
        print(age_in_months)
    
class Results(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Results : ")
        self.resize(750, 225)
        second_widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()

        sub_layout1 = QtWidgets.QHBoxLayout()
        Result = QtWidgets.QLabel("Results")
        sub_layout1.addWidget(Result, alignment  = Qt.AlignmentFlag.AlignHCenter)
        layout.addLayout(sub_layout1)
        sub_layout2 = QtWidgets.QHBoxLayout()
        self.total_age  = QtWidgets.QLabel(f"Total age : {self.total_age} years and {self.rest_of_days}")
        sub_layout2.addWidget(self.total_age)
        layout.addLayout(sub_layout2)
        second_widget.setCentralLayout(layout)   
    
        
            
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
