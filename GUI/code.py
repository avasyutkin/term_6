# -*- coding: utf-8 -*-
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
import Матричный_шифр
import Решетка_Кардано
import Шифр_Плэйфера
import Вертикальная_перестановка
import S_блок_замены


Window.size = (900, 410)
Window.clearcolor = (1, 1, 1, 0)
cipher_array = {'АТБАШ_var': 'АТБАШ', 'Квадрат_Полибия_var': 'Квадрат Полибия', 'Шифр_Цезаря_var': 'Шифр Цезаря', 'Шифр_Тритемия_var': 'Шифр Тритемия', 'Шифр_Белазо_var': 'Шифр Белазо', 'Шифр_Виженера_var': 'Шифр Виженера', 'S_block_var': 'S-блок замены', 'Матричный_шифр_var': 'Матричный шифр', 'Шифр_Плэйфера_var': 'Шифр Плэйфера', 'Перестановка_var': ' Перестановка', 'Решетка_Кардано_var': 'Решетка Кардано'}

class Interface(App):
    def build(self):
        self.label_input = Label()
        self.label_input.text = 'Введите сообщение'
        self.label_input.font_name = 'Arial'
        self.label_input.font_size = 13
        self.label_input.pos = (19, 390)
        self.label_input.size = (120, 14)
        self.label_input.color = (255, 255, 255)

        self.input_message = TextInput()
        self.input_message.pos = (17, 285)
        self.input_message.size = (660, 100)
        self.input_message.font_name = 'Arial'
        self.input_message.background_color = (.196, .196, .196, .1)

        self.button_encryption = Button()
        self.button_encryption.size = (180, 40)
        self.button_encryption.pos = (700, 344)
        self.button_encryption.background_color = (.196, .196, .196, .2)
        self.button_encryption.text = 'Зашифровать'
        self.button_encryption.font_name = 'Arial'
        self.button_encryption.color = (255, 255, 255)

        self.button_decryption = Button()
        self.button_decryption.size = (180, 40)
        self.button_decryption.pos = (700, 285)
        self.button_decryption.background_color = (.196, .196, .196, .1)
        self.button_decryption.text = 'Расшифровать'
        self.button_decryption.font_name = 'Arial'
        self.button_decryption.color = (255, 255, 255)

        self.label_input_key = Label()
        self.label_input_key.text = 'Введите ключи через пробел'
        self.label_input_key.font_name = 'Arial'
        self.label_input_key.font_size = 13
        self.label_input_key.pos = (47, 211)
        self.label_input_key.size = (120, 14)
        self.label_input_key.color = (255, 255, 255)

        self.input_key = TextInput()
        self.input_key.pos = (17, 175)
        self.input_key.size = (660, 30)
        self.input_key.background_color = (.196, .196, .196, .1)
        self.input_key.font_name = 'Arial'

        self.key_warning = Label()
        self.key_warning.text = 'В случае несоответствия ключа параметрам ключ может быть изменён'
        self.key_warning.font_name = 'ariali'
        self.key_warning.pos = (142, 163)
        self.key_warning.color = (.196, .196, .196, .2)
        self.key_warning.font_size = 10
        self.key_warning.size = (120, 14)

        self.label_output = Label()
        self.label_output.text = 'Результат преобразования'
        self.label_output.font_name = 'Arial'
        self.label_output.font_size = 13
        self.label_output.pos = (40, 125)
        self.label_output.size = (120, 14)
        self.label_output.color = (255, 255, 255)

        self.output_message = TextInput()
        self.output_message.pos = (17, 20)
        self.output_message.size = (860, 100)
        self.output_message.font_name = 'Arial'
        self.output_message.background_color = (.196, .196, .196, .1)

        self.layout_array_cipher = GridLayout()
        self.layout_array_cipher.font_name = 'Arial'
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
        self.form.add_widget(self.key_warning)
        self.form.add_widget(self.label_output)
        self.form.add_widget(self.output_message)
        self.form.add_widget(self.scroll_cipher_array)

        def encryption(instance):
            str = ''
            if АТБАШ_var.state == 'down':
                self.output_message.text = АТБАШ.encryption(self.input_message.text, str)
            if Квадрат_Полибия_var.state == 'down':
                self.output_message.text = Квадрат_Полибия.encryption(self.input_message.text)
            if Шифр_Цезаря_var.state == 'down':
                if self.input_key.text == '':
                    self.button_encryption.disabled
                else:
                    calculation = Шифр_Цезаря.validate(self.input_message.text, self.input_key.text, True)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if Шифр_Тритемия_var.state == 'down':
                self.output_message.text = Шифр_Тритемия.encryption(self.input_message.text)
            if Шифр_Виженера_var.state == 'down':
                if self.input_key.text == '':
                    self.button_encryption.disabled
                else:
                    calculation = Шифр_Виженера.validate(self.input_message.text, self.input_key.text, True)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if Шифр_Белазо_var.state == 'down':
                if self.input_key.text == '':
                    self.button_encryption.disabled
                else:
                    calculation = Шифр_Белазо.validate(self.input_message.text, self.input_key.text, True)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if Матричный_шифр_var.state == 'down':
                if self.input_key.text == '':
                    self.button_encryption.disabled
                else:
                    if Матричный_шифр.matrix_check(Матричный_шифр.key_generation(Матричный_шифр.key_to_array(self.input_key.text))) == 'Введенный ключ не подходит для шифрования, введите другой.':
                        self.output_message.text = 'Введенный ключ не подходит для шифрования, введите другой.'
                    else:
                        self.output_message.text = Матричный_шифр.encryption(Матричный_шифр.message_to_vector(Матричный_шифр.message_to_index(self.input_message.text), Матричный_шифр.key_to_array(self.input_key.text)), Матричный_шифр.key_generation(Матричный_шифр.key_to_array(self.input_key.text)))
            if Решетка_Кардано_var.state == 'down':
                Решетка_Кардано_сообщение_ключ = Решетка_Кардано.encryption(self.input_message.text)
                self.output_message.text = Решетка_Кардано_сообщение_ключ[0]
                self.input_key.text = Решетка_Кардано_сообщение_ключ[1]
            if Перестановка_var.state == 'down':
                if self.input_key.text == '':
                    self.button_encryption.disabled
                else:
                    self.output_message.text = Вертикальная_перестановка.encryption(Вертикальная_перестановка.message_to_vector_enc(Вертикальная_перестановка.vector_initialization(self.input_message.text, self.input_key.text), self.input_message.text, self.input_key.text), self.input_key.text)
            if Шифр_Плэйфера_var.state == 'down':
                if self.input_key.text == '':
                    self.button_encryption.disabled
                else:
                    self.output_message.text = Шифр_Плэйфера.encryption(Шифр_Плэйфера.before_processing(self.input_message.text, self.input_key.text), self.input_key.text)
            if S_block_var.state == 'down':
                self.output_message.text = S_блок_замены.encryption(self.input_message.text)



        def decryption(instance):
            str = ''
            if АТБАШ_var.state == 'down':
                self.output_message.text = АТБАШ.decryption(self.input_message.text, str)
            if Квадрат_Полибия_var.state == 'down':
                self.output_message.text = Квадрат_Полибия.decryption(self.input_message.text)
            if Шифр_Цезаря_var.state == 'down':
                if self.input_key.text == '':
                    self.button_decryption.disabled
                else:
                    calculation = Шифр_Цезаря.validate(self.input_message.text, self.input_key.text, False)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if Шифр_Тритемия_var.state == 'down':
                self.output_message.text = Шифр_Тритемия.decryption(self.input_message.text)
            if Шифр_Виженера_var.state == 'down':
                if self.input_key.text == '':
                    self.button_decryption.disabled
                else:
                    calculation = Шифр_Виженера.validate(self.input_message.text, self.input_key.text, False)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if Шифр_Белазо_var.state == 'down':
                if self.input_key.text == '':
                    self.button_decryption.disabled
                else:
                    calculation = Шифр_Белазо.validate(self.input_message.text, self.input_key.text, False)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if Матричный_шифр_var.state == 'down':
                if self.input_key.text == '':
                    self.button_decryption.disabled
                else:
                    if Матричный_шифр.matrix_check(Матричный_шифр.key_generation(Матричный_шифр.key_to_array(self.input_key.text))) == 'Введенный ключ не подходит для шифрования, введите другой.':
                        self.output_message.text = 'Введенный ключ не подходит для шифрования, введите другой.'
                    else:
                        self.output_message.text = Матричный_шифр.decryption(Матричный_шифр.message_to_vector(Матричный_шифр.str_to_list(self.input_message.text),  Матричный_шифр.key_to_array(self.input_key.text)), Матричный_шифр.key_generation(Матричный_шифр.key_to_array(self.input_key.text)))
            if Решетка_Кардано_var.state == 'down':
                if self.input_key.text == '':
                    self.button_decryption.disabled
                else:
                    self.output_message.text = Решетка_Кардано.decryption(self.input_message.text, self.input_key.text)
            if Перестановка_var.state == 'down':
                if self.input_key.text == '':
                    self.button_decryption.disabled
                else:
                    self.output_message.text = Вертикальная_перестановка.decryption(Вертикальная_перестановка.message_to_vector_dec(Вертикальная_перестановка.vector_initialization(self.input_message.text, self.input_key.text), self.input_message.text, self.input_key.text), self.input_key.text)
            if Шифр_Плэйфера_var.state == 'down':
                if self.input_key.text == '':
                    self.button_decryption.disabled
                else:
                    self.output_message.text = Шифр_Плэйфера.decryption(self.input_message.text, self.input_key.text)
            if S_block_var.state == 'down':
                self.output_message.text = S_блок_замены.decryption(self.input_message.text)


        def choice_АТБАШ(instance):
            self.input_key.hint_text = 'Бесключевой криптографический алгоритм'

        def choice_Квадрат_Полибия(instance):
            self.input_key.hint_text = 'Бесключевой криптографический алгоритм'

        def choice_Шифр_Цезаря(instance):
            self.input_key.hint_text = 'Введите целое число от -1114 до 1114'

        def choice_Шифр_Тритемия(instance):
            self.input_key.hint_text = 'Бесключевой криптографический алгоритм'

        def choice_Шифр_Белазо(instance):
            self.input_key.hint_text = 'Введите любую последовательность символов'

        def choice_Шифр_Виженера(instance):
            self.input_key.hint_text = 'Введите любой символ'

        def choice_S_block(instance):
            self.input_key.hint_text = 'Бесключевой криптографический алгоритм'



        АТБАШ_var.bind(on_press=choice_АТБАШ)
        Квадрат_Полибия_var.bind(on_press=choice_Квадрат_Полибия)
        Шифр_Цезаря_var.bind(on_press=choice_Шифр_Цезаря)
        Шифр_Тритемия_var.bind(on_press=choice_Шифр_Тритемия)
        Шифр_Белазо_var.bind(on_press=choice_Шифр_Белазо)
        Шифр_Виженера_var.bind(on_press=choice_Шифр_Виженера)
        S_block_var.bind(on_press=choice_S_block)



        self.button_encryption.bind(on_press=encryption)
        self.button_decryption.bind(on_press=decryption)
        self.layout_array_cipher.bind(minimum_width=self.layout_array_cipher.setter('width'))


        return self.form


if __name__ == '__main__':
    Interface().run()


