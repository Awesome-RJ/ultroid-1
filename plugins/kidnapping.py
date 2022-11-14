from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest

from userbot import CMD_HELP
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd

async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply(
                "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = " ".join(names)
    return full_name


@bot.on(admin_cmd(pattern="scrapall ?(.*)"))
@bot.on(sudo_cmd(pattern="scrapall ?(.*)", allow_sudo=True))
async def get_users(event):
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        hell = await edit_or_reply(event, "𝐘𝐮𝐤𝐢 𝐌𝐞𝐦𝐞𝐛𝐞𝐫𝐬 𝐒𝐜𝐫𝐚𝐩𝐩𝐢𝐧𝐠 𝐂𝐨𝐫𝐞 𝐒𝐭𝐚𝐫𝐭𝐞𝐝....")
    else:
        hell = await edit_or_reply(event, "𝐘𝐮𝐤𝐢 𝐌𝐞𝐦𝐞𝐛𝐞𝐫𝐬 𝐒𝐜𝐫𝐚𝐩𝐩𝐢𝐧𝐠 𝐂𝐨𝐫𝐞 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠....")
    kraken = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await hell.edit("𝐒𝐨𝐫𝐫𝐲, 𝐒𝐜𝐫𝐚𝐩 𝐮𝐬𝐞𝐫𝐬 𝐡𝐞𝐫𝐞")
    s = 0
    f = 0
    error = "None"

    await hell.edit("⇝ GIɾʅʂ Bσყʂ ҲƊ 💜 𝐒𝐭𝐚𝐭𝐮𝐬\n\n𝐌𝐞𝐦𝐞𝐛𝐞𝐫𝐬 𝐒𝐜𝐫𝐚𝐩𝐩𝐢𝐧𝐠 𝐔𝐬𝐞𝐫𝐬.......")
    async for user in event.client.iter_participants(kraken.full_chat.id):
        try:
            if error.startswith("Too"):
                return await hell.edit(
                    f"**𝐒𝐜𝐫𝐚𝐩𝐩𝐢𝐧𝐠 𝐅𝐢𝐧𝐢𝐬𝐡𝐞𝐝 𝐖𝐢𝐭𝐡 𝐄𝐫𝐫𝐨𝐫**\n(`𝐌𝐚𝐲 𝐆𝐨𝐭 𝐋𝐢𝐦𝐢𝐭 𝐄𝐫𝐫𝐨𝐫 𝐟𝐫𝐨𝐦 𝐤𝐢𝐝𝐧𝐚𝐩𝐞𝐫 𝐥𝐨𝐥, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧 𝐋𝐚𝐭𝐞𝐫`)\n**Error** : \n`{error}`\n\n• Kidnapped `{s}` people \n➛ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐭𝐨 𝐒𝐜𝐫𝐚𝐩 `{f}` 𝐩𝐞𝐨𝐩𝐥𝐞"
                )
            await event.client(
                functions.channels.InviteToChannelRequest(channel=chat, users=[user.id])
            )
            s = s + 1
            await hell.edit(
                f"**𝐒𝐜𝐫𝐚𝐩𝐞𝐫 𝐑𝐮𝐧𝐧𝐢𝐧𝐠..**\n\n➛ 𝐒𝐜𝐫𝐞𝐩𝐞𝐝 `{s}` people \n➛ 𝐅𝐚𝐢𝐥𝐞𝐝 𝐭𝐨 𝐒𝐜𝐫𝐚𝐩 `{f}` people\n\n**➛ 𝐋𝐚𝐬𝐭𝐄𝐫𝐫𝐨𝐫:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await hell.edit(
        f"**𝐒𝐜𝐫𝐚𝐩𝐢𝐧𝐠 𝐅𝐢𝐧𝐢𝐬𝐡𝐞𝐝** \n\n➛ 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐒𝐜𝐫𝐚𝐩𝐞𝐝 `{s}` people \n➛ 𝐟𝐚𝐢𝐥𝐞𝐝 𝐭𝐨 𝐒𝐜𝐫𝐚𝐩𝐞 `{f}` people"
    )
