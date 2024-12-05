import logging
from config import TOKEN
from menu import builder, builderBack, builderSocial,builderBackTwo
from aiogram import types, Router, Dispatcher, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart, Command, StateFilter
from text import InfoMainText, HelpMainText, StartMainText, NotHandledText
dp = Dispatcher()
router = Router()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.message(Command('start' , 'info', 'help', 'social'))
async def MainFunc(message: types.Message):
    if message.text == '/start':
        await message.answer(StartMainText, parse_mode= 'HTML', reply_markup= builder)
    if message.text == '/social':
        await message.answer("Sfvdfs", parse_mode= 'HTML', reply_markup= builderSocial)
    if message.text == '/info':
        await message.answer(InfoMainText, parse_mode = 'HTML', reply_markup= builderBack)
    if message.text == '/help':
        await message.answer(HelpMainText, parse_mode = 'HTML', reply_markup = builderBack)
        

@router.message()
async def TextFunc(message: types.Message):
    await message.answer(NotHandledText, parse_mode = 'HTML', reply_markup = builderBackTwo)

