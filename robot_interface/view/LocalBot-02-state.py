
import argparse
import itertools
import os
from abc import ABC
from os.path import dirname
from kivy.lang import Builder
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivymd.theming import ThemableBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase

from kivy.uix.screenmanager import ScreenManager

from kivymd.uix.screen import MDScreen

from kivy.core.window import Window

from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivymd.uix.list import OneLineIconListItem, MDList