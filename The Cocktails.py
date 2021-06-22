from flask import Flask #import flask
import utils #import other functions
app = Flask(__name__)

from flask import Flask, request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage,TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction

#要有以下兩個資訊API才能運作，知道要連接哪一個LINE Bot
#Channel access token
line_bot_api = LineBotApi('210iJEGHMYUoFh+spPFRYFggAgkc00ZSPc66L9WwlmgyMmm0nDZuxk7jIUmZVHxW+Wl5xfkGoW58YqrIDGuTqQydJbFYe5o1HgEqtAQmtM0a5kzpCFVmx+Mjy3av0AeTDQsBytu7pEuPFA0N4repRQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5d66fd4055c6d94748dd581d845f1ff0') #Channel secret

#建立callback，檢查LINE Bot的資料是否正確
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

'''以下程式的註解為了因應六種不同的酒類及雞尾酒口味，每一種雞尾酒都會建立一個instruction、ingredients及照片一張，
因此程式碼有大量重覆，註解只會到第一種酒(Vodka)結束(187行)'''
#如果接到user傳送的訊息，就執行下面的function
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text #接收user的訊息

    if mtext == 'Base wine': #如果user的訊息=Base wine
        try:
            message = TextSendMessage(
                # LINE Bot就回傳'Please pick a base wine:'
                text = 'Please pick a base wine:',
                #建立六大基酒的Quick Reply
                quick_reply = QuickReply(
                    items=[
                        QuickReplyButton(
                            action = MessageAction(label='Vodka', text='Vodka') #顯示label為Vodka，按下按鈕回傳Vodka
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Tequila', text='Tequila') #顯示label為Tequila，按下按鈕回傳Tequila
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Gin', text='Gin') #顯示label為Gin，按下按鈕回傳Gin
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Rum', text='Rum') #顯示label為Rum，按下按鈕回傳Rum
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Whisky', text='Whisky') #顯示label為Whisky，按下按鈕回傳Whisky
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Brandy', text='Brandy') #顯示label為Brandy，按下按鈕回傳Brandy
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message) #回傳訊息
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!')) #如果前面發生問題就會回傳'發生錯誤'
    
    if mtext == 'Vodka': #如果user的訊息=Vodka
        try:
            message = TextSendMessage(
                # LINE Bot就回傳'Choose a Vodka cocktail:'
                text = 'Choose a Vodka cocktail:',
                # 建立Vodka的Quick Reply
                quick_reply = QuickReply(
                    items=[
                        QuickReplyButton(
                            action = MessageAction(label='Long vodka', text='Long vodka') #顯示label為Long vodka，按下按鈕回傳Long vodka
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Vodka Fizz', text='Vodka Fizz') #顯示label為Vodka Fizz，按下按鈕回傳Vodka Fizz
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Coffee-Vodka', text='Coffee-Vodka') #顯示label為Coffee-Vodka，按下按鈕回傳Coffee-Vodka
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Vodka Martini', text='Vodka Martini') #顯示label為Vodka Martini，按下按鈕回傳Vodka Martini
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Vodka Russian', text='Vodka Russian') #顯示label為Vodka Russian，按下按鈕回傳Vodka Russian
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Vodka And Tonic', text='Vodka And Tonic') #顯示label為Vodka And Tonic，按下按鈕回傳Vodka And Tonic
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message) #回傳訊息
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Long vodka': #如果user的訊息=Long Vodka
        my_instructions, my_ingredient = utils.cocktails('vodka', 'Long vodka') #呼叫utils.cocktails取得instructions及ingredients
        try:
            message = [
                #顯示處理好的ingredients和instructions
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions + '.'),
                #顯示圖片
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/9179i01503565212.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/9179i01503565212.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message) #回覆訊息
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!')) #如果前面發生問題就會回傳'發生錯誤'
            
    elif mtext == 'Vodka Fizz': #如果user的訊息=Vodka Fizz
        my_instructions, my_ingredient = utils.cocktails('vodka', 'Vodka Fizz') #呼叫utils.cocktails取得instructions及ingredients
        try:
            message = [
                # 顯示處理好的ingredients和instructions
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                # 顯示圖片
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/xwxyux1441254243.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/xwxyux1441254243.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message) #回覆訊息
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!')) #如果前面發生問題就會回傳'發生錯誤'
            
    elif mtext == 'Coffee-Vodka': #如果user的訊息=Coffee-Vodka
        my_instructions, my_ingredient = utils.cocktails('vodka', 'Coffee-Vodka') #呼叫utils.cocktails取得instructions及ingredients
        try:
            message = [
                # 顯示處理好的ingredients和instructions
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                # 顯示圖片
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/qvrrvu1472667494.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/qvrrvu1472667494.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message) #回覆訊息
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!')) #如果前面發生問題就會回傳'發生錯誤'
            
    elif mtext == 'Vodka Martini': #如果user的訊息=Vodka Martini
        my_instructions, my_ingredient = utils.cocktails('vodka', 'Vodka Martini') #呼叫utils.cocktails取得instructions及ingredients
        try:
            message = [
                # 顯示處理好的ingredients和instructions
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                # 顯示圖片
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/qyxrqw1439906528.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/qyxrqw1439906528.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message) #回覆訊息
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!')) #如果前面發生問題就會回傳'發生錯誤'
            
    elif mtext == 'Vodka Russian': #如果user的訊息=Vodka Russian
        my_instructions, my_ingredient = utils.cocktails('vodka', 'Vodka Russian') #呼叫utils.cocktails取得instructions及ingredients
        try:
            message = [
                # 顯示處理好的ingredients和instructions
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                # 顯示圖片
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/rpttur1454515129.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/rpttur1454515129.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message) #回覆訊息
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!')) #如果前面發生問題就會回傳'發生錯誤'
            
    elif mtext == 'Vodka And Tonic': #Vodka And Tonic
        my_instructions, my_ingredient = utils.cocktails('vodka', 'Vodka And Tonic') #呼叫utils.cocktails取得instructions及ingredients
        try:
            message = [
                # 顯示處理好的ingredients和instructions
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                # 顯示圖片
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/lmj2yt1504820500.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/lmj2yt1504820500.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message) #回覆訊息
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!')) #如果前面發生問題就會回傳'發生錯誤'
            
    elif mtext == 'Tequila':
        try:
            message = TextSendMessage(
                text = 'Choose a Tequila cocktail:',
                quick_reply = QuickReply(
                    items=[
                        QuickReplyButton(
                            action = MessageAction(label='Tequila Fizz', text='Tequila Fizz')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Tequila Sour', text='Tequila Sour')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Tequila Sunrise', text='Tequila Sunrise')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Tequila Slammer', text='Tequila Slammer')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Tequila Surprise', text='Tequila Surprise')
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Tequila Fizz':
        my_instructions, my_ingredient = utils.cocktails('Tequila', 'Tequila Fizz')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/2bcase1504889637.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/2bcase1504889637.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Tequila Sour':
        my_instructions, my_ingredient = utils.cocktails('Tequila', 'Tequila Sour')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/ek0mlq1504820601.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/ek0mlq1504820601.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
    
    elif mtext == 'Tequila Sunrise':
        my_instructions, my_ingredient = utils.cocktails('Tequila', 'Tequila Sunrise')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/quqyqp1480879103.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/quqyqp1480879103.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Tequila Slammer':
        my_instructions, my_ingredient = utils.cocktails('Tequila', 'Tequila Slammer')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/43uhr51551451311.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/43uhr51551451311.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Tequila Surprise':
        my_instructions, my_ingredient = utils.cocktails('Tequila', 'Tequila Surprise')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/8189p51504735581.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/8189p51504735581.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Gin':
        try:
            message = TextSendMessage(
                text = 'Choose a Gin cocktail:',
                quick_reply = QuickReply(
                    items=[
                        QuickReplyButton(
                            action = MessageAction(label='Gin Fizz', text='Gin Fizz')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Gin Sour', text='Gin Sour')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Pink Gin ', text='Pink Gin ')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Gin Daisy', text='Gin Daisy')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Gin Sling', text='Gin Sling')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Gin Smash', text='Gin Smash')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Gin Toddy', text='Gin Toddy')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Gin Cooler', text='Gin Cooler')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Gin Squirt', text='Gin Squirt')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Gin Rickey', text='Gin Rickey')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Gin Swizzle', text='Gin Swizzle')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Gin and Soda', text='Gin and Soda')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Gin And Tonic', text='Gin And Tonic')
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
    
    elif mtext == 'Gin Fizz':
        my_instructions, my_ingredient = utils.cocktails('Gin', 'Gin Fizz')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/drtihp1606768397.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/drtihp1606768397.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Gin Sour':
        my_instructions, my_ingredient = utils.cocktails('Gin', 'Gin Sour')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/noxp7e1606769224.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/noxp7e1606769224.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Pink Gin':
        my_instructions, my_ingredient = utils.cocktails('Gin', 'Pink Gin')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/qyr51e1504888618.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/qyr51e1504888618.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Gin Daisy':
        my_instructions, my_ingredient = utils.cocktails('Gin', 'Gin Daisy')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/z6e22f1582581155.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/z6e22f1582581155.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Gin Sling':
        my_instructions, my_ingredient = utils.cocktails('Gin', 'Gin Sling')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/8cl9sm1582581761.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/8cl9sm1582581761.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Gin Smash':
        my_instructions, my_ingredient = utils.cocktails('Gin', 'Gin Smash')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/iprva61606768774.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/iprva61606768774.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Gin Toddy':
        my_instructions, my_ingredient = utils.cocktails('Gin', 'Gin Toddy')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/jxstwf1582582101.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/jxstwf1582582101.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
    
    elif mtext == 'Gin Cooler':
        my_instructions, my_ingredient = utils.cocktails('Gin', 'Gin Cooler')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/678xt11582481163.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/678xt11582481163.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Gin Squirt':
        my_instructions, my_ingredient = utils.cocktails('Gin', 'Gin Squirt')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/xrbhz61504883702.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/xrbhz61504883702.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Gin Rickey':
        my_instructions, my_ingredient = utils.cocktails('Gin', 'Gin Rickey')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/s00d6f1504883945.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/s00d6f1504883945.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Gin Swizzle':
        my_instructions, my_ingredient = utils.cocktails('Gin', 'Gin Swizzle')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/sybce31504884026.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/sybce31504884026.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Gin and Soda':
        my_instructions, my_ingredient = utils.cocktails('Gin', 'Gin and Soda')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/nzlyc81605905755.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/nzlyc81605905755.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Gin And Tonic':
        my_instructions, my_ingredient = utils.cocktails('Gin', 'Gin And Tonic')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/z0omyp1582480573.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/z0omyp1582480573.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Rum':
        try:
            message = TextSendMessage(
                text = 'Choose a Rum cocktail:',
                quick_reply = QuickReply(
                    items=[
                        QuickReplyButton(
                            action = MessageAction(label='Rum Sour', text='Rum Sour')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Rum Toddy', text='Rum Toddy')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Rum Punch', text='Rum Punch')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Cherry Rum', text='Cherry Rum')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Rum Cooler', text='Rum Cooler')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Rum Runner', text='Rum Runner')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Rum Cobbler', text='Rum Cobbler')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Rum Milk Punch', text='Rum Milk Punch')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Rum Screwdriver', text='Rum Screwdriver')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Espresso Rumtini', text='Espresso Rumtini')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Rum Old-fashioned', text='Rum Old-fashioned')
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Rum Sour':
        my_instructions, my_ingredient = utils.cocktails('Rum', 'Rum Sour')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/bylfi21504886323.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/bylfi21504886323.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Rum Toddy':
        my_instructions, my_ingredient = utils.cocktails('Rum', 'Rum Toddy')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/athdk71504886286.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/athdk71504886286.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
    
    elif mtext == 'Rum Punch':
        my_instructions, my_ingredient = utils.cocktails('Rum', 'Rum Punch')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/wyrsxu1441554538.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/wyrsxu1441554538.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
    
    elif mtext == 'Cherry Rum':
        my_instructions, my_ingredient = utils.cocktails('Rum', 'Cherry Rum')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/twsuvr1441554424.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/twsuvr1441554424.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
    
    elif mtext == 'Rum Cooler':
        my_instructions, my_ingredient = utils.cocktails('Rum', 'Rum Cooler')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/2hgwsb1504888674.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/2hgwsb1504888674.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Rum Runner':
        my_instructions, my_ingredient = utils.cocktails('Rum', 'Rum Runner')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/vqws6t1504888857.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/vqws6t1504888857.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
    
    elif mtext == 'Rum Cobbler':
        my_instructions, my_ingredient = utils.cocktails('Rum', 'Rum Cobbler')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/5vh9ld1504390683.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/5vh9ld1504390683.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
    
    elif mtext == 'Rum Milk Punch':
        my_instructions, my_ingredient = utils.cocktails('Rum', 'Rum Milk Punch')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/w64lqm1504888810.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/w64lqm1504888810.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
    
    elif mtext == 'Rum Screwdriver':
        my_instructions, my_ingredient = utils.cocktails('Rum', 'Rum Screwdriver')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/4c85zq1511782093.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/4c85zq1511782093.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Espresso Rumtini':
        my_instructions, my_ingredient = utils.cocktails('Rum', 'Espresso Rumtini')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/acvf171561574403.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/acvf171561574403.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Rum Old-fashioned':
        my_instructions, my_ingredient = utils.cocktails('Rum', 'Rum Old-fashioned')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/otn2011504820649.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/otn2011504820649.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
    
    elif mtext == 'Whisky':
        try:
            message = TextSendMessage(
                text = 'Choose a Whisky cocktail:',
                quick_reply = QuickReply(
                    items=[
                        QuickReplyButton(
                            action = MessageAction(label='Whisky Mac', text='Whisky Mac')
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Whisky Mac':
        my_instructions, my_ingredient = utils.cocktails('Whisky', 'Whisky Mac')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/yvvwys1461867858.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/yvvwys1461867858.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Brandy':
        try:
            message = TextSendMessage(
                text = 'Choose a Brandy cocktail:',
                quick_reply = QuickReply(
                    items=[
                        QuickReplyButton(
                            action = MessageAction(label='Brandy Flip', text='Brandy Flip')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Brandy Sour', text='Brandy Sour')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Brandy Cobbler', text='Brandy Cobbler')
                        ),
                        QuickReplyButton(
                            action = MessageAction(label='Brandy Alexander', text='Brandy Alexander')
                        ),
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Brandy Flip':
        my_instructions, my_ingredient = utils.cocktails('Brandy', 'Brandy Flip')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/6ty09d1504366461.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/6ty09d1504366461.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Brandy Sour':
        my_instructions, my_ingredient = utils.cocktails('Brandy', 'Brandy Sour')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/b1bxgq1582484872.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/b1bxgq1582484872.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Brandy Cobbler':
        my_instructions, my_ingredient = utils.cocktails('Brandy', 'Brandy Cobbler')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/5xgu591582580586.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/5xgu591582580586.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
            
    elif mtext == 'Brandy Alexander':
        my_instructions, my_ingredient = utils.cocktails('Brandy', 'Brandy Alexander')
        try:
            message = [
                TextSendMessage( text = my_ingredient + '\rInstruction:\n' + my_instructions),
                ImageSendMessage(
                    original_content_url = 'https://www.thecocktaildb.com/images/media/drink/mlyk1i1606772340.jpg',
                    preview_image_url = 'https://www.thecocktaildb.com/images/media/drink/mlyk1i1606772340.jpg'
                )]
            line_bot_api.reply_message(event.reply_token,message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))
    
if __name__ == '__main__':
    app.run() #停止