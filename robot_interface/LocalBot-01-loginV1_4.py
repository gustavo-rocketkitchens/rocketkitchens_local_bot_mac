import subprocess

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.icon_definitions import md_icons
from kivymd.uix.button import MDTextButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screenmanager import MDScreenManager

from rocketkitchens_local_bot_master.robot_interface.model.credentials import passport as ps

from rocketkitchens_local_bot_master.robot_interface.controller import observer_controller as obs

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
from kivymd.uix.textfield import MDTextField

Window.size = (350, 400)

import watchdog.events
import watchdog.observers
import time

class Manager(ScreenManager):
    # image_source = StringProperty('')
    pass


class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def login(self, instance):
        global username
        global password
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        # Check login credentials
        if cred.get(username) == password:
            # Login successful, go to main screen
            self.manager.current = 'main'
        else:
            # Login failed
            self.ids.username_input.text = ''
            self.ids.password_input.text = ''
            self.ids.username_input.hint_text = 'Invalid username or password'
            self.ids.password_input.hint_text = 'Invalid username or password'

class MainScreen(MDScreen):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Call the Controller
        self.obs_start = obs.start_controller

        # Call for stop the Controller
        self.obs_stop = obs.stop_controller

        # Launch the Robots
        self.obs_bot = obs.start_bot_controller

    def logout(self, instance):
        print(username)
        print(password)
        LoginScreen().login(instance)
        # LoginScreen.login.username = ''
        # LoginScreen.login.password = ''
        # self.username_input.text = ''
        # self.password_input.text = ''
        self.manager.current = 'login'
        # LoginScreen().login(instance)


class RocketKitchens(MDApp):

    def build(self):
        # self.screen_manager = MDScreenManager()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        # self.icons = list(md_icons.keys())[15:30]
        # self.iter_list_names = iter(list(self.icons))
        self.icon = 'logo.png'
        # self.login_screen = LoginScreen(name='login_screen')
        # self.main_screen = MainScreen(name='main_page')
        #
        # self.screen_manager.add_widget(self.login_screen)
        # self.screen_manager.add_widget(self.main_screen)

        # return self.screen_manager
        # Builder.load_file('LocalBot-01-loginV1_4.kv')
        return Manager()


RocketKitchens().run()

