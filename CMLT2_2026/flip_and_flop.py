import sys, subprocess, time, os

print("restarting....")
time.sleep(3)
current_directory =  os.path.dirname(os.path.abspath(__file__))
main_gui_path = os.path.join(current_directory, "main_gui.py")
subprocess.Popen([sys.executable, main_gui_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
print(">>> Script restarted ! attempting to load the graphic modules...")
time.sleep(3)
sys.exit()
