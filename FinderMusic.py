#Name: FinderMusic
#Decsription: A module for searching music in @fmusbot
#Author: kayt3m
#Commands: 
# .fm
# 
#     _  __     ____    __    __  ________    ____       __  __
#    | |/ /    / /\ \   \ \  / / |__    __|  /_/\ \     /  \/  \
#    |   /    / /__\ \   \ \/ /     |  |        / /    / /\__/\ \
#    |   \   / /____\ \   |  |      |  |     _  \ \   / /      \ \
#    |_|\_\ /_/      \_\  |__|      |__|     \_\/_/  /_/        \_\
#    
#
#
#     🔐  Licenced under the GNU AGPLv3
#                        https://www.gnu.org/licenses/aplg-3.0.html
#meta developer: @dev_n0
#

__version__ = (1, 0, 1)

import logging
from .. import loader, main, utils 

logger = logging.getLogger(__name__)

class FinderMusic(loader.Module):
    """A module for searching music in bot @fmusbot """
    strings = {
        "name": "FinderMusic",
        "na": "<b>What do you need to find?</b>",
        "searching": "<b><emoji document_id=5309924890462134382>📀</emoji>Search...</b>"
    }
    async def fmcmd(self, message):
        """Music search"""
        args = utils.get_args_raw(message)
        r = await message.get_reply_message()
        bot = "@fmusbot"
        if not args:
            return await message.edit(self.strings("na"))
        try:
            await message.edit(self.strings("searching"))
            find = await message.client.inline_query(bot, args)
            await message.delete()
            try:
                await message.client.send_file(
                    message.to_id,
                    find[1].result.document,
                    caption="<b>Maybe this is the track you are looking for.</b>",
                    reply_to=utils.get_topic(message) if r else None,
                 )
            except:
                await message.client.send_file(
                    message.to_id,
                    find[3].result.document,
                    captain="<b>Maybe this is the track you are looking for.</b>",
                    reply_to=utils.get_topic(message) if r else None

                 )
        except:
            return await message.client.send_message(
                message.chat_id,
                f"<b>Sorry, I couldn't find your track. <code>{args}</code></b>"
            )        
