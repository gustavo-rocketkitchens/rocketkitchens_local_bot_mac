import sys
print(sys.platform)


class ChromeWindow:
    def __init__(self, os):
        self.os = os

    def minimize(self):
        if self.os == 'win32':
            import win32gui
            import win32con

            # Get the handle of the current Chrome window
            chrome_handle = win32gui.GetForegroundWindow()

            # Minimize the window
            win32gui.ShowWindow(chrome_handle, win32con.SW_MINIMIZE)

        elif self.os == 'darwin':
            import AppKit

            # Get the current window object
            window = AppKit.NSApp.keyWindow()

            # Minimize the window
            window.miniaturize_(None)

        else:
            print("Unsupported operating system.")

    def close(self):
        if self.os == 'win32':
            import win32gui
            import win32con
            # Get the handle of the current Chrome window
            chrome_handle = win32gui.GetForegroundWindow()

            # Close the window
            win32gui.PostMessage(chrome_handle, win32con.WM_CLOSE, 0, 0)

        elif self.os == 'darwin':
            import AppKit

            # Get the current window object
            window = AppKit.NSApp.keyWindow()

            # Close the window
            window.performClose_(None)

        else:
            print("Unsupported operating system.")

    def restore(self):
        if self.os == 'win':
            import win32gui
            import win32api
            import win32con

            # Restore the window
            win32gui.SendMessage(win32gui.GetForegroundWindow(), win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
            win32api.keybd_event(0x5B, 0, 0, 0) # left windows key down
            win32api.keybd_event(0x31, 0, 0, 0) # 1 key down
            win32api.keybd_event(0x31, 0, win32con.KEYEVENTF_KEYUP, 0) # 1 key up
            win32api.keybd_event(0x5B, 0, win32con.KEYEVENTF_KEYUP, 0) # left windows key up

        elif self.os == 'darwin':
            import subprocess

            # Restore the window
            subprocess.call(["osascript", "-e", 'tell application "Google Chrome" to activate'])

            # Bring the tab with the title 'My Restaurant' to the foreground
            subprocess.call(["osascript", "-e", 'tell application "Google Chrome" to tell the first window to set active tab index to (get index of (first tab whose title contains "My Restaurant"))'])

        else:
            print("Unsupported operating system.")


if __name__ == "__main__":
    import sys

    print(sys.platform)
    os_name = sys.platform
    chrome = ChromeWindow(os_name)
    chrome.minimize()
