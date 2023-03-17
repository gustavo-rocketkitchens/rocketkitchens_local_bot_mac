import os
import signal
import subprocess
import logging

import psutil
import watchdog.events
import watchdog.observers
import time


class Handler(watchdog.events.PatternMatchingEventHandler):

    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.csv'], ignore_directories=True,
                                                             case_sensitive=False)
        self.process_running = False  # Add flag to keep track of whether the process is running
        self.file_processed = []  # Initialize list to keep track of processed files
        self.logger = logging.getLogger(__name__)

    def on_created(self, event):
        self.logger.info("Watchdog received created event - %s.", event.src_path)
        # Event is created, you can process it now
        ...

    def on_modified(self, event):
        self.logger.info("Watchdog received modified event - %s.", event.src_path)

        if event.src_path in self.file_processed:
            # File has been processed before, remove from the list
            self.file_processed.remove(event.src_path)

        if not self.process_running:  # Only start the process if it's not already running
            navigation_model = "dependencies/navigation_model.py"
            dist_robot_interface = "dependencies/robot-launcher.py"
            if os.path.exists(dist_robot_interface):
                minimize = 5
                self.logger.info("minimize = 5")
                for i in range(minimize):
                    subprocess.Popen(['python', navigation_model])
                    time.sleep(0.1)  # Add a brief pause to prevent overloading the system
                subprocess.Popen(['python', dist_robot_interface])
                self.process_running = True  # Set flag to indicate that the process is running


    def on_deleted(self, event):
        self.logger.info("Watchdog received deleted event - %s.", event.src_path)


        # If the file that was deleted is the file we are monitoring, stop the process and set the flag to False
        self.process_running = False
        # stop_process()
        self.logger.info("Process Running Status: %s ", self.process_running)

        # Remove the deleted file from the list of processed files

        self.process_running = False
        self.logger.info("File deleted. Removed from processed list.")
        self.logger.info("File Processed: %s  ", self.file_processed)
        self.logger.info("Process Running Status: %s ", self.process_running)


def start_observer(src_path):
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def stop_observer():
    observer = watchdog.observers.Observer()

    observer.stop()


def stop_process():
    # Stop the process by finding its PID and killing it
    process_name = "robot-launcher.py"
    pid = None
    for proc in psutil.process_iter():
        if process_name in proc.name():
            pid = proc.pid
            break
    if pid is not None:
        os.kill(pid, signal.SIGTERM)


if __name__ == "__main__":
    home_dir = os.path.expanduser("~")
    output_dir = os.path.join(home_dir, "Downloads", "output")

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    logger.info('output_dir: %s', output_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    logger.info("start_observer(%s)", output_dir)
    start_observer(output_dir)
