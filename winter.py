# Name: winter
# Author: kayt3m
# Commands: 
# .wt
#🔒 Licensed under the GNU AGPLv3
#             https://www.gnu.org/licenses/agpl-3.0.html
#
# meta developer: @dev_n0


from datetime import datetime
from .. import loader, utils

@loader.tds
class WintMod(loader.Module):
    """ Module that outputs a timer before the start of winter. """

    strings = {
        "name": "WinterTime"
    }

    @loader.command()
    async def wt(self, message):
        """- outputs a timer."""
        now = datetime.now()
        winter = datetime(now.year, 12, 1)
        
        if now.month > 12 or (now.month == 12 and now.day > 1):
            winter = datetime(now.year + 1, 12, 1)

        time_to_winter = abs(winter - now)

        await utils.answer(
            message,
            (
            "<b><emoji document_id=5391017948934578296>😌</emoji> До зимы"
                f" осталось: {time_to_winter.days } дней,"
                f" {time_to_winter.seconds // 3600} часов:"
                f" {time_to_winter.seconds // 60 % 60} минут:"
                f" {time_to_winter.seconds % 60} секунд.\n<b>"
                "<b><emoji document_id=5456169836855957796>😊</emoji> Жду вместе с тобой.</b> "
                 
            ),
        )
        
