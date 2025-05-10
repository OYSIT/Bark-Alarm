"""
telegram_alarm_app_material.py  –  v5
=================================================
Ein komplettes Facelift mit **Kivy‑MD** (Material Design):

• **MDBottomNavigation** mit Tabs *Setup*, *Control*, *About*  
• **MDToolbar** mit Light/Dark‑Toggle  
• Alle Regler in **MDCards** (schön gruppiert)  
• Presets als **MDChips**  
• Riesen‑Bell‑Button (Hund‑Icon) für Sofort‑Bellen  
• Animation, wenn Alarm feuert (Puls‑Ring)  
• Persistenz & Logik der v4 bleibt erhalten

Voraussetzung: `pip install kivymd`  (Kivy ≥2.2)
"""

from __future__ import annotations

import json
import math
import os
import random
import threading
import time
from pathlib import Path
from typing import List

from kivy.animation import Animation
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (NumericProperty, ObjectProperty, StringProperty,
                             BooleanProperty)
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.slider import MDSlider
from kivymd.uix.textfield import MDTextField
from kivymd.uix.chip import MDChip

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from plyer import accelerometer
from kivy.clock import Clock, mainthread
from kivy.core.audio import SoundLoader

CONFIG_PATH = str(Path.home() / "bell_alarm_config.json")

KV = r"""
#:import md_icons kivymd.icon_definitions.md_icons
MDNavigationLayout:
    ScreenManager:
        id: scr_mngr
        Screen:
            name: "main"
            BoxLayout:
                orientation: 'vertical'

                MDToolbar:
                    id: toolbar
                    title: "Bell Alarm"
                    elevation: 10
                    right_action_items: [["weather-night", app.toggle_theme]]

                MDBottomNavigation:
                    id: bottom_nav

                    MDBottomNavigationItem:
                        name: 'setup'
                        text: 'Setup'
                        icon: 'tune'
                        ScrollView:
                            MDBoxLayout:
                                orientation: 'vertical'
                                adaptive_height: True
                                padding: dp(16)
                                spacing: dp(16)

                                MDTextField:
                                    id: token_input
                                    hint_text: 'Telegram Bot Token'
                                    mode: 'rectangle'

                                MDCard:
                                    orientation: 'vertical'
                                    padding: dp(12)
                                    ripple_behavior: True
                                    MDLabel:
                                        text: 'Empfindlichkeit (g)'
                                        theme_text_color: 'Secondary'
                                    MDSlider:
                                        id: thr_slider
                                        min: 0.5
                                        max: 3.0
                                        value: app.threshold_g
                                        step: 0.1
                                        on_value: app.on_threshold_change(self.value)
                                    MDLabel:
                                        id: thr_lbl
                                        text: f"{app.threshold_g:.1f} g"
                                        halign: 'right'
                                        theme_text_color: 'Hint'

                                MDCard:
                                    orientation: 'vertical'
                                    padding: dp(12)
                                    spacing: dp(8)
                                    MDLabel:
                                        text: 'Loops'
                                        theme_text_color: 'Secondary'
                                    MDSlider:
                                        id: loops_min_slider
                                        min: 1
                                        max: 10
                                        step: 1
                                        value: app.loops_min
                                        on_value: app.on_loops_min_change(self.value)
                                    MDSlider:
                                        id: loops_max_slider
                                        min: 1
                                        max: 10
                                        step: 1
                                        value: app.loops_max
                                        on_value: app.on_loops_max_change(self.value)
                                    MDLabel:
                                        id: loops_lbl
                                        text: f"{app.loops_min}-{app.loops_max}"
                                        halign: 'right'
                                        theme_text_color: 'Hint'

                                MDCard:
                                    orientation: 'vertical'
                                    padding: dp(12)
                                    spacing: dp(8)
                                    MDLabel:
                                        text: 'Pause (s)'
                                        theme_text_color: 'Secondary'
                                    MDSlider:
                                        id: pause_min_slider
                                        min: 0
                                        max: 3
                                        step: 0.1
                                        value: app.pause_min
                                        on_value: app.on_pause_min_change(self.value)
                                    MDSlider:
                                        id: pause_max_slider
                                        min: 0
                                        max: 3
                                        step: 0.1
                                        value: app.pause_max
                                        on_value: app.on_pause_max_change(self.value)
                                    MDLabel:
                                        id: pause_lbl
                                        text: f"{app.pause_min}-{app.pause_max}"
                                        halign: 'right'
                                        theme_text_color: 'Hint'

                                MDLabel:
                                    text: 'Presets'
                                    theme_text_color: 'Secondary'
                                MDBoxLayout:
                                    adaptive_height: True
                                    spacing: dp(8)
                                    MDChip:
                                        text: 'Leise'
                                        icon: 'volume-low'
                                        on_release: app.apply_preset('leise')
                                    MDChip:
                                        text: 'Normal'
                                        icon: 'volume-medium'
                                        on_release: app.apply_preset('normal')
                                    MDChip:
                                        text: 'Agro'
                                        icon: 'volume-high'
                                        on_release: app.apply_preset('agro')

                                MDRaisedButton:
                                    id: choose_btn
                                    text: 'Bell‑Sounds auswählen'
                                    on_release: app.open_file_chooser()

                    MDBottomNavigationItem:
                        name: 'control'
                        text: 'Control'
                        icon: 'dog'

                        MDBoxLayout:
                            orientation: 'vertical'
                            padding: dp(32)
                            spacing: dp(24)
                            MDLabel:
                                id: status_lbl
                                text: 'Bereit'
                                halign: 'center'
                                theme_text_color: 'Primary'
                                font_style: 'H5'

                            MDRaisedButton:
                                id: start_btn
                                text: 'Alarm starten'
                                md_bg_color: get_color_from_hex('#4CAF50')
                                on_release: app.start_alarm()
                                pos_hint: {'center_x': 0.5}

                            MDRaisedButton:
                                id: bell_btn
                                text: 'BELL!'
                                icon: 'dog'
                                md_bg_color: get_color_from_hex('#FF5722')
                                on_release: app.play_once()
                                pos_hint: {'center_x': 0.5}

                    MDBottomNavigationItem:
                        name: 'about'
                        text: 'About'
                        icon: 'information'
                        MDLabel:
                            text: "Bell Alarm\nMade with KivyMD"
                            halign: 'center'
"""


class BellPlayer:
    def __init__(self):
        self._sounds: List = []

    def load_files(self, filenames: List[str]):
        self._sounds = [SoundLoader.load(f) for f in filenames if SoundLoader.load(f)]

    def play_random_sequence(self, loops_min: int, loops_max: int, pause_min: float, pause_max: float):
        if not self._sounds:
            return
        loops = random.randint(loops_min, loops_max)
        for _ in range(loops):
            sound = random.choice(self._sounds)
            if sound:
                sound.play()
            time.sleep(random.uniform(pause_min, pause_max))


class MotionDetector(threading.Thread):
    def __init__(self, app: 'AlarmMaterialApp', cooldown: float = 3.0):
        super().__init__(daemon=True)
        self.app = app
        self.cooldown = cooldown
        self.stop_event = threading.Event()

    def run(self):
        accelerometer.enable()
        last_trigger = 0.0
        while not self.stop_event.is_set():
            val = accelerometer.acceleration
            if val and all(v is not None for v in val):
                g = math.sqrt(sum(v ** 2 for v in val)) / 9.81
                if g > self.app.threshold_g and time.time() - last_trigger > self.cooldown:
                    self.app.on_motion()
                    last_trigger = time.time()
            time.sleep(0.15)


class AlarmMaterialApp(MDApp):
    # Bindable properties
    threshold_g = NumericProperty(1.4)
    loops_min = NumericProperty(2)
    loops_max = NumericProperty(7)
    pause_min = NumericProperty(0.5)
    pause_max = NumericProperty(2.0)

    token = StringProperty("")
    is_running = BooleanProperty(False)

    def build(self):
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.theme_style = "Light"
        self.bell_player = BellPlayer()
        self._load_config()
        return Builder.load_string(KV)

    # ------------------- Theme Toggle ------------------- #
    def toggle_theme(self, *args):
        self.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == "Light" else "Light"

    # ------------------- Slider Callbacks ------------------- #
    def on_threshold_change(self, val):
        self.threshold_g = round(val, 1)
        self.root.ids.thr_lbl.text = f"{self.threshold_g:.1f} g"
        self._save_config()

    def on_loops_min_change(self, val):
        self.loops_min = int(val)
        if self.loops_min > self.loops_max:
            self.loops_max = self.loops_min
            self.root.ids.loops_max_slider.value = self.loops_max
        self.root.ids.loops_lbl.text = f"{self.loops_min}-{self.loops_max}"
        self._save_config()

    def on_loops_max_change(self, val):
        self.loops_max = int(val)
        if self.loops_max < self.loops_min:
            self.loops_min = self.loops_max
            self.root.ids.loops_min_slider.value = self.loops_min
        self.root.ids.loops_lbl.text = f"{self.loops_min}-{self.loops_max}"
        self._save_config()

    def on_pause_min_change(self, val):
        self.pause_min = round(val, 1)
        if self.pause_min > self.pause_max:
            self.pause_max = self.pause_min
            self.root.ids.pause_max_slider.value = self.pause_max
        self.root.ids.pause_lbl.text = f"{self.pause_min}-{self.pause_max}"
        self._save_config()

    def on_pause_max_change(self, val):
        self.pause_max = round(val, 1)
        if self.pause_max < self.pause_min:
            self.pause_min = self.pause_max
            self.root.ids.pause_min_slider.value = self.pause_min
        self.root.ids.pause_lbl.text = f"{self.pause_min}-{self.pause_max}"
        self._save_config()

    # ------------------- Presets ------------------- #
    def apply_preset(self, name: str):
        presets = {
            "leise": (1, 3, 1.0, 2.5),
            "normal": (2, 7, 0.5, 2.0),
            "agro": (5, 10, 0.0, 1.0),
        }
        self.loops_min, self.loops_max, self.pause_min, self.pause_max = presets[name]
        # Update sliders
        self.root.ids.loops_min_slider.value = self.loops_min
        self.root.ids.loops_max_slider.value = self.loops_max
        self.root.ids.pause_min_slider.value = self.pause_min
        self.root.ids.pause_max_slider.value = self.pause_max
        self.root.ids.loops_lbl.text = f"{self.loops_min}-{self.loops_max}"
        self.root.ids.pause_lbl.text = f"{self.pause_min}-{self.pause_max}"
        Snackbar(text=f"Preset '{name.title()}' angewendet").open()
        self._save_config()

    # ------------------- FileChooser ------------------- #
    def open_file_chooser(self):
        from kivymd.uix.filemanager import MDFileManager
        def _select(path):
            self.bell_player.load_files([path])
            Snackbar(text="Sound geladen").open()
            file_manager.close()
        file_manager = MDFileManager(select_path=_select, exit_manager=lambda *_: file_manager.close())
        file_manager.show("/")

    # ------------------- Telegram & Alarm ------------------- #
    def start_alarm(self):
        if self.is_running:
            self.stop_alarm()
            return
        self.token = self.root.ids.token_input.text.strip()
        if not self.token or not self.bell_player._sounds:
            Snackbar(text="Bitte Token und Sound laden!").open()
            return
        self.is_running = True
        self.root.ids.start_btn.text = "Alarm läuft (Stop)"
        self.root.ids.status_lbl.text = "Alarm läuft"
        Snackbar(text="Alarm gestartet").open()
        # start threads
        self.motion_detector = MotionDetector(self)
        self.motion_detector.start()
        threading.Thread(target=self._telegram_bot, daemon=True).start()

    def stop_alarm(self):
        self.is_running = False
        self.motion_detector.stop_event.set()
        self.root.ids.start_btn.text = "Alarm starten"
        self.root.ids.status_lbl.text = "Bereit"
        Snackbar(text="Alarm gestoppt").open()

    def play_once(self):
        if not self.bell_player._sounds:
            Snackbar(text="Kein Sound geladen!").open()
            return
        threading.Thread(target=self.bell_player.play_random_sequence,
                         args=(self.loops_min, self.loops_max, self.pause_min, self.pause_max),
                         daemon=True).start()

    @mainthread
    def on_motion(self):
        if not self.is_running:
            return
        # Pulsanimation des Bell Buttons
        btn = self.root.ids.bell_btn
        anim = Animation(scale=1.2, duration=0.1) + Animation(scale=1.0, duration=0.2)
        btn.scale = 1.0
        anim.start(btn)
        # Play sound
        threading.Thread(target=self.bell_player.play_random_sequence,
                         args=(self.loops_min, self.loops_max, self.pause_min, self.pause_max),

