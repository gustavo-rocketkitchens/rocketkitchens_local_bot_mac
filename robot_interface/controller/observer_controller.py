import os
import glob

import subprocess
# MacOS Computer Compilation
from rocketkitchens_local_bot_master.robot_interface.model import observer_model
from rocketkitchens_local_bot_master.robot_interface.model.observer_model import Handler


# Notebook Compilation
# from robot_interface.model import observer_model
# from robot_interface.model.observer_model import Handler

observer_process = None


def start_controller(instance):

    global observer_process

    # Get the current working directory
    # Get the current working directory
    cwd = os.getcwd()
    print("observer_controller")
    print("I am here: ")
    print(cwd)

    # launcher_oberserver = observer_model.start_observer(src_path)

    dist_robot_interface = "dependencies/observer_model.py"

    # RUN WITH SCRIPT
    # observer_process = subprocess.Popen(['python', 'model/observer_model.py'])

    # RUN WITH PYINSTALLER
    observer_process = subprocess.Popen(['python', dist_robot_interface])

    # Run the Python script
    print('observer_process = ', observer_process)


def stop_controller(instance):
    global observer_process
    # Construct a platform-independent path to the output folder
    output_dirname = 'output'
    src_path = os.path.join(os.getcwd(), 'robot_interface', 'model', 'robot_models', output_dirname)

    # Search for the output folder using the glob module
    if not os.path.exists(src_path):
        src_path = glob.glob(f'**/{output_dirname}', recursive=True)[0]

    # Get the current working directory
    cwd = os.getcwd()

    # Navigate to the parent directory
    os.chdir('..')

    observer_process.kill()
    print("stopping observer")

    # Navigate back to the original working directory
    os.chdir(cwd)


def start_bot_controller(instance):
    bot_process = subprocess.Popen(['python', 'model/robot-launcher.py'])
    print(bot_process)

