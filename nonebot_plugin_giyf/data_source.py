import re
from typing import Optional
from urllib import parse

from nonebot.adapters.onebot.v11 import Bot, utils, GroupMessageEvent

from .config import Config


async def search_handle(bot: Bot, event: GroupMessageEvent):
    msg = str(event.message).strip().lstrip(" ？?")
    msg = utils.unescape(msg)
    cfg: Config = Config(event.group_id)
    try:
        prefix, keyword = re.split(" ", msg, maxsplit=1)
    except ValueError:
        return

    url = cfg.get_url(prefix)
    if url:
        await bot.send(event, url_parse(url, keyword))


def url_parse(url: str, keyword: str) -> Optional[str]:
    if url:
        return re.sub(r"%s(?!\w)", parse.quote(keyword), url, count=1)  # 排除后面跟的有其他字母/数字的
