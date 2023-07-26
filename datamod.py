# Name: Time
# Author: kayt3m
# Commands:
# .now
# Licenced under the GNU AGPLv3
#                           https://www.gnu.org/licenses/apgl-3.0.html
#meta developer: @def_n0

from datetime import datetime
from .. import loader, utils

class Time(loader.Module):

    strings = {"name": "Today"}

    @loader.command()
    async def now(self, message):
        """- показать сегодняшнюю дату"""
        time = datetime.now()


        await utils.answer(
                message,
                ("<b><emoji document_id=5370711279134582149>🗓</emoji><u>NOW--></u>\n"
                 f"<b><emoji document_id=5258105663359294787>🗓</emoji>>year: {time.year}\n</b>"
                 f"<b><emoji document_id=5258105663359294787>🗓</emoji>>month: {time.month}\n</b>"
                 f"<b><emoji document_id=5258105663359294787>🗓</emoji>>day: {time.day}\n</b>"
                 f"<b><emoji document_id=5258258882022612173>⏲</emoji>>time: {time.hour}</b>:"
                 f"{time.minute}:"
                 f"{time.second}(UTC+3)</b>"

                 ),
            )
