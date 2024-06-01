from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def add_back_main_button() -> ReplyKeyboardMarkup:
	"""
	Кнопка для возврата на родительскую страницу.

	:return: markup
	"""
	# Инициализация клавиатуры и добавление кнопки «Вернуться»
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	back_main_page = KeyboardButton(text='Вернуться')
	markup.add(back_main_page)

	return markup


def course_now_button() -> ReplyKeyboardMarkup:
	"""
	Кнопка для перехода к редактированию списка

	:return: markup
	"""
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	edit_currencies = KeyboardButton(text='Главная')
	markup.add(edit_currencies)

	return markup


def add_back_main_custom_button() -> ReplyKeyboardMarkup:
	"""
	Возврат на домашнюю страницу в команде custom.

	:return: markup
	"""
	markup = course_now_button()
	back_main = KeyboardButton(text='Вернуться к выбору периода')
	markup.add(back_main)

	return markup


def main_buttons() -> ReplyKeyboardMarkup:
	"""
	Кнопки для главной страницы

	:return: markup
	"""
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	button1 = KeyboardButton(text='Список валют')
	button2 = KeyboardButton(text='Посчитать курс')
	button3 = KeyboardButton(text='Курс за период')
	markup.row(button1)
	markup.row(button2, button3)

	return markup


def remove_keyboard_button() -> ReplyKeyboardRemove:
	"""
	Удаление клавиатуры

	:return: ReplyKeyboardRemove
	"""
	return ReplyKeyboardRemove()