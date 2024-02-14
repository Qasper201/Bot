import asyncio
import logging
import random
import config

from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder


logging.basicConfig(level=logging.INFO)
bot = Bot(token="6555614063:AAGatIRDW558XJpHl47jJXjnKEyv0lJ6vrQ")
dp = Dispatcher()



cinemas = {"Мультіплекс","Планета кіно","Магнат"}



kb1 = [
    [KeyboardButton(text="Баланс карти")],
    [KeyboardButton(text="Поповнити карту")],
    [KeyboardButton(text="Афіша кіно на сьогодні")],
    [KeyboardButton(text="Купити білет")],
    [KeyboardButton(text="Попкорн та його вартість")],
    [KeyboardButton(text="Купити попкорн")],
    [KeyboardButton(text="Напої та їх вартість")],
    [KeyboardButton(text="Купити напій")],
    [KeyboardButton(text="Адреси наших кінотеатрів")],
    [KeyboardButton(text="Розробники цього бота")],
    [KeyboardButton(text="Підтримати розробників бота")]
]
keyboard1 = ReplyKeyboardMarkup(keyboard=kb1)





kb = [
    [KeyboardButton(text="Мультіплекс"), KeyboardButton(text="Планета кіно"), KeyboardButton(text="Магнат")]]
keyboard = ReplyKeyboardMarkup(keyboard=kb)



@dp.message(Command("start"))
async def send_random_value(message: types.Message):
    with open("result.txt", "a") as file:
        file.write(f"_______________________________\n")
        file.write(f"Time: {datetime.now()}\n")
        file.write(f"ChatID: {message.chat.id}\n")
        file.write(f"Name: {message.chat.first_name}\n")
        file.write(f"Last name: {message.chat.last_name}\n")
        file.write(f"Full name: {message.chat.full_name}\n")
    await message.answer("Привіт, я твій бот для кіно. Обери кінотеатр, в який ти би хотів піти.", reply_markup=keyboard)



@dp.message(F.text.in_(cinemas))
async def cmd_answer(message: types.Message):
    with open("кінотеатр.txt","w") as file:
        file.write(message.text)
    await message.answer(f"Дякую що обрали кінотеатр {message.text.title()}, сподіваюсь вам сподобається)", reply_markup =keyboard1)






with open("кінотеатр.txt","r") as file:
    cought_cinema = file.read()



if cought_cinema == "Мультіплекс":

    @dp.message(F.text == "Купити білет")
    async def cmd_answer(message: types.Message):
        buttons1 = [
            [
                InlineKeyboardButton(text="На фільм Інтерстеллар (230 грн)", callback_data="num_decr")
            ],
            [
                InlineKeyboardButton(text="На фільм Паразити (200 грн)", callback_data="num_incr")
            ],
            [
                InlineKeyboardButton(text="На фільм Недоторканні (210 грн)", callback_data="num_decе")
            ],
            [
                InlineKeyboardButton(text="На фільм Найкращий стрілець: Маверік (220 грн)", callback_data="num_decь")
            ],
            [
                InlineKeyboardButton(text="На фільм Шалений Макс: Дорога гніву (170 грн)", callback_data="num_decа")
            ],
            [
                InlineKeyboardButton(text="На фільм У центрі уваги (190 грн)", callback_data="num_decі")
            ],
            [
                InlineKeyboardButton(text="На фільм Аутсайдери (150 грн)", callback_data="num_decш")
            ],
        ]

        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons1)

        await message.answer(
            "Оберіть фільм, на який ви хочете придбати квиток",
            reply_markup=keyboard)


    @dp.callback_query(F.data == "num_decr")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 230:

            number -= 230
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Інтерстеллар за 230 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")


    @dp.callback_query(F.data == "num_incr")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 200:

            number -= 200
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Паразити за 200 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "num_decе")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 210:

            number -= 210
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Недоторканні за 210 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "num_decь")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 220:

            number -= 220
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Найкращий стрілець: Маверік за 220 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "num_decа")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 170:

            number -= 170
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Шалений Макс: Дорога гніву за 170 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "num_decі")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 190:

            number -= 190
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм У центрі уваги за 190 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "num_decш")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 150:

            number -= 150
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Аутсайдери за 150 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")



    @dp.message(F.text == "Афіша кіно на сьогодні")
    async def cmd_answer(message: types.Message):
        await message.answer("""
Інтерстеллар - 14:20
Паразити - 15:20
Недоторканні - 18:30
Найкращий  стрілець: Маверік - 17:40
Шалений Макс: Дорога гніву - 20:00
У центрі уваги - 16:40
Аутсайдери - 21:30
""")





    @dp.message(F.text == "Попкорн та його вартість")
    async def cmd_answer(message: types.Message):
        await message.answer("""
Карамельний маленький - 60грн    середній - 100грн    великий - 150грн\n
З беконом маленький - 70грн    середній - 120грн    великий - 180грн\n
Сирний маленький - 65грн    середній - 100грн    великий - 170грн\n
Шоколадний маленький - 75грн    середній - 105грн    великий - 165грн
""")


    @dp.message(F.text == "Напої та їх вартість")
    async def cmd_answer(message: types.Message):
        await message.answer("""
Пепсі: 0.3л - 25грн    0.4л - 35грн    0.5л - 50грн\n
Фанта: 0.3л - 25грн    0.4л - 40грн    0.5л - 55грн\n
Спрайт: 0.3л - 30грн    0.4л - 40грн    0.5л - 60грн\n
Вода негазована: 0.5л - 40грн    1л - 70грн\n
Вода газована: 0.5л - 45грн    1л - 75грн
""")


    @dp.message(F.text == "Купити напій")
    async def cmd_answer(message: types.Message):
        buttons2 = [
            [
                InlineKeyboardButton(text="Пепсі 0.3л (25 грн)", callback_data="а")
            ],
            [
                InlineKeyboardButton(text="Пепсі 0.4л (35 грн)", callback_data="б")
            ],
            [
                InlineKeyboardButton(text="Пепсі 0.5л (50 грн)", callback_data="в")
            ],
            [
                InlineKeyboardButton(text="Фанта 0.3л (25 грн)", callback_data="г")
            ],
            [
                InlineKeyboardButton(text="Фанта 0.4л (40 грн)", callback_data="д")
            ],
            [
                InlineKeyboardButton(text="Фанта 0.5л (55 грн)", callback_data="е")
            ],
            [
                InlineKeyboardButton(text="Спрайт 0.3л (30 грн)", callback_data="є")
            ],
            [
                InlineKeyboardButton(text="Спрайт 0.4л (40 грн)", callback_data="ж")
            ],
            [
                InlineKeyboardButton(text="Спрайт 0.5л (60 грн)", callback_data="з")
            ],
            [
                InlineKeyboardButton(text="Вода негазована 0.5л (40 грн)", callback_data="и")
            ],
            [
                InlineKeyboardButton(text="Вода негазована 1л (70 грн)", callback_data="і")
            ],
            [
                InlineKeyboardButton(text="Вода газована 0.5л (45 грн)", callback_data="ї")
            ],
            [
                InlineKeyboardButton(text="Вода газована 1л (75 грн)", callback_data="й")
            ],
        ]

        kb = InlineKeyboardMarkup(inline_keyboard=buttons2)

        await message.answer(
            "Виберіть напій, який ви хочете купити",
            reply_markup=kb)


    @dp.callback_query(F.data == "а")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 25:

            number -= 25
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили пепсі 0.3л за 25 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "б")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 35:

            number -= 35
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили пепсі 0.4л за 35 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "в")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 50:

            number -= 50
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили пепсі 0.5л за 50 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "г")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 25:

            number -= 25
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили фанту 0.3л за 25 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "д")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 40:

            number -= 40
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили фанту 0.4л за 40 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "е")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 55:

            number -= 55
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили фанту 0.5л за 55 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "є")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 30:

            number -= 30
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили спрайт 0.3л за 30 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "ж")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 40:

            number -= 40
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили спрайт 0.4л за 40 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "з")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 60:

            number -= 60
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили спрайт 0.5л за 60 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "и")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 40:

            number -= 40
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили негазовану воду 0.5л за 40 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "і")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 70:

            number -= 70
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили негазовану воду 1л за 70 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "ї")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 45:

            number -= 45
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили газовану воду 0.5л за 45 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "й")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 75:

            number -= 75
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили газовану воду 1л за 75 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")




    @dp.message(F.text == "Купити попкорн")
    async def cmd_answer(message: types.Message):
        buttons2 = [
            [
                InlineKeyboardButton(text="карамельний маленький (60 грн)", callback_data="a")
            ],
            [
                InlineKeyboardButton(text="карамельний середній (100 грн)", callback_data="b")
            ],
            [
                InlineKeyboardButton(text="карамельний великий (150 грн)", callback_data="c")
            ],
            [
                InlineKeyboardButton(text="з беконом маленький (70 грн)", callback_data="d")
            ],
            [
                InlineKeyboardButton(text="з беконом середній (120 грн)", callback_data="e")
            ],
            [
                InlineKeyboardButton(text="з беконом великий (180 грн)", callback_data="f")
            ],
            [
                InlineKeyboardButton(text="сирний маленький (65 грн)", callback_data="g")
            ],
            [
                InlineKeyboardButton(text="сирний середній (100 грн)", callback_data="h")
            ],
            [
                InlineKeyboardButton(text="сирний великий (170 грн)", callback_data="i")
            ],
            [
                InlineKeyboardButton(text="шоколадний маленький (75 грн)", callback_data="j")
            ],
            [
                InlineKeyboardButton(text="шоколадний середній (105 грн)", callback_data="k")
            ],
            [
                InlineKeyboardButton(text="шоколадний великий (165 грн)", callback_data="l")
            ],
        ]

        kb = InlineKeyboardMarkup(inline_keyboard=buttons2)

        await message.answer(
            "Виберіть попкорн, який ви хочете купити",
            reply_markup=kb)


    @dp.callback_query(F.data == "a")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 60:

            number -= 60
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький попкорн зі смаком карамелі за 60 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "b")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 100:

            number -= 100
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній попкорн зі смаком карамелі за 100 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "c")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 150:

            number -= 150
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великий попкорн зі смаком карамелі за 150 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "d")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 70:

            number -= 70
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький попкорн зі смаком бекону за 70 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "e")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 120:

            number -= 120
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній попкорн зі смаком бекону за 120 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "f")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 180:

            number -= 180
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великий попкорн зі смаком бекону за 180 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "g")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 65:

            number -= 65
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький попкорн зі смаком сиру за 65 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "h")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 100:

            number -= 100
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній попкорн зі смаком сиру за 100 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "i")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 170:

            number -= 170
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великий попкорн зі смаком сиру за 170 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "j")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 75:

            number -= 75
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький попкорн зі смаком шоколаду за 75 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "k")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 105:

            number -= 105
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній попкорн зі смаком шоколаду за 105 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "l")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 165:

            number -= 165
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великий попкорн зі смаком шоколаду за 165 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")






if cought_cinema == "Планета кіно":

    @dp.message(F.text == "Купити білет")
    async def cmd_answer(message: types.Message):
        buttons2 = [
            [
                InlineKeyboardButton(text="На фільм Довга доба (140 грн)", callback_data="ewd")
            ],
            [
                InlineKeyboardButton(text="На фільм Хижа ніч (205 грн)", callback_data="пмвупц")
            ],
            [
                InlineKeyboardButton(text="На фільм Дюна (255 грн)", callback_data="пвапіуафі")
            ],
            [
                InlineKeyboardButton(text="На фільм Смак пристрасті (190 грн)", callback_data="тапряврикаіп")
            ],
            [
                InlineKeyboardButton(text="На фільм Уроки толерантності (170 грн)", callback_data="лбдшщшгпдшг")
            ],
            [
                InlineKeyboardButton(text="На фільм Мадам Павутина (240 грн)", callback_data="блсрпчрвяпв")
            ],
            [
                InlineKeyboardButton(text="На фільм Керол (235 грн)", callback_data="риепікфупнолш")
            ],
        ]

        keyboard2 = InlineKeyboardMarkup(inline_keyboard=buttons2)

        await message.answer(
            "Оберіть фільм, на який ви хочете придбати квиток",
            reply_markup=keyboard2)


    @dp.callback_query(F.data == "ewd")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 140:

            number -= 140
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Довга доба за 140 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")


    @dp.callback_query(F.data == "пмвупц")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 205:

            number -= 205
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer(
                "Ви купили білет на фільм Хижа ніч за 205 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "пвапіуафі")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 255:

            number -= 255
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Дюна за 255 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "тапряврикаіп")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 190:

            number -= 190
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Смак пристрасті за 190 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "лбдшщшгпдшг")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 170:

            number -= 170
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Уроки толерантності за 170 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "блсрпчрвяпв")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 240:

            number -= 240
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Мадам Павутина за 240 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "риепікфупнолш")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 235:

            number -= 235
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Керол за 250 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")



    @dp.message(F.text == "Афіша кіно на сьогодні")
    async def cmd_answer(message: types.Message):
        await message.answer("""
Довга доба - 13:50
Хижа ніч - 14:40
Дюна - 17:30
Смак пристрасті - 18:40
Уроки толерантності - 20:15
Мадам Павутина - 21:20
Керол - 22:50
""")





    @dp.message(F.text == "Попкорн та його вартість")
    async def cmd_answer(message: types.Message):
        await message.answer("""
Карамельний маленький - 70грн    середній - 105грн    великий - 170грн\n
З беконом маленький - 75грн    середній - 130грн    великий - 190грн\n
Сирний маленький - 55грн    середній - 105грн    великий - 175грн\n
Шоколадний маленький - 80грн    середній - 120грн    великий - 185грн
""")


    @dp.message(F.text == "Напої та їх вартість")
    async def cmd_answer(message: types.Message):
        await message.answer("""
Пепсі: 0.3л - 23грн    0.4л - 37грн    0.5л - 55грн\n
Фанта: 0.3л - 20грн    0.4л - 42грн    0.5л - 52грн\n
Спрайт: 0.3л - 26грн    0.4л - 37грн    0.5л - 55грн\n
Вода негазована: 0.5л - 45грн    1л - 90грн\n
Вода газована: 0.5л - 50грн    1л - 85грн
""")


    @dp.message(F.text == "Купити напій")
    async def cmd_answer(message: types.Message):
        buttons2 = [
            [
                InlineKeyboardButton(text="Пепсі 0.3л (23 грн)", callback_data="ьевчрыекп")
            ],
            [
                InlineKeyboardButton(text="Пепсі 0.4л (37 грн)", callback_data="пмлвпьоукта")
            ],
            [
                InlineKeyboardButton(text="Пепсі 0.5л (55 грн)", callback_data="алкацоугшашц")
            ],
            [
                InlineKeyboardButton(text="Фанта 0.3л (20 грн)", callback_data="ыцзйывуоаткрип")
            ],
            [
                InlineKeyboardButton(text="Фанта 0.4л (42 грн)", callback_data="зцувдцвл")
            ],
            [
                InlineKeyboardButton(text="Фанта 0.5л (52 грн)", callback_data="увщулврцрвуц")
            ],
            [
                InlineKeyboardButton(text="Спрайт 0.3л (26 грн)", callback_data="члфщзылцвр")
            ],
            [
                InlineKeyboardButton(text="Спрайт 0.4л (37 грн)", callback_data="цзвдуцщаовмт")
            ],
            [
                InlineKeyboardButton(text="Спрайт 0.5л (55 грн)", callback_data="йцзвдушататм")
            ],
            [
                InlineKeyboardButton(text="Вода негазована 0.5л (45 грн)", callback_data="щывлшлурарми")
            ],
            [
                InlineKeyboardButton(text="Вода негазована 1л (90 грн)", callback_data="хзкпдщерплтпе")
            ],
            [
                InlineKeyboardButton(text="Вода газована 0.5л (50 грн)", callback_data="дуащлкапрри")
            ],
            [
                InlineKeyboardButton(text="Вода газована 1л (85 грн)", callback_data="зерлшеткпкотп")
            ],
        ]

        kb = InlineKeyboardMarkup(inline_keyboard=buttons2)

        await message.answer(
            "Виберіть напій, який ви хочете купити",
            reply_markup=kb)


    @dp.callback_query(F.data == "ьевчрыекп")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 23:

            number -= 23
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили пепсі 0.3л за 23 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "пмлвпьоукта")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 37:

            number -= 37
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили пепсі 0.4л за 37 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "алкацоугшашц")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 55:

            number -= 55
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили пепсі 0.5л за 55 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "ыцзйывуоаткрип")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 20:

            number -= 20
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили фанту 0.3л за 20 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "зцувдцвл")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 42:

            number -= 42
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили фанту 0.4л за 42 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "увщулврцрвуц")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 52:

            number -= 52
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили фанту 0.5л за 52 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "члфщзылцвр")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 26:

            number -= 26
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили спрайт 0.3л за 30 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "цзвдуцщаовмт")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 37:

            number -= 37
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили спрайт 0.4л за 37 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "йцзвдушататм")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 55:

            number -= 55
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили спрайт 0.5л за 55 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "щывлшлурарми")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 45:

            number -= 45
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили негазовану воду 0.5л за 45 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "хзкпдщерплтпе")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 90:

            number -= 90
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили негазовану воду 1л за 90 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "дуащлкапрри")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 50:

            number -= 50
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили газовану воду 0.5л за 50 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "зерлшеткпкотп")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 85:

            number -= 85
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили газовану воду 1л за 85 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")




    @dp.message(F.text == "Купити попкорн")
    async def cmd_answer(message: types.Message):
        buttons2 = [
            [
                InlineKeyboardButton(text="карамельний маленький (70 грн)", callback_data="щртлшкатута")
            ],
            [
                InlineKeyboardButton(text="карамельний середній (105 грн)", callback_data="запмлушврй")
            ],
            [
                InlineKeyboardButton(text="карамельний великий (170 грн)", callback_data="азулашцруйн")
            ],
            [
                InlineKeyboardButton(text="з беконом маленький (75 грн)", callback_data="зклацшвуйгру")
            ],
            [
                InlineKeyboardButton(text="з беконом середній (130 грн)", callback_data="мзукалцшврйнп")
            ],
            [
                InlineKeyboardButton(text="з беконом великий (190 грн)", callback_data="азцдвцшоагурап")
            ],
            [
                InlineKeyboardButton(text="сирний маленький (55 грн)", callback_data="цхавдуаоктпотами")
            ],
            [
                InlineKeyboardButton(text="сирний середній (105 грн)", callback_data="звйлвацшраврикм")
            ],
            [
                InlineKeyboardButton(text="сирний великий (175 грн)", callback_data="зцлвцшрацнпвп")
            ],
            [
                InlineKeyboardButton(text="шоколадний маленький (80 грн)", callback_data="хйщвцшоагвурамнвим")
            ],
            [
                InlineKeyboardButton(text="шоколадний середній (120 грн)", callback_data="зйвщцоагуврсмнвми")
            ],
            [
                InlineKeyboardButton(text="шоколадний великий (185 грн)", callback_data="моагпмнпаеупасвса")
            ],
        ]

        kb = InlineKeyboardMarkup(inline_keyboard=buttons2)

        await message.answer(
            "Виберіть попкорн, який ви хочете купити",
            reply_markup=kb)


    @dp.callback_query(F.data == "щртлшкатута")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 60:

            number -= 60
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький попкорн зі смаком карамелі за 60 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "запмлушврй")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 100:

            number -= 100
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній попкорн зі смаком карамелі за 100 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "азулашцруйн")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 150:

            number -= 150
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великий попкорн зі смаком карамелі за 150 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "зклацшвуйгру")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 70:

            number -= 70
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький попкорн зі смаком бекону за 70 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "мзукалцшврйнп")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 120:

            number -= 120
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній попкорн зі смаком бекону за 120 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "азцдвцшоагурап")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 180:

            number -= 180
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великий попкорн зі смаком бекону за 180 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "цхавдуаоктпотами")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 65:

            number -= 65
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький попкорн зі смаком сиру за 65 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "звйлвацшраврикм")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 100:

            number -= 100
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній попкорн зі смаком сиру за 100 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "зцлвцшрацнпвп")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 170:

            number -= 170
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великий попкорн зі смаком сиру за 170 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "хйщвцшоагвурамнвим")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 75:

            number -= 75
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький попкорн зі смаком шоколаду за 75 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "зйвщцоагуврсмнвми")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 105:

            number -= 105
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній попкорн зі смаком шоколаду за 105 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "моагпмнпаеупасвса")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 165:

            number -= 165
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великий попкорн зі смаком шоколаду за 165 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")








if cought_cinema == "Магнат":

    @dp.message(F.text == "Купити білет")
    async def cmd_answer(message: types.Message):
        buttons3 = [
            [
                InlineKeyboardButton(text="На фільм Бджоляр (220 грн)", callback_data="єощзєгеншп")
            ],
            [
                InlineKeyboardButton(text="На фільм Шлях до слави (195 грн)", callback_data="зжшдгнкеіуе")
            ],
            [
                InlineKeyboardButton(text="На фільм Володар хаосу (160 грн)", callback_data="іукеукнгогл")
            ],
            [
                InlineKeyboardButton(text="На фільм Аргайл (240 грн)", callback_data="апоглглеговгкве")
            ],
            [
                InlineKeyboardButton(text="На фільм Догмен (175 грн)", callback_data="фвауапиророь")
            ],
            [
                InlineKeyboardButton(text="На фільм Бідолашні створіння (210 грн)", callback_data="голкепукцецк")
            ],
            [
                InlineKeyboardButton(text="На фільм Залізний кіготь (235 грн)", callback_data="жєзєщгшщншнеш")
            ],
        ]

        keyboard = InlineKeyboardMarkup(inline_keyboard=buttons3)

        await message.answer(
            "Оберіть фільм, на який ви хочете придбати квиток",
            reply_markup=keyboard)


    @dp.callback_query(F.data == "єощзєгеншп")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 220:

            number -= 220
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Бджоляр за 220 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей")


    @dp.callback_query(F.data == "зжшдгнкеіуе")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 195:

            number -= 195
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Шлях до слави за 195 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "іукеукнгогл")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 160:

            number -= 160
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Володар хаосу за 160 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "апоглглеговгкве")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 240:

            number -= 240
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Аргайл за 240 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "фвауапиророь")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 175:

            number -= 175
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Догмен за 175 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "голкепукцецк")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 210:

            number -= 210
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Бідолашні створіння за 210 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "жєзєщгшщншнеш")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 235:

            number -= 235
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили білет на фільм Залізний кіготь за 235 грн, на " + str(random.randint(1, 10)) + " ряду, на " + str(random.randint(1, 10)) + " місці")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")



    @dp.message(F.text == "Афіша кіно на сьогодні")
    async def cmd_answer(message: types.Message):
        await message.answer("""
Бджоляр - 12:20
Шлях до слави - 14:15
Володар хаосу - 17:10
Аргайл - 19:30
Догмен - 20:05
Бідолашні створіння - 21:00
Залізний кіготь - 22:30
""")





    @dp.message(F.text == "Попкорн та його вартість")
    async def cmd_answer(message: types.Message):
        await message.answer("""
Карамельний маленький - 58грн    середній - 104грн    великий - 155грн\n
З беконом маленький - 73грн    середній - 125грн    великий - 190грн\n
Сирний маленький - 70грн    середній - 110грн    великий - 176грн\n
Шоколадний маленький - 82грн    середній - 113грн    великий - 171грн
""")


    @dp.message(F.text == "Напої та їх вартість")
    async def cmd_answer(message: types.Message):
        await message.answer("""
Пепсі: 0.3л - 30грн    0.4л - 40грн    0.5л - 57грн\n
Фанта: 0.3л - 34грн    0.4л - 45грн    0.5л - 60грн\n
Спрайт: 0.3л - 32грн    0.4л - 48грн    0.5л - 64грн\n
Вода негазована: 0.5л - 42грн    1л - 73грн\n
Вода газована: 0.5л - 48грн    1л - 80грн
""")


    @dp.message(F.text == "Купити напій")
    async def cmd_answer(message: types.Message):
        buttons2 = [
            [
                InlineKeyboardButton(text="Пепсі 0.3л (30 грн)", callback_data="щерплкоауца")
            ],
            [
                InlineKeyboardButton(text="Пепсі 0.4л (40 грн)", callback_data="йщліцщвлущпли")
            ],
            [
                InlineKeyboardButton(text="Пепсі 0.5л (57 грн)", callback_data="лрещокшпокшопкпр")
            ],
            [
                InlineKeyboardButton(text="Фанта 0.3л (34 грн)", callback_data="мошкапоушоапу")
            ],
            [
                InlineKeyboardButton(text="Фанта 0.4л (45 грн)", callback_data="тпрортиаругарм")
            ],
            [
                InlineKeyboardButton(text="Фанта 0.5л (60 грн)", callback_data="тдрщатлвровшп")
            ],
            [
                InlineKeyboardButton(text="Спрайт 0.3л (32 грн)", callback_data="хздронщлркщлерлкеар")
            ],
            [
                InlineKeyboardButton(text="Спрайт 0.4л (48 грн)", callback_data="рьелпрокупокорпи")
            ],
            [
                InlineKeyboardButton(text="Спрайт 0.5л (64 грн)", callback_data="вцогаупокиорпшти")
            ],
            [
                InlineKeyboardButton(text="Вода негазована 0.5л (42 грн)", callback_data="йуцдазуплкщрлп")
            ],
            [
                InlineKeyboardButton(text="Вода негазована 1л (73 грн)", callback_data="цщзвдуцщалвкпмлаи")
            ],
            [
                InlineKeyboardButton(text="Вода газована 0.5л (48 грн)", callback_data="рогеегегкпоаошуваоп")
            ],
            [
                InlineKeyboardButton(text="Вода газована 1л (80 грн)", callback_data="хкепклщропшкопушпо")
            ],
        ]

        kb = InlineKeyboardMarkup(inline_keyboard=buttons2)

        await message.answer(
            "Виберіть напій, який ви хочете купити",
            reply_markup=kb)


    @dp.callback_query(F.data == "щерплкоауца")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 30:

            number -= 30
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили пепсі 0.3л за 30 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "йщліцщвлущпли")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 40:

            number -= 40
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили пепсі 0.4л за 40 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "лрещокшпокшопкпр")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 57:

            number -= 57
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили пепсі 0.5л за 57 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "мошкапоушоапу")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 34:

            number -= 34
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили фанту 0.3л за 34 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "тпрортиаругарм")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 45:

            number -= 45
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили фанту 0.4л за 45 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "тдрщатлвровшп")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 60:

            number -= 60
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили фанту 0.5л за 60 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "хздронщлркщлерлкеар")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 32:

            number -= 32
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили спрайт 0.3л за 32 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "рьелпрокупокорпи")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 48:

            number -= 48
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили спрайт 0.4л за 48 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "вцогаупокиорпшти")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 64:

            number -= 64
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили спрайт 0.5л за 64 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "йуцдазуплкщрлп")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 42:

            number -= 42
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили негазовану воду 0.5л за 42 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "цщзвдуцщалвкпмлаи")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 73:

            number -= 73
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили негазовану воду 1л за 73 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "рогеегегкпоаошуваоп")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 48:

            number -= 48
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили газовану воду 0.5л за 48 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "хкепклщропшкопушпо")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 80:

            number -= 80
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили газовану воду 1л за 80 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")




    @dp.message(F.text == "Купити попкорн")
    async def cmd_answer(message: types.Message):
        buttons2 = [
            [
                InlineKeyboardButton(text="карамельний маленький (58 грн)", callback_data="флыщошвошыаов")
            ],
            [
                InlineKeyboardButton(text="карамельний середній (104 грн)", callback_data="жзглнеукцукцк")
            ],
            [
                InlineKeyboardButton(text="карамельний великий (155 грн)", callback_data="пуцепрглшлш")
            ],
            [
                InlineKeyboardButton(text="з беконом маленький (73 грн)", callback_data="зыфлывовоасв")
            ],
            [
                InlineKeyboardButton(text="з беконом середній (125 грн)", callback_data="йакппеиррлшл")
            ],
            [
                InlineKeyboardButton(text="з беконом великий (190 грн)", callback_data="жюдюлдотьиииапи")
            ],
            [
                InlineKeyboardButton(text="сирний маленький (70 грн)", callback_data="юдюопарапчтр")
            ],
            [
                InlineKeyboardButton(text="сирний середній (110 грн)", callback_data="бдлолпрпврврвв")
            ],
            [
                InlineKeyboardButton(text="сирний великий (176 грн)", callback_data="выывппртоьоьоьо")
            ],
            [
                InlineKeyboardButton(text="шоколадний маленький (82 грн)", callback_data="енеотимсмм")
            ],
            [
                InlineKeyboardButton(text="шоколадний середній (113 грн)", callback_data="зуалщкпошапргир")
            ],
            [
                InlineKeyboardButton(text="шоколадний великий (171 грн)", callback_data="кйывцвургауврамгр")
            ],
        ]

        kb = InlineKeyboardMarkup(inline_keyboard=buttons2)

        await message.answer(
            "Виберіть попкорн, який ви хочете купити",
            reply_markup=kb)


    @dp.callback_query(F.data == "флыщошвошыаов")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 58:

            number -= 58
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький попкорн зі смаком карамелі за 58 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "жзглнеукцукцк")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 104:

            number -= 104
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній попкорн зі смаком карамелі за 104 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "пуцепрглшлш")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 155:

            number -= 155
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великий попкорн зі смаком карамелі за 155 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "зыфлывовоасв")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 73:

            number -= 73
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький попкорн зі смаком бекону за 73 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "йакппеиррлшл")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 125:

            number -= 125
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній попкорн зі смаком бекону за 125 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "жюдюлдотьиииапи")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 190:

            number -= 190
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великий попкорн зі смаком бекону за 190 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "юдюопарапчтр")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 70:

            number -= 70
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький попкорн зі смаком сиру за 70 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "бдлолпрпврврвв")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 110:

            number -= 110
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній попкорн зі смаком сиру за 110 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "выывппртоьоьоьо")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 176:

            number -= 176
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великий попкорн зі смаком сиру за 176 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "енеотимсмм")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 82:

            number -= 82
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили маленький попкорн зі смаком шоколаду за 82 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "зуалщкпошапргир")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 113:

            number -= 113
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили середній попкорн зі смаком шоколаду за 113 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")


    @dp.callback_query(F.data == "кйывцвургауврамгр")
    async def send_random_value(callback: types.CallbackQuery):
        file = open("Баланс.txt", 'r')
        number = int(file.read())
        file.close()

        if number >= 171:

            number -= 171
            file = open("Баланс.txt", 'w')
            file.write(str(number))
            file.close()
            await callback.message.answer("Ви купили великий попкорн зі смаком шоколаду за 171 грн")
        else:
            await callback.message.answer("На вашому балансі не вистачає грошей, вам треба поповнити карту")




















@dp.message(F.text == "Баланс карти")
async def cmd_answer(message: types.Message):
    file1 = open("Баланс.txt", 'r')
    balans = file1.read()
    await message.answer(f"Ваш баланс зараз - {balans} грн")


@dp.message(F.text == "Адреси наших кінотеатрів")
async def cmd_answer(message: types.Message):
    await message.answer("""
Наші кінотеатри знаходяться за адресами:
вул. Пушкіна 13
вул. Кільцева 9б
вул. Новорічна 48
вул. Сумська 230
проспект Героїв Харкова 86
Чекаємо саме на вас!
""")


@dp.message(F.text == "Розробники цього бота")
async def cmd_answer(message: types.Message):
    await message.answer("Рома, Саша")


@dp.message(F.text == "Поповнити карту")
async def cmd_answer(message: types.Message):
    buttons2 = [
        [
            InlineKeyboardButton(text="Поповнити на 500 грн", callback_data="nuй_decr")
        ],
        [
            InlineKeyboardButton(text="Поповнити на 250 грн", callback_data="nuц_decr")
        ],
        [
            InlineKeyboardButton(text="Поповнити на 100 грн", callback_data="nuу_decr")
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons2)

    await message.answer(
        "На скільки ви хочете поповнити карту?",
        reply_markup=keyboard)


@dp.callback_query(F.data == "nuй_decr")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", "r")
    number = int(file.read())
    file.close()

    number += 500

    file = open("Баланс.txt", 'w')
    file.write(str(number))
    file.close()

    await callback.message.answer(f"Ви поповнили карту на 500 грн, ваш баланс тепер складає {number}")


@dp.callback_query(F.data == "nuц_decr")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    number += 250

    file = open("Баланс.txt", 'w')
    file.write(str(number))
    file.close()

    await callback.message.answer(f"Ви поповнили карту на 250 грн, ваш баланс тепер складає {number}")


@dp.callback_query(F.data == "nuу_decr")
async def send_random_value(callback: types.CallbackQuery):
    file = open("Баланс.txt", 'r')
    number = int(file.read())
    file.close()

    number += 100

    file = open("Баланс.txt", 'w')
    file.write(str(number))
    file.close()

    await callback.message.answer(f"Ви поповнили карту на 100 грн, ваш баланс тепер складає {number}")



@dp.message(Command("help"))
async def cmd_answer(message: types.Message):
    await message.answer("Якщо вам щось незрозуміло або хочете щось уточнити, то не соромтесь і задавайте питання сюди: @sheremetkaaaa")


@dp.message(F.text == "Підтримати розробників бота")
async def cmd_answer(message: types.Message):
    await message.answer("""
5168752021570554 або 5168755906406224
(на покушать)
""")


@dp.message(F.sticker)
async def message_with_sticker(message: Message):
    await message.answer("Це стікер! Будь ласка, виберіть якусь функцію з меню можливих варіантів.")


@dp.message(F.animation)
async def message_with_gif(message: Message):
    await message.answer("Це GIF, я таке не сприймаю:(")


@dp.message(F.video)
async def message_with_video(message: Message):
    await message.answer("""
Це відео! Замість цього відео, ви можете скористатися функцією з меню, а я зможу вас погрузити у світ кіно!
Дозвольте мені допомогти вам розширити ваш кіно-досвід)
""")



@dp.message(F.photo)
async def message_with_sticker(message: Message):
    await message.answer("Дуже красива фотографія) Але якщо ви хочете користуватись ботом на тему кіно, то будь ласка, виберіть якусь функцію з меню можливих варіантів.")


@dp.message(Command("otzyw"))
async def cmd_answer(message: types.Message):
    global leaving_review
    leaving_review = True
    await message.answer("Будь ласка, у наступному повідомленні напишіть свій відгук та враження про бота.")
@dp.message(F.text)
async def save_review(message: Message):
    global leaving_review
    if leaving_review:
        review_text = message.text
        with open("відгуки.txt","a") as file:
            file.write(f"_______________________________\n")
            file.write(f"Відгук: {message.text}\n")
        await message.answer("Ваш відгук записано та передано розробникам бота!")
        leaving_review = False
    else:
        await message.reply("Мені подобається ваше текстове повідомлення, але у форматі введеного вами тексту я сприймаю лише відгуки користувачів. Для залишення відгуку використовуйте команду /otzyw.")




async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())