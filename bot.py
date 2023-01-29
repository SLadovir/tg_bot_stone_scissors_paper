import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config
from handlers.user_handlers import register_user_handlers
from handlers.other_handlers import register_other_handlers


# Инициализируем логгер
logger = logging.getLogger(__name__)


# Фнукция для регистрации всех хэндлеров
def register_all_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)
    register_other_handlers(dp)

