from wxauto import *
import time

from ChatGPT import generate_response

wx = WeChat()

wx.GetSessionList()

while True:
    try:
        msgs = wx.GetLastMessage
        print(msgs)
        if msgs[0] != "Void":
            recv_msg = msgs[1]
            output_message = generate_response(recv_msg)
            print(output_message)
            who = '张泽凯'
            wx.ChatWith(who)
            wx.SendMsg(output_message)
            time.sleep(5)
        else:
            time.sleep(5)
    except Exception as ex:
        pass


