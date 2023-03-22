from logging.config import listen
from typing import Annotated
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.ariadne.message.parser.base import MatchContent

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel = Channel.current()

helpmessage = """
ZiKeBot
------------
提示：方括号为可选参数
------------
/sum [stp]
 - 总结最多100条消息内容
 - 每stp条消息摘取一次内容，默认为1
"""
@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def get_help(app:Ariadne, group:Group, message: MessageChain):
    if str(message).lower() == "/help zike":
        return await app.send_message(
            group,
            MessageChain(helpmessage)
        )
