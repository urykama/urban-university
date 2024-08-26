from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import get_all_products
import asyncio

data_products = get_all_products()

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb_start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')]
    ], resize_keyboard=True)

kb_main = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text=text, callback_data=call)
                      for text, call in (('Рассчитать норму калорий', 'calories'), ('Формулы расчёта', 'formulas'))
                      ]], resize_keyboard=True)

kb_products = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text=text[1], callback_data='product_buying')]
                     for text in data_products], resize_keyboard=True)


class UserState(StatesGroup):
    age, growth, weight, gender, activity = [State() for _ in range(5)]


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb_start)


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_main)


@dp.message_handler(text=['Информация'])
async def info(message):
    await message.answer('''Этот бот рассчитает для Вас суточную норму калорий. 
Для этого он запросит возраст, рост, вес, пол и степень активности.
Все ваши сообщения должны быть числами, без лишних знаков.''')


@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    await call.message.answer('''Формулы Миффлина-Сан Жеора, учитывающие степень физической активности человека:
· для мужчин: (10 x вес (кг) + 6.25 x рост (см) – 5 x возраст (г) + 5) x A;
· для женщин: (10 x вес (кг) + 6.25 x рост (см) – 5 x возраст (г) – 161) x A.''')
    await call.answer()


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    for i, e in enumerate(data_products, start=1):
        id_, title, description, price = e
        with open(f'images/{i}.jpg', 'rb') as img:
            await message.answer_photo(img, f'Название: {title} | Описание: {description} | Цена: {price}')
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_products)


@dp.callback_query_handler(text=['product_buying'])
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_gender(message, state):
    await state.update_data(weight=message.text)
    await message.answer('Введите свой пол (мужской - 1, женский - 2):\n(отправьте цифру)')
    await UserState.gender.set()


@dp.message_handler(state=UserState.gender)
async def set_activity(message, state):
    await state.update_data(gender=message.text)
    await message.answer('''Введите свою активность: 
1. Минимальная активность
2. Слабая активность
3. Средняя активность
4. Высокая активность
5. Экстра-активность
(отправьте цифру)''')
    await UserState.activity.set()


@dp.message_handler(state=UserState.activity)
async def send_calories(message, state):
    await state.update_data(activity=message.text)
    data = await state.get_data()
    for k, v in data.items():
        try:
            data[k] = int(v)
        except ValueError:
            k_rus = {'age': 'возраст', 'growth': 'рост', 'weight': 'вес',
                     'gender': 'пол', 'activity': 'активность', }
            await message.answer(f'Параметр "{k_rus[k]}" должен быть числом. Вы ввели "{v}"\n'
                                 'Введите данные заново (отправьте "Calories")')
            await state.finish()
            return

    activity_cases = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}
    user_activity = activity_cases[data['activity']]
    user_gender = -161 if int(data['gender']) - 1 else 5  # True - female, False - male

    calories = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age']
    pro_calories = (calories + user_gender) * user_activity
    await message.answer(f'Ваша норма калорий {pro_calories}')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)