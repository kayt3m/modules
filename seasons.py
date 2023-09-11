#Name: Seasons
#Description: Модуль - таймер времен года.
#Author: Gwynplaine
#Commands:
#.sut | .aut | .wit | .spt
#---------------------------------------------------------------------------------
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# ⚠️ All modules is not scam and absolutely safe.
# 👤 https://t.me/morcorp
#meta developer: @smlgwy

__version__ = (2, 0, 1)

from datetime import datetime
from .. import loader, utils

@loader.tds
class Seasons(loader.Module):
    """Модуль - таймер до начала времен года."""

    strings = {
        "name": "Seasons"
        }

    
    @loader.command()
    async def wit(self, message):
        """-> вывести таймер до зимы."""
        now = datetime.now()
        winter = datetime(now.year, 12, 1)
        
        if now.month > 12 or (now.month == 12 and now.day > 1):
            winter = datetime(now.year + 1, 12, 1)

        time_to_winter = abs(winter - now)

        await utils.answer(
            message,
            (
            "<b><emoji document_id=5258258882022612173>⏲</emoji>До зимы:\n"
                f"Дней<emoji document_id=5364179527230564196>⚪️</emoji> {time_to_winter.days}\n"
                f"Часов<emoji document_id=5364179527230564196>⚪️</emoji> {time_to_winter.seconds // 3600}\n"
                f"Минут<emoji document_id=5364179527230564196>⚪️</emoji> {time_to_winter.seconds // 60 % 60}\n</b>"              
            ),
        ),
    
    @loader.command()
    async def sut(self, message):
        """-> вывести таймер до лета."""
        now = datetime.now()
        summer = datetime(now.year, 6, 1)
        
        if now.month > 6 or (now.month == 6 and now.day > 1):
            summer = datetime(now.year + 1, 6, 1)

        time_to_summer = abs(summer - now)

        await utils.answer(
            message,
            (
            "<b><emoji document_id=5258258882022612173>⏲</emoji>До лета:\n"
                f"Дней<emoji document_id=5364179527230564196>⚪️</emoji> {time_to_summer.days}\n"
                f"Часов<emoji document_id=5364179527230564196>⚪️</emoji> {time_to_summer.seconds // 3600}\n"
                f"Минут<emoji document_id=5364179527230564196>⚪️</emoji> {time_to_summer.seconds // 60 % 60}\n</b>"
            ),
        ),
    
    @loader.command()
    async def aut(self, message):
        """-> вывести таймер до осени."""
        now = datetime.now()
        autumn = datetime(now.year, 9, 1)
        
        if now.month > 9 or (now.month == 9 and now.day > 1):
            autumn = datetime(now.year + 1, 9, 1)

        time_to_autumn = abs(autumn - now)

        await utils.answer(
            message,
            (
            "<b><emoji document_id=5258258882022612173>⏲</emoji>До осени:\n"
                f"Дней<emoji document_id=5364179527230564196>⚪️</emoji> {time_to_autumn.days}\n"
                f"Часов<emoji document_id=5364179527230564196>⚪️</emoji> {time_to_autumn.seconds // 3600}\n"
                f"Минут<emoji document_id=5364179527230564196>⚪️</emoji> {time_to_autumn.seconds // 60 % 60}\n</b>"     
            ),
        ),
    
    @loader.command()
    async def spt(self, message):
        """-> вывести таймер до весны."""
        now = datetime.now()
        spring = datetime(now.year, 3, 1)
        
        if now.month > 3 or (now.month == 3 and now.day > 1):
            spring  = datetime(now.year + 1, 3, 1)

        time_to_spring  = abs(spring  - now)

        await utils.answer(
            message,
            (
            "<b><emoji document_id=5258258882022612173>⏲</emoji>До весны:\n"
               f"Дней<emoji document_id=5364179527230564196>⚪️</emoji> {time_to_spring.days}\n"
               f"Часов<emoji document_id=5364179527230564196>⚪️</emoji> {time_to_spring.seconds // 3600}\n"
               f"Минут<emoji document_id=5364179527230564196>⚪️</emoji> {time_to_spring.seconds // 60 % 60}\n</b>"
            ),
        )