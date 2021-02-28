from twilio.rest import Client
from time import sleep
import re
import QBTTXPSE

debug = False


def nothing(msg:str):pass
def print_Message(msg:str = ""):
    print("(debug)--->>",msg)
    sleep(1)


D = {
    False:nothing,
    True :print_Message
}[debug]


msg_no:int = 0


def getIt(what:str = None):
    QXE = ''
    if what == 'AC':
        key = QBTTXPSE.AC
        QXE += 'AC'
    else:
        key = QBTTXPSE.extra
    for Q in key:
        if len(Q) == 1:
            QXE+= Q
        else:
            QXE+= hex(int(Q)).lstrip('0x')
    return QXE






account_sid = getIt('AC')
auth_token = getIt()





client = Client(account_sid, auth_token) 





def __isvalid(text:str = None):
    if text == None:                            return False

    text = text.lstrip('\n').rstrip('\n')

    if re.search("[A-Za-z0-9]", text):          return True
    
    return False



def __send(To:str, msg:str):
    if not __isvalid(msg): return

    global msg_no
    msg_no += 1

    # print(f"SMS-{msg_no}" + "\n" + f"To={To}, msg={msg}"+ "\n" + "-"*40)

    client.messages.create( 
        from_='whatsapp:+14155238886',  
        body =msg.lstrip('\n').rstrip('\n'),      
        to   =f'whatsapp:{To}'
    )
    sleep(1)






sep_list = {
    '\n\n'  :   '\n'    ,   # After \n\n start seperating with help of \n
    '\n'    :   ' '     ,   # After \n start seperating with help of .
    ' '     :   ''          # After <space> start seperating Charachter by Charachter
}



def cutMessage(msg:str, sep:str='\n\n'):
    trimmedMessage = []

    if sep != '':
        trimmedMessage.append('')
        D(f"Message is = {msg}")
        for msgPart in msg.split(sep):
            if len(msgPart) > 1300:
                D(f"MessagePart is = {msgPart} is > 1300")
                for subPart in cutMessage(msgPart, sep_list[sep]):
                    if len(trimmedMessage[-1] + subPart) <= (1300):
                        trimmedMessage[-1] += sep + subPart
                    else:
                        trimmedMessage.append(subPart)
                    D(f"subPart is = {subPart}")
            else:
                if len(trimmedMessage[-1] + msgPart) <= (1300):
                    trimmedMessage[-1] += sep + msgPart
                else:
                    trimmedMessage.append(msgPart)
                D(f"MessagePart is = {msgPart} is <= 1300")
    else:
        for i in range(0,len(msg),1300):
            trimmedMessage.append(msg[i:i+1300])
    
    return trimmedMessage
                    








def sendMessage(msg:str = 'Hello World', clientPhoneNo:str = '+917798044008'):
    D(f"Length of Message : {msg}")
    if len(msg) < 1300:
        D("message Length initially Small")
        __send(To=clientPhoneNo, msg=msg)

    else:
        D("message Length initially Too Big, cutting")
        msg_parts = cutMessage(msg)

        D(f"Now the Message is --> {msg_parts}")

        for msg in msg_parts:
            __send(To=clientPhoneNo, msg=msg)





if __name__ == "__main__":
    cool = "Hello World"*2
    sendMessage(msg=f"*{cool}*")
