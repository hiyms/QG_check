import checklib as cl
import qg_botsdk as botsdk
import key

bot = botsdk.BOT(key.BOT_ID,key.BOT_TOKEN,is_private=True)

def msg_function(data: botsdk.Model.MESSAGE):
    # print(bot.api.get_channel_member_permission(channel_id=data.channel_id,user_id=data.author.id).data.permissions)
    text = data.treated_msg
    if text == None:
        return
    if cl.check_txt(str(text)):
        ...
        if bot.api.get_channel_member_permission(channel_id=data.channel_id,user_id=data.author.id).data.permissions!="7" and not data.author.bot:
            bot.api.delete_msg(channel_id=data.channel_id,message_id=data.id)
            bot.api.send_embed(title="内容包含敏感词",channel_id=data.channel_id,content=['{}所发送的信息包含敏感词'.format(data.author.username),'已经撤回'])
        else:
            bot.api.send_embed(title="内容包含敏感词",channel_id=data.channel_id,content=['{}所发送的信息包含敏感词'.format(data.author.username)])
            
bot.bind_msg(msg_function)
bot.start()




