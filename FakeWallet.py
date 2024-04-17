# Name: FakeWallet
#Description: Fun joke - fake crypto wallet. Your balance = π
# Author: @nervousmods
# Commands:
# .fwallet | .fwinfo
# ---------------------------------------------------------------------------------
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# ⚠️ All modules is not scam and absolutely safe.
# 👤 https://t.me/smlgwy
#-----------------------------------------------------------------------------------
# meta developer: @hikka_mods, @nervousmods
#scope: hikka_only 
#scope: hikka_min 1.4.2
#-----------------------------------------------------------------------------------

from .. import loader, utils
import logging
from telethon.tl.custom import Message
import numpy as np

__version__ = (1, 0, 0)
logger = logging.getLogger(__name__)


@loader.tds
class FakeWallet(loader.Module):
    """Fun joke - fake crypto wallet. Your balances = π"""
    strings = {
        "name": "FakeWallet",
    }

    @loader.command()
    async def fwalletcmd(self, message: Message):
        """-> to get a fake wallet"""
        np.set_printoptions(precision=11)
        pi = np.pi
        await utils.answer(message,
                           (f"<emoji document_id=5438626338560810621>👛</emoji> <b>Wallet</b>\n\n<emoji document_id=5215276644620586569>☺️</emoji> <a href='https://ton.org'>Toncoin</a>: {pi} TON\n\n<emoji document_id=5215699136258524363>☺️</emoji> <a href='https://tether.to'>Tether</a>: {pi} USDT\n\n<emoji document_id=5215590800003451651>☺️</emoji> <a href='https://bitcoin.org'>Bitcoin</a>: {pi} BTC\n\n<emoji document_id=5217867240044512715>☺️</emoji> <a href='https://etherium.org'>Etherium</a>: {pi} ETH\n\n<emoji document_id=5215595550237279768>☺️</emoji> <a href='https://binance.org'>Binance coin</a>: {pi} BNB\n\n<emoji document_id=5215437796088499410>☺️</emoji> <a href='https://tron.network'>TRON</a>: {pi} TRX\n\n<emoji document_id=5215440441788351459>☺️</emoji> <a href='https://www.centre.io/usdc'>USD Coin</a>: {pi} USDC\n\n<emoji document_id=5215267041073711005>☺️</emoji> <a href='https://gramcoin.org'>Gram</a>: {pi} GRAM\n\n<emoji document_id=5217877586620729050>☺️</emoji> <a href='https://litecoin.org'>Litecoin</a>: {pi} LTC"),
                           )
        
    @loader.command()
    async def fwinfo(self, message):
        """-> info about FakeModule"""
        await utils.answer(message, "<b><emoji document_id=5305467350064047192>🫥</emoji><i>Attention!</b>\n\n <emoji document_id=5915991028430542030>☝️</emoji>This module is strictly prohibited from being used for the purposes of <b>scam, fraud and advertising</b>.\n\n<emoji document_id=5787190061644647815>🗣</emoji>The module is provided solely for entertainment purposes, and any violation of the <b>Rules for using the module</b>, if detected, will be subject <b>to appropriate punishment</b></i>.")
