import subprocess

from kivy.core.window import Window
from kivymd.uix.button import MDTextButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screenmanager import MDScreenManager

from rocket_kitchens_local_bot.robot_interface.model.credentials import passport as ps

from rocket_kitchens_local_bot.robot_interface.controller import observer_controller as obs



def credential():
    dict_credential = {
        "ahmd": "ahmd123",
        "hassan": "hassan123",
        "accounts": "accounts123",
        "marwan": "marwan123",
        "gustavo": "gustavo123"
    }
    return dict_credential


cred = ps.credential()

# main.py

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivymd.uix.screen import MDScreen
# from kivymd.tools.hotreload.app import MDApp
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
Window.size = (400, 300)


import watchdog.events
import watchdog.observers
import time

class LoginScreen(MDScreen):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        self.username_input = TextInput(hint_text='Username')
        layout.add_widget(self.username_input)

        self.password_input = TextInput(hint_text='Password', password=True)
        layout.add_widget(self.password_input)

        login_button = Button(text='Login', on_press=self.login)
        layout.add_widget(login_button)

        self.add_widget(layout)

        #================================

    def start_controller(self):
        obs.start_controller()

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        # Check login credentials
        if cred.get(username) == password:
            # Login successful, go to main screen
            self.manager.current = 'main_page'
        else:
            # Login failed
            self.username_input.text = ''
            self.password_input.text = ''
            self.username_input.hint_text = 'Invalid username or password'
            self.password_input.hint_text = 'Invalid username or password'


class MainScreen(MDScreen):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        src_path = r"D:\Arquivos HD\Projetos HD\SD Labs\JOBS\Ahmd\rocket\rocket_kitchens\Dashboard\View\Pages\output"

        self.add_widget(MDLabel(text='Welcome to the main screen!'))

        # Call the Controller
        self.obs_start = obs.start_controller
        self.obs_stop = obs.stop_controller
        control_layout = BoxLayout(orientation='horizontal')
        start_button = Button(text='Start',
                              size_hint=(0.1, .2),
                              on_press=self.obs_start)


        stop_button = Button(text='Stop',
                             size_hint=(0.1, .2),
                             on_press=obs.stop_controller
                             )


        status_button = Button(text='status', size_hint=(0.1, .2))
        logout_button = Button(text='logout', size_hint=(0.1, .2))
        control_layout.add_widget(start_button)
        control_layout.add_widget(stop_button)
        control_layout.add_widget(status_button)
        control_layout.add_widget(logout_button)

        self.add_widget(control_layout)

    def on_button_press(self, instance):
        print("Starting Observer")
        subprocess.Popen(['python', '../model/observer_model.py'])

class ScreenManagementApp(MDApp):
    def build(self):
        self.screen_manager = MDScreenManager()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        self.login_screen = LoginScreen(name='login_screen')
        self.main_screen = MainScreen(name='main_page')

        self.screen_manager.add_widget(self.login_screen)
        self.screen_manager.add_widget(self.main_screen)

        return self.screen_manager

class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.csv'],
                                                             ignore_directories=True, case_sensitive=False)

    def on_created(self, event):
        print("Watchdog received created event - % s." % event.src_path)
        # Event is created, you can process it now

    def on_modified(self, event):
        print("Watchdog received modified event - % s." % event.src_path)
        # Event is modified, you can process it now


if __name__ == '__main__':
    ScreenManagementApp().run()