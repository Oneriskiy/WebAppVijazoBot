
from handlers import router
from config import TOKEN
from aiogram import types
from aiogram import types, Router, Bot, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from text import InfoMainText, HelpMainText, StartMainText
from menu import builderBack, builderSocial, builder
callbackrouter = Router()

dp = Dispatcher()
bot = Bot(TOKEN)





@callbackrouter.callback_query(lambda c: c.data in ['help', 'info', 'social'])
async def help_main(callback_query: types.CallbackQuery):
    if callback_query.data == 'info':
        await callback_query.message.edit_text(InfoMainText, parse_mode="HTML", reply_markup=builderBack)
    elif callback_query.data == 'help':
        await callback_query.message.edit_text(HelpMainText, parse_mode="HTML", reply_markup=builderBack)
    elif callback_query.data == 'social':
        await callback_query.message.edit_text('Соц сети Vijazo', parse_mode="HTML", reply_markup=builderSocial)


@callbackrouter.callback_query(lambda c: c.data in ['back'])
async def help_main(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(StartMainText, parse_mode= 'HTML', reply_markup= builder)