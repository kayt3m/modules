#Name: FindMusicMod
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

__version__ = (1, 0, 0)

from .. import loader, utils
import logging

logger = logging.getLogger(__name__)
@loader.tds
class FindMusicMod(loader.Module):
    class FindMusicMod(loader.Module):
        """A module for searching music in bot @fmusbot """
    strings = {
        "name": "FindMusicMod",
        "na": "<b>What do you need to find?</b>",
        "searching": "<b><emoji document_id=5309924890462134382>📀</emoji>Search...</b>"
    }
    async def fmcmd(self, message):
        """Music search"""
        args = utils.get_args_raw(message)    
        reply = await message.get_reply_message()
        if not args:
            return await message.edit(self.strings("na"))
        try:
            await message.edit(self.strings("searching"))
            music = await message.client.inline_query("fmusbot", args)
            await message.delete()
            await message.client.send_file(
                message.to_id,
                music[0].result.document,
                reply_to = reply.id if reply else None,

            )
        except:
            return await message.client.send_message(
                message.chat_id,
                f"<b> Sorry, I couldn't find your track. <code>{args}</code> </b>"
            )    
      
