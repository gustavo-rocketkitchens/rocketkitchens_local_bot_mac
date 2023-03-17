import subprocess

from kivy.core.window import Window
from kivymd.uix.button import MDTextButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screenmanager import MDScreenManager

from rocket_kitchens_local_bot.robot_interface.model.credentials import passport as ps

from rocket_kitchens_local_bot.robot_interface.controller import observer_controller as obs

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

        # Create an instance of MDCard
        card = MDCard(padding=20)

        # Add the username and password inputs to the card
        self.username_input = TextInput(hint_text='Username')
        card.add_widget(self.username_input)

        self.password_input = TextInput(hint_text='Password', password=True)
        card.add_widget(self.password_input)

        # Add the card to the layout
        layout.add_widget(card)

        login_button = Button(text='Login', on_press=self.login)
        layout.add_widget(login_button)

        self.add_widget(layout)

        # ================================

    def login(self, instance):
        global username
        global password
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

        self.add_widget(MDLabel(text='Welcome to the main screen!'))

        # Call the Controller
        self.obs_start = obs.start_controller

        # Call for stop the Controller
        self.obs_stop = obs.stop_controller

        # Launch the Robots
        self.obs_bot = obs.start_bot_controller

        control_layout = BoxLayout(orientation='horizontal')

        #  Start the Controller Button
        start_button = Button(text='Start',
                              size_hint=(0.1, .2),
                              on_press=self.obs_start)

        # Stop the Controller Button
        stop_button = Button(text='Stop',
                             size_hint=(0.1, .2),
                             on_press=obs.stop_controller
                             )

        # Call the Logout
        # self.logout = logout()

        # Status Button
        status_button = Button(text='status', size_hint=(0.1, .2))
        logout_button = Button(text='Logout', size_hint=(0.1, .2), on_press=self.logout)
        control_layout.add_widget(start_button)
        control_layout.add_widget(stop_button)
        control_layout.add_widget(status_button)
        control_layout.add_widget(logout_button)

        self.add_widget(control_layout)

    def logout(self, instance):
        print(username)
        print(password)
        LoginScreen().login(instance)
        # LoginScreen.login.username = ''
        # LoginScreen.login.password = ''
        # self.username_input.text = ''
        # self.password_input.text = ''
        self.manager.current = 'login_screen'
        # LoginScreen().login(instance)


class LocalBot(MDApp):
    def build(self):
        self.screen_manager = MDScreenManager()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"

        self.login_screen = LoginScreen(name='login_screen')
        self.main_screen = MainScreen(name='main_page')

        self.screen_manager.add_widget(self.login_screen)
        self.screen_manager.add_widget(self.main_screen)

        return self.screen_manager


if __name__ == '__main__':
    LocalBot().run()