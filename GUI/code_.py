# -*- coding: utf-8 -*-
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
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
import Одноразовый_блокнот_Шеннона
import ГОСТ_28147_89
import A5_1
import A5_2
import AES
import Магма
import Кузнечик
import RSA_DS
import Elgamal_DS
import ГОСТ_34_10_94
import ГОСТ_34_10_2012
import RSA_cipher
import Elgamal_cipher
import ECC
import DiffieHellman

Window.size = (900, 410)
Window.clearcolor = (1, 1, 1, 0)
cipher_array = {'АТБАШ_var': '  АТБАШ  ', 'Квадрат_Полибия_var': 'Квадрат Полибия', 'Шифр_Цезаря_var': 'Шифр Цезаря', 'Шифр_Тритемия_var': 'Шифр Тритемия', 'Шифр_Белазо_var': 'Шифр Белазо', 'Шифр_Виженера_var': 'Шифр Виженера', 'S_block_var': 'S-блок замены', 'Матричный_шифр_var': 'Матричный шифр', 'Шифр_Плэйфера_var': 'Шифр Плэйфера', 'Перестановка_var': ' Перестановка', 'Решетка_Кардано_var': 'Решетка Кардано', 'Блокнот_Шеннона_var': 'Блокнот Шеннона', 'ГОСТ_28147_89_var': 'ГОСТ 28147-89', 'A5_1_var': ' A5/1 ', 'A5_2_var': ' A5/2 ', 'AES_var': ' AES ', 'Магма_var': ' Магма ', 'Кузнечик_var': 'Кузнечик', 'RSA_DS_var': 'RSA DS', 'Elgamal_DS_var': 'Elgamal DS', 'ГОСТ_34_10_94_var': 'ГОСТ 34.10-94', 'ГОСТ_34_10_2012_var': 'ГОСТ 34.10-2012', 'RSA_cipher_var': ' RSA ', 'Elgamal_cipher_var': 'Elgamal', 'ECC_var': ' ECC ', 'DiffieHellman_var': 'Протокол Диффи — Хеллмана'}

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
            globals()[cipher] = ToggleButton(group='group', text=cipher_array[cipher], size_hint_x=None, height=40, color=(0, 0, 0), font_size=13, width=len(cipher_array[cipher]) * 10, background_normal='')
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

        def show_enc(instance):
            if АТБАШ_var.state == 'down':
                self.output_message.text = АТБАШ.enc_dec(self.input_message.text)
            if Квадрат_Полибия_var.state == 'down':
                self.output_message.text = Квадрат_Полибия.encryption(self.input_message.text)
            if Шифр_Цезаря_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_encryption.disabled
                else:
                    calculation = Шифр_Цезаря.validate(self.input_message.text, self.input_key.text, True)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if Шифр_Тритемия_var.state == 'down':
                self.output_message.text = Шифр_Тритемия.encryption(self.input_message.text)
            if Шифр_Виженера_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_encryption.disabled
                else:
                    calculation = Шифр_Виженера.validate(self.input_message.text, self.input_key.text, True)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if Шифр_Белазо_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_encryption.disabled
                else:
                    calculation = Шифр_Белазо.validate(self.input_message.text, self.input_key.text, True)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if Матричный_шифр_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_encryption.disabled
                else:
                    self.output_message.text = Матричный_шифр.matrix_check(self.input_message.text, self.input_key.text, True)
            if Решетка_Кардано_var.state == 'down':
                Решетка_Кардано_сообщение_ключ = Решетка_Кардано.encryption(self.input_message.text)
                self.output_message.text = Решетка_Кардано_сообщение_ключ[0]
                self.input_key.text = Решетка_Кардано_сообщение_ключ[1]
            if Перестановка_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_encryption.disabled
                else:
                    self.output_message.text = Вертикальная_перестановка.encryption(Вертикальная_перестановка.message_to_vector_enc(Вертикальная_перестановка.vector_initialization(self.input_message.text, self.input_key.text), self.input_message.text, self.input_key.text), self.input_key.text)
            if Шифр_Плэйфера_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_encryption.disabled
                else:
                    calculation = Шифр_Плэйфера.validate(self.input_message.text, self.input_key.text, True)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if S_block_var.state == 'down':
                self.output_message.text = S_блок_замены.encryption(self.input_message.text)
            if Блокнот_Шеннона_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_encryption.disabled
                else:
                    self.output_message.text = Одноразовый_блокнот_Шеннона.encryption(self.input_message.text, self.input_key.text)
            if ГОСТ_28147_89_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_encryption.disabled
                else:
                    calculation = ГОСТ_28147_89.encryption_decryption(self.input_message.text, self.input_key.text, True)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if A5_1_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_encryption.disabled
                else:
                    calculation = A5_1.bin_to_hex(self.input_message.text, self.input_key.text)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if A5_2_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_encryption.disabled
                else:
                    calculation = A5_2.bin_to_hex(self.input_message.text, self.input_key.text)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if AES_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_encryption.disabled
                else:
                    calculation = AES.encryption(self.input_message.text, self.input_key.text)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if Магма_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_encryption.disabled
                else:
                    calculation = Магма.encryption(self.input_message.text, self.input_key.text)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if Кузнечик_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_encryption.disabled
                else:
                    calculation = Кузнечик.encryption(self.input_message.text, self.input_key.text)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if RSA_DS_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_encryption.disabled
                else:
                    self.output_message.text = RSA_DS.generation_signature(self.input_message.text, self.input_key.text)
            if Elgamal_DS_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_encryption.disabled
                else:
                    self.output_message.text = Elgamal_DS.generation_signature(self.input_message.text, self.input_key.text)
            if ГОСТ_34_10_94_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_encryption.disabled
                else:
                    self.output_message.text = ГОСТ_34_10_94.generation_signature(self.input_message.text, self.input_key.text)
            if ГОСТ_34_10_2012_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_encryption.disabled
                else:
                    self.output_message.text = ГОСТ_34_10_2012.generation_signature(self.input_message.text, self.input_key.text)
            if RSA_cipher_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    self.output_message.text = RSA_cipher.encryption(self.input_message.text, self.input_key.text)
            if Elgamal_cipher_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_encryption.disabled
                else:
                    self.output_message.text = Elgamal_cipher.encryption(self.input_message.text, self.input_key.text)
            if ECC_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_encryption.disabled
                else:
                    self.output_message.text = ECC.encryption(self.input_message.text, self.input_key.text)
            if DiffieHellman_var.state == 'down':
                if self.input_key.text == '':
                    self.button_encryption.disabled
                else:
                    self.output_message.text = DiffieHellman.key_exchange(self.input_key.text)


        def show_dec(instance):
            if АТБАШ_var.state == 'down':
                self.output_message.text = АТБАШ.enc_dec(self.input_message.text)
            if Квадрат_Полибия_var.state == 'down':
                self.output_message.text = Квадрат_Полибия.decryption(self.input_message.text)
            if Шифр_Цезаря_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    calculation = Шифр_Цезаря.validate(self.input_message.text, self.input_key.text, False)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if Шифр_Тритемия_var.state == 'down':
                self.output_message.text = Шифр_Тритемия.decryption(self.input_message.text)
            if Шифр_Виженера_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    calculation = Шифр_Виженера.validate(self.input_message.text, self.input_key.text, False)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if Шифр_Белазо_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    calculation = Шифр_Белазо.validate(self.input_message.text, self.input_key.text, False)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if Матричный_шифр_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    self.output_message.text = Матричный_шифр.matrix_check(self.input_message.text, self.input_key.text, False)
            if Решетка_Кардано_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    self.output_message.text = Решетка_Кардано.decryption(self.input_message.text, self.input_key.text)
            if Перестановка_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    self.output_message.text = Вертикальная_перестановка.decryption(Вертикальная_перестановка.message_to_vector_dec(Вертикальная_перестановка.vector_initialization(self.input_message.text, self.input_key.text), self.input_message.text, self.input_key.text), self.input_key.text)
            if Шифр_Плэйфера_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    calculation = Шифр_Плэйфера.validate(self.input_message.text, self.input_key.text, False)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if S_block_var.state == 'down':
                self.output_message.text = S_блок_замены.decryption(self.input_message.text)
            if Блокнот_Шеннона_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    self.output_message.text = Одноразовый_блокнот_Шеннона.decryption(self.input_message.text, self.input_key.text)
            if ГОСТ_28147_89_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    calculation = ГОСТ_28147_89.encryption_decryption(self.input_message.text, self.input_key.text, False)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if A5_1_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    calculation = A5_1.bin_to_message(self.input_message.text, self.input_key.text)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if A5_2_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    calculation = A5_2.bin_to_message(self.input_message.text, self.input_key.text)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if AES_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    calculation = AES.decryption(self.input_message.text, self.input_key.text)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if Магма_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    calculation = Магма.decryption(self.input_message.text, self.input_key.text)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if Кузнечик_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    calculation = Кузнечик.decryption(self.input_message.text, self.input_key.text)
                    self.output_message.text = calculation[0]
                    self.input_key.text = calculation[1]
            if RSA_DS_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    self.output_message.text = RSA_DS.signature_verification(self.input_message.text, self.input_key.text)
            if Elgamal_DS_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    self.output_message.text = Elgamal_DS.signature_verification(self.input_message.text, self.input_key.text)
            if ГОСТ_34_10_94_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    self.output_message.text = ГОСТ_34_10_94.signature_verification(self.input_message.text, self.input_key.text)
            if ГОСТ_34_10_2012_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    self.output_message.text = ГОСТ_34_10_2012.signature_verification(self.input_message.text, self.input_key.text)
            if RSA_cipher_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    self.output_message.text = RSA_cipher.decryption(self.input_message.text, self.input_key.text)
            if Elgamal_cipher_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_dencryption.disabled
                else:
                    self.output_message.text = Elgamal_cipher.decryption(self.input_message.text, self.input_key.text)
            if ECC_var.state == 'down':
                if self.input_key.text == '' or self.input_message.text == '':
                    self.button_decryption.disabled
                else:
                    self.output_message.text = ECC.decryption(self.input_message.text, self.input_key.text)


        def choice_АТБАШ(instance):
            self.input_key.hint_text = 'Бесключевой криптографический алгоритм'
            choice_cipher(instance)

        def choice_Квадрат_Полибия(instance):
            self.input_key.hint_text = 'Бесключевой криптографический алгоритм'
            choice_cipher(instance)

        def choice_Шифр_Цезаря(instance):
            self.input_key.hint_text = 'Введите целое число от -1114 до 1114'
            choice_cipher(instance)

        def choice_Шифр_Тритемия(instance):
            self.input_key.hint_text = 'Бесключевой криптографический алгоритм'
            choice_cipher(instance)

        def choice_Шифр_Белазо(instance):
            self.input_key.hint_text = 'Введите любую последовательность символов'
            choice_cipher(instance)

        def choice_Шифр_Виженера(instance):
            self.input_key.hint_text = 'Введите любой символ'
            choice_cipher(instance)

        def choice_S_block(instance):
            self.input_key.hint_text = 'Бесключевой криптографический алгоритм'
            choice_cipher(instance)

        def choice_Матричный_шифр(instance):
            self.input_key.hint_text = 'Введите размерность ключа и его элементы через пробел'
            choice_cipher(instance)

        def choice_Вертикальная_перестановка(instance):
            self.input_key.hint_text = 'Введите любую последовательность нулей и единиц'
            choice_cipher(instance)

        def choice_Решетка_Кардано(instance):
            self.input_key.hint_text = 'Введите числа через пробел. Ключ необходим только при расшифровании'
            choice_cipher(instance)

        def choice_Блокнот_Шеннона(instance):
            self.input_key.hint_text = 'Введите а (mod 4 = 1) и с (нечётное), а также порождающую величину T0'
            choice_cipher(instance)

        def choice_ГОСТ_28147_89(instance):
            self.input_key.hint_text = 'Введите последовательность символов длиной 20'
            choice_cipher(instance)

        def choice_Плейфер(instance):
            self.input_key.hint_text = 'Введите любую последовательность символов'
            choice_cipher(instance)

        def choice_A5_1(instance):
            self.input_key.hint_text = 'Введите последовательность символов длиной 4'
            choice_cipher(instance)

        def choice_A5_2(instance):
            self.input_key.hint_text = 'Введите последовательность символов длиной 6'
            choice_cipher(instance)

        def choice_AES(instance):
            self.input_key.hint_text = 'Введите последовательность символов длиной 8'
            choice_cipher(instance)

        def choice_Магма(instance):
            self.input_key.hint_text = 'Введите последовательность символов длиной 16'
            choice_cipher(instance)

        def choice_Кузнечик(instance):
            self.input_key.hint_text = 'Введите последовательность символов длиной 9'
            choice_cipher(instance)

        def choice_RSA_DS(instance):
            self.input_key.hint_text = 'Введите два простых числа, для проверки - значение подписи и параметры E и N'
            choice_DS(instance)

        def choice_Elgamal_DS(instance):
            self.input_key.hint_text = 'Введите простое P, G (1; P) и X (1; P-1), для проверки - подпись и параметры Y, G, P'
            choice_DS(instance)

        def choice_ГОСТ_34_10_94(instance):
            self.input_key.hint_text = 'Введите простое число (>22), для проверки - подпись и параметры p (простое), q, a и y'
            choice_DS(instance)

        def choice_ГОСТ_34_10_2012(instance):
            self.input_key.hint_text = 'Введите открытый ключ и рандомизатор, для проверки - подпись, закрытый ключ, a, p, q, G '
            choice_DS(instance)

        def choice_RSA_cipher(instance):
            self.input_key.hint_text = 'Введите два простых числа, для расшифрования - параметры D и N'
            choice_cipher(instance)

        def choice_Elgamal_cipher(instance):
            self.input_key.hint_text = 'Введите простое P (> 8500), G (1; P) и X (1; P), для расшифрования - параметры X и P'
            choice_cipher(instance)

        def choice_ECC(instance):
            self.input_key.hint_text = 'Введите закрытый ключ (< 65537)'
            choice_cipher(instance)

        def choice_DiffieHellman(instance):
            self.input_key.hint_text = 'Введите n, a (< n) и секретый ключ (< n)'
            choice_cipher(instance)

            self.button_encryption.text = 'Обменяться ключами'
            self.button_decryption.disabled = True


        def choice_cipher(instance):
            self.button_encryption.text = 'Зашифровать'
            self.button_decryption.text = 'Расшифровать'

            self.label_input_key.text = 'Введите ключи через пробел'
            self.label_input_key.pos = (47, 211)

            self.label_output.text = 'Результат преобразования'
            self.label_output.pos = (40, 125)
            self.button_decryption.disabled = False


        def choice_DS(instance):
            self.button_encryption.text = 'Генерация'
            self.button_decryption.text = 'Проверка'

            self.label_input_key.text = 'Введите параметры цифровой подписи и само значение подписи для проверки'
            self.label_input_key.pos = (200, 211)

            self.label_output.text = 'Значение подписи или результат проверки'
            self.label_output.pos = (88, 125)
            self.button_decryption.disabled = False



        АТБАШ_var.bind(on_press=choice_АТБАШ)
        Квадрат_Полибия_var.bind(on_press=choice_Квадрат_Полибия)
        Шифр_Цезаря_var.bind(on_press=choice_Шифр_Цезаря)
        Шифр_Тритемия_var.bind(on_press=choice_Шифр_Тритемия)
        Шифр_Белазо_var.bind(on_press=choice_Шифр_Белазо)
        Шифр_Виженера_var.bind(on_press=choice_Шифр_Виженера)
        S_block_var.bind(on_press=choice_S_block)
        Матричный_шифр_var.bind(on_press=choice_Матричный_шифр)
        Перестановка_var.bind(on_press=choice_Вертикальная_перестановка)
        Шифр_Плэйфера_var.bind(on_press=choice_Плейфер)
        Решетка_Кардано_var.bind(on_press=choice_Решетка_Кардано)
        Блокнот_Шеннона_var.bind(on_press=choice_Блокнот_Шеннона)
        ГОСТ_28147_89_var.bind(on_press=choice_ГОСТ_28147_89)
        A5_1_var.bind(on_press=choice_A5_1)
        A5_2_var.bind(on_press=choice_A5_2)
        AES_var.bind(on_press=choice_AES)
        Магма_var.bind(on_press=choice_Магма)
        Кузнечик_var.bind(on_press=choice_Кузнечик)
        RSA_DS_var.bind(on_press=choice_RSA_DS)
        Elgamal_DS_var.bind(on_press=choice_Elgamal_DS)
        ГОСТ_34_10_94_var.bind(on_press=choice_ГОСТ_34_10_94)
        ГОСТ_34_10_2012_var.bind(on_press=choice_ГОСТ_34_10_2012)
        RSA_cipher_var.bind(on_press=choice_RSA_cipher)
        Elgamal_cipher_var.bind(on_press=choice_Elgamal_cipher)
        ECC_var.bind(on_press=choice_ECC)
        DiffieHellman_var.bind(on_press=choice_DiffieHellman)

        self.button_encryption.bind(on_press=show_enc)
        self.button_decryption.bind(on_press=show_dec)
        self.layout_array_cipher.bind(minimum_width=self.layout_array_cipher.setter('width'))


        return self.form


if __name__ == '__main__':
    Interface().run()


