#Name: calcmod
#Description: Calculator module
#Author: Gwynplaine
#Commands:
#.ccm
#---------------------------------------------------------------------------------
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# ⚠️ All modules is not scam and absolutely safe.
# 👤 https://t.me/morcorp
#-----------------------------------------------------------------------------------
#meta developer: @smlgwy
#scope: hikka_only 
#scope: hikka_min 1.4.2
#-----------------------------------------------------------------------------------

from .. import loader, utils

@loader.tds
class calcmod(loader.Module):
    """Calculator module."""
    strings = {
        "name": "Calcmod",
    }
    async def ccmcmd(self, message):
        """ -> calculate the value of an expression."""
        q = utils.get_args_raw(message)
        r = await message.get_reply_message()
        if not q:
            if not r:
                await utils.answer(message, "<b>e.g.<emoji document_id=5364179527230564196>⚪️</emoji> 1+1=2</b>")
                return
            else:
                q = r.raw_text
        try:
            a = eval(q)
            a = f"<b>{q}=</b><code>{a}</code>"
        except Exception as e:    
            a = f"<b>{q}=</b><code>{e}</code>"
        await utils.answer(message, a)