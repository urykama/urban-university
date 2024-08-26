# 2024/01/17 00:00|Домашнее задание по теме "Машина состояний".
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age, growth, weight, gender, activity = [State() for _ in range(5)]


@dp.message_handler(text=['Calories'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


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


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)