import subprocess

# Path to Sikuli's JAR file
sikulix_jar = r"C:\Users\gus\AppData\Roaming\tagui\src\sikulix\sikulix.jar"

# Path to your Sikuli script
sikuli_script = r'C:\SikuliX\myscript.sikuli'

# Build the command to execute Sikuli with the appropriate options
cmd = ['java', '-jar', sikulix_jar, '-r', sikuli_script]

# Use subprocess to launch the command and hide the window
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
subprocess.Popen(cmd, startupinfo=startupinfo)
