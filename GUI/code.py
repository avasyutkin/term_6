import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import kivy
from kivy.app import App
from  kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import АТБАШ
import Квадрат_Полибия
import Шифр_Цезаря
import Шифр_Тритемия
import Шифр_Белазо
import Шифр_Виженера

Window.size = (900, 410)
Window.clearcolor = (1, 1, 1, 0)
cipher_array = {'АТБАШ_var': 'АТБАШ', 'Квадрат_Полибия_var': 'Квадрат Полибия', 'Шифр_Цезаря_var': 'Шифр Цезаря', 'Шифр_Тритемия_var': 'Шифр Тритемия', 'Шифр_Белазо_var': 'Шифр Белазо', 'Шифр_Виженера_var': 'Шифр Виженера'}

class Interface(App):
    def build(self):
        self.label_input = Label()
        self.label_input.text = 'Введите сообщение'
        self.label_input.font_size = 13
        self.label_input.pos = (19, 390)
        self.label_input.size = (120, 14)
        self.label_input.color = (255, 255, 255)

        self.input_message = TextInput()
        self.input_message.pos = (17, 285)
        self.input_message.size = (660, 100)
        self.input_message.background_color = (.196, .196, .196, .1)

        self.button_encryption = Button()
        self.button_encryption.size = (180, 40)
        self.button_encryption.pos = (700, 344)
        self.button_encryption.background_color = (.196, .196, .196, .2)
        self.button_encryption.text = 'Зашифровать'
        self.button_encryption.color = (255, 255, 255)

        self.button_decryption = Button()
        self.button_decryption.size = (180, 40)
        self.button_decryption.pos = (700, 285)
        self.button_decryption.background_color = (.196, .196, .196, .1)
        self.button_decryption.text = 'Расшифровать'
        self.button_decryption.color = (255, 255, 255)

        self.label_input_key = Label()
        self.label_input_key.text = 'Введите ключи через пробел'
        self.label_input_key.font_size = 13
        self.label_input_key.pos = (47, 211)
        self.label_input_key.size = (120, 14)
        self.label_input_key.color = (255, 255, 255)

        self.input_key = TextInput()
        self.input_key.pos = (17, 175)
        self.input_key.size = (660, 30)
        self.input_key.background_color = (.196, .196, .196, .1)

        self.label_output = Label()
        self.label_output.text = 'Результат преобразования'
        self.label_output.font_size = 13
        self.label_output.pos = (40, 125)
        self.label_output.size = (120, 14)
        self.label_output.color = (255, 255, 255)

        self.output_message = TextInput()
        self.output_message.pos = (17, 20)
        self.output_message.size = (860, 100)
        self.output_message.background_color = (.196, .196, .196, .1)

        self.layout_array_cipher = GridLayout()
        self.layout_array_cipher.cols = len(cipher_array)
        self.layout_array_cipher.spacing = 20
        self.layout_array_cipher.size_hint_x = None

        for cipher in cipher_array:
            globals()[cipher] = ToggleButton(group='group', text=cipher_array[cipher], size_hint_x=None, height=40, color=(0, 0, 0), font_size=13, width=120, background_normal='')
            self.layout_array_cipher.add_widget(globals()[cipher])
        self.scroll_cipher_array = ScrollView(size_hint=(1, None), size=(863, 30), pos=(16, 245), bar_color=(0, 0, 0, 0), bar_inactive_color=(0, 0, 0, 0))
        self.scroll_cipher_array.add_widget(self.layout_array_cipher)

        self.form = Widget()
        self.form.add_widget(self.label_input)
        self.form.add_widget(self.input_message)
        self.form.add_widget(self.button_encryption)
        self.form.add_widget(self.button_decryption)
        self.form.add_widget(self.label_input_key)
        self.form.add_widget(self.input_key)
        self.form.add_widget(self.label_output)
        self.form.add_widget(self.output_message)
        self.form.add_widget(self.scroll_cipher_array)

        def encryption(instance):
            str = ''
            if АТБАШ_var.state == 'down':
                self.output_message.text = АТБАШ.encryption(self.input_message.text, str)
            if Квадрат_Полибия_var.state == 'down':
                self.output_message.text = Квадрат_Полибия.encryption(self.input_message.text, str)
            if Шифр_Цезаря_var.state == 'down':
                if self.input_key.text == '':
                    self.button_encryption.disabled
                else:
                    self.output_message.text = Шифр_Цезаря.encryption(self.input_message.text, str, self.input_key.text)
            if Шифр_Тритемия_var.state == 'down':
                self.output_message.text = Шифр_Тритемия.encryption(self.input_message.text, str)
            if Шифр_Виженера_var.state == 'down':
                if self.input_key.text == '':
                    self.button_encryption.disabled
                else:
                    self.output_message.text = Шифр_Виженера.encryption(self.input_message.text, str, self.input_key.text)
            if Шифр_Белазо_var.state == 'down':
                if self.input_key.text == '':
                    self.button_encryption.disabled
                else:
                    self.output_message.text = Шифр_Белазо.encryption(self.input_message.text, str, self.input_key.text)


        def decryption(instance):
            str = ''
            if АТБАШ_var.state == 'down':
                self.output_message.text = АТБАШ.decryption(self.input_message.text, str)
            if Квадрат_Полибия_var.state == 'down':
                self.output_message.text = Квадрат_Полибия.decryption(self.input_message.text, str)
            if Шифр_Цезаря_var.state == 'down':
                if self.input_key.text == '':
                    self.button_decryption.disabled
                else:
                    self.output_message.text = Шифр_Цезаря.decryption(self.input_message.text, str, self.input_key.text)
            if Шифр_Тритемия_var.state == 'down':
                self.output_message.text = Шифр_Тритемия.decryption(self.input_message.text, str)
            if Шифр_Виженера_var.state == 'down':
                if self.input_key.text == '':
                    self.button_decryption.disabled
                else:
                    self.output_message.text = Шифр_Виженера.decryption(self.input_message.text, str, self.input_key.text)
            if Шифр_Белазо_var.state == 'down':
                if self.input_key.text == '':
                    self.button_decryption.disabled
                else:
                    self.output_message.text = Шифр_Белазо.decryption(self.input_message.text, str, self.input_key.text)


        self.button_encryption.bind(on_press=encryption)
        self.button_decryption.bind(on_press=decryption)
        self.layout_array_cipher.bind(minimum_width=self.layout_array_cipher.setter('width'))

        return self.form


if __name__ == '__main__':
    Interface().run()


