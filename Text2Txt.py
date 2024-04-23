#Name: Text2Txt
#Description: Module for convertation your text to .txt file
#Author: @nervousmods
#Commands:
#.t2t
# ---------------------------------------------------------------------------------
#🔒 Licensed under the GNU GPLv3
#🌐 https://www.gnu.org/licenses/agpl-3.0.html
#⚠️ All modules is not scam and absolutely safe.
#👤 https://t.me/smlgwy
#-----------------------------------------------------------------------------------
#meta developer: @nervousmods, @hikka_mods
#scope: hikka_only 
#scope: hikka_min 1.4.2
#-----------------------------------------------------------------------------------

from hikka import loader, utils
import logging
from telethon.tl.types import Message
import io

__version__ = (1, 0, 0)
logger = logging.getLogger(__name__)

@loader.tds
class Text2TXT(loader.Module):
    """Module for convertation your text to .txt file"""
    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "name",
                "file.txt",
                lambda:
                self.strings("cfg_name"),
            ),
        )

    strings = {
        "name": "Text2Txt",
        "no_args": "Don't have any args!",
        "cfg_name": "Enter a custom file name",
    }

    strings_ru = {
        "no_args": "Недостаточно аргументов! Используйте: .txt args",
        "cfg_name": "Введите собственное значение для названия файла",
    }

    @loader.command()
    async def t2tcmd(self, message: Message):
        """-> to create a .txt file with your custom text"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("no_args"))
        else:
            text = args
            by = io.BytesIO(text.encode("utf-8"))
            by.name = self.config["name"]

            await utils.answer_file(message, by)
