import secrets
import string

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.clipboard import Clipboard


class PasswordApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        title = Label(
            text="Password Generator",
            font_size=28
        )

        self.length_input = TextInput(
            text="16",
            multiline=False,
            input_filter="int"
        )

        generate_button = Button(
            text="Generate Password",
            font_size=20
        )

        self.password_label = Label(
            text="Your password will appear here",
            font_size=20
        )

        copy_button = Button(
            text="Copy Password",
            font_size=20
        )

        generate_button.bind(
            on_press=self.generate_password
        )

        copy_button.bind(
            on_press=self.copy_password
        )

        layout.add_widget(title)
        layout.add_widget(self.length_input)
        layout.add_widget(generate_button)
        layout.add_widget(self.password_label)
        layout.add_widget(copy_button)

        return layout

    def generate_password(self, instance):
        length = int(self.length_input.text or 16)

        characters = (
            string.ascii_letters
            + string.digits
            + "!@#$%^&*"
        )

        password = "".join(
            secrets.choice(characters)
            for _ in range(length)
        )

        self.password_label.text = password

    def copy_password(self, instance):
        Clipboard.copy(self.password_label.text)


PasswordApp().run()import random
import string

def generate_password():
    length = int(length_input.text)
    
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(characters) for _ in range(length))
    
    password_label.text = password

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class PasswordApp(App):
    def build(self):
        global length_input, password_label

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        title = Label(
            text="Password Generator",
            font_size=28
        )

        length_input = TextInput(
            text="16",
            multiline=False,
            input_filter="int"
        )

        generate_button = Button(
            text="Generate Password",
            font_size=20
        )

        password_label = Label(
            text="Your password will appear here",
            font_size=20
        )

        generate_button.bind(on_press=lambda x: generate_password())

        layout.add_widget(title)
        layout.add_widget(length_input)
        layout.add_widget(generate_button)
        layout.add_widget(password_label)

        return layout

PasswordApp().run()
