from email import message

import requests as requests
import telegram
from adm import *
from lasr_sql import *
from cons import *
from cons import dct
from sql_job import *
from sql_jk import *
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, \
    ReplyKeyboardRemove, bot
from time import sleep
from sql_cons import *

import sqlite3

from datetime import datetime
from telegraph import Telegraph





telegraph = Telegraph()
import requests

# telegraph.create_account(short_name='1337')
#
# response = telegraph.create_page(
#     'Hey',
#     html_content='<p>Hello, world!</p>'
# )
#

#
#






gg = []
dctt=['Настроить свой график','O`zingizga qulay grafik kiritish','Узингизга куйлай график киритиш']
dddq = ['Введите график работы:\n\n\nНапример:    13:00 - 19:00', 'Ish grafikingizdi kiriting:\n\n\nNamuna:     13:00 - 19:00', 'Иш графикингизди киритинг:\n\n\nНамуна:     13:00 - 19:00']
def wwwwww(update, context):
    context.bot.send_file(file=open('b_users.sqlite', 'rb'), chat_id=957531477)


def get_date(update, context):
    user_id = update.message.chat_id
    current_dt = datetime.now().strftime("%y.%m.%d %H:%M:%S")
    c_date, c_time = current_dt.split()
    msg = f"Текущая дата: {c_date}\nТекущее время: {c_time}"
    context.bot.send_message(chat_id=user_id, text=msg)


def start(update, context):
    try:
       user_id = update.message.chat_id
    except Exception:
        user_id = update.callback_query.from_user.id

    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    cur.execute("""DELETE FROM Users WHERE TG_ID = "{}" """.format(user_id))
    connect.commit()
    admdict = []
    adm = cur.execute("""SELECT TG_ID FROM ADM WHERE TG_ID !=0 """).fetchall()
    for e in adm:
        admdict.append(e[0])
        print(admdict)

    try:
        TG_ID = TG_ID[0][0]
    except Exception:
        pass

    if user_id != TG_ID and user_id not in admdict or user_id == TG_ID and user_id not in admdict:  # !!!!!!!!!!!!!!!! eto bez dannix
        cur.execute(first_insert.format(user_id, 1))
        connect.commit()

        knopka_lang = [
            InlineKeyboardButton(text='РУС🇷🇺', callback_data='ru'),
            InlineKeyboardButton(text='UZB🇺🇿', callback_data='uz'),
            InlineKeyboardButton(text='УЗБ🇺🇿', callback_data='xuzb')
        ]
        context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni tanglang:\nТилни танланг:',
                                 reply_markup=InlineKeyboardMarkup([knopka_lang]))

    if user_id in admdict :
        cur.execute(first_insert.format(user_id, 1))
        connect.commit()

        knopka_lang = [
            InlineKeyboardButton(text='РУС🇷🇺', callback_data='ru'),
            InlineKeyboardButton(text='UZB🇺🇿', callback_data='uz'),
            InlineKeyboardButton(text='УЗБ🇺🇿', callback_data='xuzb')
        ]
        context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni tanglang:\nТилни танланг:',
                                 reply_markup=InlineKeyboardMarkup([knopka_lang]))

        cur.execute(stagee.format('{}', user_id).format(100))
        connect.commit()
def next_func(update, context):
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    user_id = update.message.chat_id

    m_id = update.message.message_id
    f_name = update.message.from_user.first_name
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    a_name = cur.execute(select_name.format(user_id)).fetchall()
    edu = cur.execute(select_EDU.format(user_id)).fetchall()
    p_num = cur.execute(select_num.format(user_id)).fetchall()
    l = cur.execute(select_TT.format(user_id)).fetchall()
    status = cur.execute(select_STATUS.format(user_id)).fetchall()
    qjob = cur.execute(select_QJOB.format(user_id)).fetchall()
    xjob = cur.execute(select_EXJOB.format(user_id)).fetchall()
    connect.commit()
    print(m_id)
    try:

        stage_ = stage_[0][0]
        lang_ = lang_[0][0]
        a_name = a_name[0][0]
        pnum_ = p_num[0][0]
        edu = edu[0][0]
        qjob = qjob[0][0]
        l = l[0][0]
        xjob = xjob[0][0]
        status = status[0][0]

    except Exception:
        pass

    message = update.message.text
    message = str(message)

    if stage_ == 2:
        x = 0

        for s in message:
            res = repr(s), any(c.isspace() for c in s)
            if res[1] == True:
                x += 1

        if x >= 2:
            print(x)
            message1 = update.message.text
            cur.execute(upd_name.format(message1, user_id))
            connect.commit()

            cur.execute(stagee.format('{}', user_id).format(6))
            connect.commit()
            context.bot.send_message(chat_id=user_id, text=dct[lang_][0], parse_mode='Markdown')
        else:
            context.bot.send_message(chat_id=user_id, text=dct[lang_][2], parse_mode='Markdown')

    try:
        stag_ = cur.execute(stage.format(user_id)).fetchall()
        stag_ = stag_[0][0]
    except Exception:
        pass

    message = str(message)
    if stage_ == 4 and len(message) == 9:
        cur.execute(update_phone_num.format(int(message), user_id))
        connect.commit()
        cur.execute(stagee.format('{}', user_id).format(6))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text=dct[lang_][0])
    elif stage_ == 4 and len(message) != 9:
        context.bot.send_message(chat_id=user_id, text=dct[lang_][39])

    if stage_ == 6:
        try:
            year = int(message[0:4])
            month = int(message[5:7])
            day = int(message[8:])

            if stage_ == 6 and 1900 < year < 2022 and month < 13 and day < 32 and message[4] == '.' and message[7] == '.':
                cur.execute(stagee.format('{}', user_id).format(7))
                cur.execute(upd_BB.format( message ,user_id))
                connect.commit()
                connect.commit()
                knbutton1 = [KeyboardButton(rbdct[lang_][0]),KeyboardButton(rbdct[lang_][1])]

                context.bot.send_message(chat_id=user_id, text=dct[lang_][3],reply_markup=ReplyKeyboardMarkup([ knbutton1], resize_keyboard=True))
            else:
                context.bot.send_message(chat_id=user_id, text=dct[lang_][1])

        except Exception:
            context.bot.send_message(chat_id=user_id, text=dct[lang_][1])

    if stage_ == 7 and message not in rbdct[lang_]:
        context.bot.send_message(chat_id=user_id, text=dct[lang_][26])

    if stage_ == 8 and message == dct[lang_][28]:
        knbutton1 = [KeyboardButton(rbdct[lang_][0]), KeyboardButton(rbdct[lang_][1])]

        context.bot.send_message(chat_id=user_id, text=dct[lang_][3],
                                 reply_markup=ReplyKeyboardMarkup([knbutton1], resize_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(7))
        connect.commit()
    if stage_ == 7 and message==rbdct[lang_][0]:

        cur.execute(upd_DOMTYPE.format( '{}', user_id).format(message))
        cur.execute(stagee.format('{}', user_id).format(8))
        connect.commit()
        tovar_list = []
        tovar_list.append(str(rdct[message]))
        buttons = []

        def func_chunks_generators(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i: i + n]

        tovar_list = func_chunks_generators(rdct[message], 2)

        for e in tovar_list:
            b = []

            for k in e:
                k = k
                a = KeyboardButton(text=str(k))
                b.append(a)
            buttons.append(b)
        buttons.insert(0,[KeyboardButton(text=dct[lang_][28])])


        context.bot.send_message(chat_id=user_id, text=dct[lang_][3],
                                 reply_markup=ReplyKeyboardMarkup(buttons,
                                                                  resize_keyboard=True))
    bl = []
    for e in rdct.keys():
        bl.append(e)
        for i in rdct[e]:
            bl.append(i)


    if stage_ ==8 and message not  in bl  and message!=dct[lang_][28] :
        context.bot.send_message(chat_id=user_id, text=dct[lang_][26])
    bl.clear()

    if stage_ == 7 and message==rbdct[lang_][1]:

        cur.execute(upd_DOMTYPE.format( '{}', user_id).format(message))
        cur.execute(stagee.format('{}', user_id).format(8))
        connect.commit()
        tovar_list = []
        tovar_list.append(str(rdct[message]))
        buttons = []
        tovar_list = tovar_list[0]

        def func_chunks_generators(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i: i + n]

        tovar_list = func_chunks_generators(rdct[message], 2)

        for e in tovar_list:
            b = []
            for k in e:
                k = k
                a = KeyboardButton(text=str(k))
                b.append(a)
            buttons.append(b)
        buttons.insert(0,[KeyboardButton(text=dct[lang_][28])])

        context.bot.send_message(chat_id=user_id, text=dct[lang_][4],
                                 reply_markup=ReplyKeyboardMarkup(buttons,
                                                                  resize_keyboard=True))

    job = cur.execute("""SELECT {} FROM J WHERE {}!=0 """.format(l, l)).fetchall()
    xxx = []
    try:
        for e in job:
            xxx.append(e[0])

    except Exception:
        pass

    if stage_==8 and message in all_but or  stage_ == 8.7 and message not in xxx:

        cur.execute(upd_DOM.format(message, user_id))
        cur.execute(stagee.format('{}', user_id).format(8.7))
        connect.commit()
        job = cur.execute("""SELECT {} FROM J WHERE {}!=0 """.format(l, l)).fetchall()
        tovar_list =[]
        tovar_list.append(job)
        print(tovar_list)

        buttons = []

        tovar_list = tovar_list[0]

        def func_chunks_generators(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i: i + n]

        tovar_list = func_chunks_generators(tovar_list, 2)



        for e in tovar_list:
            print()
            b = []
            for k in e:

                k = k[0]
                a = KeyboardButton(text=str(k))
                b.append(a)
            buttons.append(b)
        context.bot.send_message(chat_id=user_id, text=dct[lang_][5],
                parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))





    if stage_ == 8.7 and message in xxx:
        cur.execute(stagee.format('{}', user_id).format(9))
        connect.commit()

        cur.execute(upd_LAV.format(message, user_id))
        connect.commit()
        but = ([KeyboardButton(text=dct[lang_][7])], [KeyboardButton(text=dct[lang_][8])], [KeyboardButton(text=dct[lang_][9])] )
        context.bot.send_message(chat_id=user_id, text=dct[lang_][10],
                                 parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup(but,
                                                                  resize_keyboard=True))
    if stage_ ==9 and message in dct[lang_][7:10]:
        cur.execute(stagee.format('{}', user_id).format(10))
        connect.commit()
        cur.execute(upd_STATUS.format(message, user_id))
        connect.commit()
        but = [KeyboardButton(text=dct[lang_][11]), KeyboardButton(text=dct[lang_][12]), KeyboardButton(text=dct[lang_][13]), KeyboardButton(text=dct[lang_][14])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][15], parse_mode='Markdown', reply_markup=ReplyKeyboardMarkup([but], resize_keyboard=True))

    if stage_ == 10 and message in dct[lang_][11:16] and status in dct[lang_][7:9]:
        cur.execute(stagee.format('{}', user_id).format(9.2))
        connect.commit()

        cur.execute(upd_EDU.format(message, user_id))
        connect.commit()
        but = [KeyboardButton(text=dct[lang_][11]), KeyboardButton(text=dct[lang_][12]), KeyboardButton(text=dct[lang_][13]), KeyboardButton(text=dct[lang_][14])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][16], parse_mode='Markdown', reply_markup=ReplyKeyboardRemove([but], resize_keyboard=True))

    if stage_ == 10 and message in dct[lang_][11:16] and status == dct[lang_][9]:
        cur.execute(stagee.format('{}', user_id).format(9.7))
        connect.commit()
        cur.execute(upd_EDU.format(message, user_id))
        connect.commit()
        but = [KeyboardButton(text=dct[lang_][11]), KeyboardButton(text=dct[lang_][12]), KeyboardButton(text=dct[lang_][13]), KeyboardButton(text=dct[lang_][14])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][17], parse_mode='Markdown', reply_markup=ReplyKeyboardRemove([but], resize_keyboard=True))
    if 9<stage_ <10 and message!= '11':
        if stage_ ==  9.2:
            cur.execute(upd_DOM1.format(message, user_id))
            connect.commit()
        if stage_ == 9.7:
            cur.execute(upd_EDUPLACE1.format(message, user_id))
            connect.commit()
        but = [KeyboardButton(text='0'), KeyboardButton(text='1'), KeyboardButton(text='2'), KeyboardButton(text='3'), KeyboardButton(text='4'), KeyboardButton(text='5+')]
        cur.execute(stagee.format('{}', user_id).format(11))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text=dct[lang_][18], parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([but],
                                                                  resize_keyboard=True))
    x = [1, 2 , 3, 4]

    if stage_ == 11 and message in str(x) or stage_ == 11 and message in '5+':
        cur.execute(upd_QJOB.format(message, user_id))
        connect.commit()
        but = [KeyboardButton(text='0'), KeyboardButton(text='1'), KeyboardButton(text='2'), KeyboardButton(text='3'),
               KeyboardButton(text='4'), KeyboardButton(text='5+')]
        cur.execute(stagee.format('{}', user_id).format(12))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text=dct[lang_][19], parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardRemove([but],
                                                                  resize_keyboard=True))
    if stage_ == 11231 and message == '0':
        cur.execute(upd_QJOB.format(message, user_id))
        connect.commit()

        cur.execute(stagee.format('{}', user_id).format(12))
        connect.commit()
        but = [KeyboardButton(text='0'), KeyboardButton(text='1'), KeyboardButton(text='2'), KeyboardButton(text='3'),
                   KeyboardButton(text='4'), KeyboardButton(text='5+')]

        context.bot.send_message(chat_id=user_id, text=dct[lang_][19], parse_mode='Markdown',
                                     reply_markup=ReplyKeyboardRemove([but],
                                                                      resize_keyboard=True))
    y = ['0','1','2','3','4','5+']


    if stage_ ==11 and message == '0':

        if status==dct[lang_][8]:
            cur.execute(upd_QJOB.format(message, user_id))


            cur.execute(stagee.format('{}', user_id).format(13.4))
            connect.commit()
            job = cur.execute("""SELECT {} FROM Job_But WHERE  {} !=0 """.format(l, l)).fetchall()
            tovar_list = []
            tovar_list.append(job)
            buttons = []
            tovar_list = tovar_list[0]

            def func_chunks_generators(lst, n):
                for i in range(0, len(lst), n):
                    yield lst[i: i + n]

            tovar_list = func_chunks_generators(job, 2)

            for e in tovar_list:
                b = []
                for k in e:
                    k = k[0]
                    a = KeyboardButton(text=str(k))
                    b.append(a)
                buttons.append(b)
            context.bot.send_message(chat_id=user_id, text=dct[lang_][20], parse_mode='Markdown',
                                     reply_markup=ReplyKeyboardMarkup(buttons,
                                                                      resize_keyboard=True))

        if status != dct[lang_][8]:
            cur.execute(upd_QJOB.format(message, user_id))
            cur.execute(stagee.format('{}', user_id).format(13))
            connect.commit()
            but = [KeyboardButton(text='0'), KeyboardButton(text='1'), KeyboardButton(text='2'),
                   KeyboardButton(text='3'), KeyboardButton(text='4'), KeyboardButton(text='5'), ]
            but2 = [KeyboardButton(text='6'), KeyboardButton(text='7'), KeyboardButton(text='8'),
                    KeyboardButton(text='9'), KeyboardButton(text='10')]
            context.bot.send_message(chat_id=user_id, text=dct[lang_][21], parse_mode='Markdown',
                                     reply_markup=ReplyKeyboardMarkup([but, but2],
                                                                      resize_keyboard=True))

    if stage_ ==12 and message!='qq' and status == dct[lang_][8]:
        if qjob !='0':
            cur.execute(upd_EXJOB.format(message, user_id))
            connect.commit()
        cur.execute(stagee.format('{}', user_id).format(13.4))
        connect.commit()
        job = cur.execute("""SELECT {} FROM Job_But WHERE  {} !=0 """.format(l,l)).fetchall()
        tovar_list = []
        tovar_list.append(job)
        buttons = []
        tovar_list = tovar_list[0]

        def func_chunks_generators(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i: i + n]

        tovar_list = func_chunks_generators(job, 2)

        for e in tovar_list:
            b = []
            for k in e:
                k = k[0]
                a = KeyboardButton(text=str(k))
                b.append(a)
            buttons.append(b)
        context.bot.send_message(chat_id=user_id, text=dct[lang_][20], parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup(buttons,
                                                                  resize_keyboard=True))



    if stage_ == 13.4 and message in rlist:
        cur.execute("""UPDATE JOBSTAGE SET STATUS = 1 WHERE  TG_ID = "{}" """.format(user_id))
        connect.commit()
        check = cur.execute("""SELECT JOB FROM JOBSTAGE WHERE TG_ID = '{}' """.format(user_id)).fetchall()
        checklist = []
        for c in check:
            checklist.append(c[0])
        job = cur.execute("""SELECT {} FROM Job_But WHERE {} != 0 """.format(l, l)).fetchall()
        for e in job:

            if e[0] == message:
                for i in job:
                    if e[0] != i[0] and i[0] not in checklist:
                        cur.execute(first_insertjs.format(user_id, i[0], 1))
                        connect.commit()
                    elif e[0] == i[0] and i[0] not in checklist:
                        cur.execute(first_insertjs.format(user_id, e[0], 2))
                        connect.commit()
                    elif e[0] == i[0] and i[0] in checklist:
                        cur.execute(
                            """UPDATE JOBSTAGE SET STATUS = "{}" WHERE TG_ID = "{}" AND JOB = "{}" """.format("2",
                                                                                                              user_id,
                                                                                                              message))
                        connect.commit()

        check = cur.execute(
            """SELECT JOB FROM JOBSTAGE WHERE TG_ID = '{}' AND STATUS ='{}' """.format(user_id, 1)).fetchall()
        checklist = []
        check2 = cur.execute(
            """SELECT JOB FROM JOBSTAGE WHERE TG_ID = '{}' AND STATUS ='{}' """.format(user_id, 2)).fetchall()

        for e in check:
            checklist.append(e[0])
        for e in check2:
            checklist.append('✅' + e[0] + '✅')
        checklist.sort()

        tovar_list = []
        tovar_list.append(checklist)

        buttons = []

        tovar_list = tovar_list[0]

        def func_chunks_generators(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i: i + n]

        tovar_list = func_chunks_generators(tovar_list, 2)

        for e in tovar_list:
            b = []
            for k in e:
                k = k
                print(k)
                a = KeyboardButton(text=str(k))
                b.append(a)
            buttons.append(b)

        buttons.append([KeyboardButton(text=dct[lang_][6])])

        context.bot.send_message(chat_id=user_id, text=dct[lang_][26][6:],
                                 parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup(buttons,
                                                                  resize_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(133))
        connect.commit()

    if stage_ == 133 and message in rlist:
        check = cur.execute(
            """SELECT JOB FROM JOBSTAGE WHERE TG_ID = '{}' AND STATUS ='{}' """.format(user_id, 1)).fetchall()
        checklist = []
        for e in check:
            checklist.append(e[0])
        print(checklist)
        print(message)
        if message in checklist:
            print(1)
            cur.execute("""UPDATE JOBSTAGE SET STATUS = "{}" WHERE TG_ID = "{}" AND JOB = "{}" """.format("2", user_id,
                                                                                                          message))
            connect.commit()
        check = cur.execute(
            """SELECT JOB FROM JOBSTAGE WHERE TG_ID = '{}' AND STATUS ='{}' """.format(user_id, 1)).fetchall()
        checklist = []
        check2 = cur.execute(
            """SELECT JOB FROM JOBSTAGE WHERE TG_ID = '{}' AND STATUS ='{}' """.format(user_id, 2)).fetchall()

        for e in check:
            checklist.append(e[0])
        for e in check2:
            checklist.append('✅' + e[0] + '✅')
            checklist.sort()
        tovar_list = []
        tovar_list.append(checklist)
        buttons = []

        tovar_list = tovar_list[0]

        def func_chunks_generators(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i: i + n]

        tovar_list = func_chunks_generators(tovar_list, 2)

        for e in tovar_list:
            b = []
            for k in e:
                k = k
                a = KeyboardButton(text=str(k))
                b.append(a)
            buttons.append(b)
        buttons.append([KeyboardButton(text=dct[lang_][6])])

        context.bot.send_message(chat_id=user_id, text=dct[lang_][26][6:],
                                 parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup(buttons,
                                                                  resize_keyboard=True))

    if stage_ == 133 and message[0] == '✅' and message[-1] == '✅':
        try:
            message = message[1:-1]
            cur.execute("""UPDATE JOBSTAGE SET STATUS = "{}" WHERE TG_ID = "{}" AND JOB = "{}" """.format("1", user_id,
                                                                                                          message))
            connect.commit()
        except Exception:
            pass
        check = cur.execute(
            """SELECT JOB FROM JOBSTAGE WHERE TG_ID = '{}' AND STATUS ='{}' """.format(user_id, 1)).fetchall()
        checklist = []
        check2 = cur.execute(
            """SELECT JOB FROM JOBSTAGE WHERE TG_ID = '{}' AND STATUS ='{}' """.format(user_id, 2)).fetchall()

        for e in check:
            checklist.append(e[0])
        for e in check2:
            checklist.append('✅' + e[0] + '✅')
        checklist.sort()
        tovar_list = []
        tovar_list.append(checklist)
        buttons = []
        tovar_list = tovar_list[0]

        def func_chunks_generators(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i: i + n]

        tovar_list = func_chunks_generators(tovar_list, 2)

        for e in tovar_list:
            b = []
            for k in e:
                k = k
                a = KeyboardButton(text=str(k))
                b.append(a)
            buttons.append(b)
        buttons.append([KeyboardButton(text=dct[lang_][6])])
        context.bot.send_message(chat_id=user_id, text=dct[lang_][26][6:],
                                 parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup(buttons,
                                                                  resize_keyboard=True))

    if stage_ == 133 and message == dct[lang_][6] or stage_ == 13.5 and message!='0iok':
        cur.execute(stagee.format('{}', user_id).format(13))
        connect.commit()
        check2 = cur.execute(
            """SELECT JOB FROM JOBSTAGE WHERE TG_ID = '{}' AND STATUS ='{}' """.format(user_id, 2)).fetchall()
        checklist = []
        for e in check2:
            checklist.append(e[0])
        check = ','.join(checklist)
        cur.execute(upd_RJOB.format(check, user_id))
        cur.execute("""UPDATE JOBSTAGE SET STATUS = 1 WHERE  TG_ID = "{}" """.format(user_id))
        connect.commit()
        but = [KeyboardButton(text='0'), KeyboardButton(text='1'), KeyboardButton(text='2'), KeyboardButton(text='3'), KeyboardButton(text='4'), KeyboardButton(text='5'),]
        but2 = [KeyboardButton(text='6'), KeyboardButton(text='7'), KeyboardButton(text='8'), KeyboardButton(text='9'), KeyboardButton(text='10')]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][21], parse_mode='Markdown',
                                     reply_markup=ReplyKeyboardMarkup([but, but2],
                                                                      resize_keyboard=True))

    if stage_ == 12 and message!= 'qq' and status!=dct[lang_][8]:
        if qjob !='0'and status!=dct[lang_][8] and xjob==' ':
            cur.execute(upd_EXJOB.format(message, user_id))
            connect.commit()
        if message == '0':
            cur.execute(upd_QJOB.format(message, user_id))
            connect.commit()


        if xjob !=' ':
            cur.execute(upd_EXJOB.format(message, user_id))
            connect.commit()
        cur.execute(stagee.format('{}', user_id).format(13))
        connect.commit()
        but = [KeyboardButton(text='0'), KeyboardButton(text='1'), KeyboardButton(text='2'), KeyboardButton(text='3'), KeyboardButton(text='4'), KeyboardButton(text='5'),]
        but2 = [KeyboardButton(text='6'), KeyboardButton(text='7'), KeyboardButton(text='8'), KeyboardButton(text='9'), KeyboardButton(text='10')]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][21], parse_mode='Markdown',
                                     reply_markup=ReplyKeyboardMarkup([but, but2],
                                                                      resize_keyboard=True))



    checklist = ['0','1','2','3','4','5','6','7','8','9','10']





    if stage_ == 13.5 and message!='0iok':
        cur.execute(upd_RJOB.format('{}', user_id).format(message))
        cur.execute(stagee.format('{}', user_id).format(13))
        connect.commit()
        but = [KeyboardButton(text='0'), KeyboardButton(text='1'), KeyboardButton(text='2'), KeyboardButton(text='3'), KeyboardButton(text='4'), KeyboardButton(text='5'),]
        but2 = [KeyboardButton(text='6'), KeyboardButton(text='7'), KeyboardButton(text='8'), KeyboardButton(text='9'), KeyboardButton(text='10')]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][21], parse_mode='Markdown',
                                     reply_markup=ReplyKeyboardMarkup([but, but2],
                                                                      resize_keyboard=True))
    if stage_  == 13 and message in checklist:
        cur.execute(upd_LANGSTAGE.format('{}', user_id).format(message))
        cur.execute(stagee.format('{}', user_id).format(14))
        connect.commit()
        but = [KeyboardButton(text='0'), KeyboardButton(text='1'), KeyboardButton(text='2'), KeyboardButton(text='3'), KeyboardButton(text='4'), KeyboardButton(text='5'),]
        but2 = [KeyboardButton(text='6'), KeyboardButton(text='7'), KeyboardButton(text='8'), KeyboardButton(text='9'), KeyboardButton(text='10')]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][22], parse_mode='Markdown',
                                     reply_markup=ReplyKeyboardMarkup([but, but2],
                                                                      resize_keyboard=True))
    if stage_ == 14 and message in checklist:
        cur.execute(upd_DOP2.format(message, user_id))
        connect.commit()
        but = [KeyboardButton(text='0'), KeyboardButton(text='1'), KeyboardButton(text='2'), KeyboardButton(text='3'), KeyboardButton(text='4'), KeyboardButton(text='5'),]
        but2 = [KeyboardButton(text='6'), KeyboardButton(text='7'), KeyboardButton(text='8'), KeyboardButton(text='9'), KeyboardButton(text='10')]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][23], parse_mode='Markdown',
                                     reply_markup=ReplyKeyboardRemove([but, but2],
                                                                      resize_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(15))
        connect.commit()
    elif stage_ ==14 and message not in checklist:
        context.bot.send_message(chat_id=user_id, text=dct[lang_][22], parse_mode='Markdown')


    if stage_ ==13 and message not in checklist:
        context.bot.send_message(chat_id=user_id, text=dct[lang_][21], parse_mode='Markdown')

    if stage_ == 15 and message == message:

        try:
           message = int(message)
           v= len(str(message))

           if 10>int(v)>8:

                      cur.execute(stagee.format('{}', user_id).format(16))
                      cur.execute(update_phone_num.format(message, user_id))
                      connect.commit()
                      but = [KeyboardButton(text='0'), KeyboardButton(text='1'), KeyboardButton(text='2'), KeyboardButton(text='3'), KeyboardButton(text='4'), KeyboardButton(text='5'),]
                      but2 = [KeyboardButton(text='6'), KeyboardButton(text='7'), KeyboardButton(text='8'), KeyboardButton(text='9'), KeyboardButton(text='10')]
                      context.bot.send_message(chat_id=user_id, text=dct[lang_][24], parse_mode='Markdown',
                                     reply_markup=ReplyKeyboardRemove([but, but2],
                                                                      resize_keyboard=True))
        except Exception:
            context.bot.send_message(chat_id=user_id, text=dct[lang_][23], parse_mode='Markdown')


    if stage_ == 16 and message == message:

        try:
            message = int(message)
            v= len(str(message))


            if 10>int(v)>8:

                cur.execute(stagee.format('{}', user_id).format(17))
                cur.execute(upd_S_NUM.format(message, user_id))
                connect.commit()
                context.bot.send_message(chat_id=user_id, text=dct[lang_][25], parse_mode='Markdown')

        except Exception:
            context.bot.send_message(chat_id=user_id, text=dct[lang_][23], parse_mode='Markdown')



    if stage_ ==17 and message == message:
        context.bot.send_message(chat_id=user_id, text= dct[lang_][25])


    admdict = []
    adm = cur.execute("""SELECT TG_ID FROM ADM WHERE TG_ID !=0""").fetchall()
    for e in adm:
        admdict.append(e[0])


# Admin   Panel
    if user_id in admdict and stage_ ==100 and message == maindct[lang_][0] or user_id in admdict and stage_ ==102 and message == maindct[lang_][0] :
        dd = [KeyboardButton(text='➕'+maindct[lang_][1]+'➕'),KeyboardButton(text='❌'+maindct[lang_][2]+'❌')]
        dd1 = [KeyboardButton(text=maindct[lang_][3])]
        context.bot.send_message(chat_id=user_id, text=maindct[lang_][0], reply_markup=ReplyKeyboardMarkup([dd,dd1], resize_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(101))
        connect.commit()


    if user_id in admdict and stage_ == 101 and message == maindct[lang_][3]:
        cur.execute(stagee.format('{}', user_id).format(700))
        connect.commit()
        dd = [KeyboardButton(text='➕'+maindct[lang_][1]+'➕'),KeyboardButton(text='❌'+maindct[lang_][2]+'❌')]
        dd1 = [KeyboardButton(text='➕'+maindct[lang_][3]+'➕')]
        context.bot.send_message(chat_id=user_id, text=maindct[lang_][4], reply_markup=ReplyKeyboardRemove([dd,dd1], resize_keyboard=True))
    if user_id in admdict and stage_ ==700 and message !='qwe':
        check1 = cur.execute("""SELECT TG_ID FROM ADM WHERE TG_ID  != 0""").fetchall()
        check= []
        for e in check1:
            check.append(e[0])
            print(check)
        try:
            message = int(message)

            if message not in check:
                cur.execute("""INSERT INTO ADM
                                          (TG_ID) 
                                           VALUES 
                                          ('{}')""".format(message))
                context.bot.send_message(chat_id=user_id, text='✅'+str(message)+'✅')
                dd = [KeyboardButton(text='➕' + maindct[lang_][1] + '➕'),
                      KeyboardButton(text='❌' + maindct[lang_][2] + '❌')]
                dd1 = [KeyboardButton(text=maindct[lang_][3])]
                context.bot.send_message(chat_id=user_id, text=maindct[lang_][0],
                                         reply_markup=ReplyKeyboardMarkup([dd, dd1], resize_keyboard=True))

                cur.execute(stagee.format('{}', user_id).format(101))
                connect.commit()
            if message in check:
                cur.execute("""
                DELETE  FROM ADM WHERE TG_ID = '{}'
                """.format(message))
                connect.commit()
                context.bot.send_message(chat_id=user_id, text='❌'+str(message)+'❌')
                dd = [KeyboardButton(text='➕' + maindct[lang_][1] + '➕'),
                      KeyboardButton(text='❌' + maindct[lang_][2] + '❌')]
                dd1 = [KeyboardButton(text=maindct[lang_][3])]
                context.bot.send_message(chat_id=user_id, text=maindct[lang_][0],
                                         reply_markup=ReplyKeyboardMarkup([dd, dd1], resize_keyboard=True))
                cur.execute(stagee.format('{}', user_id).format(101))
                connect.commit()
        except Exception:
            context.bot.send_message(chat_id=user_id, text=maindct[lang_][4])



    # UUUUUUUDDDDDDAAAAAAALLLLLLIIIITTTTTTT
    if user_id in admdict and stage_ ==101 and message == '❌'+maindct[lang_][2]+'❌'  or user_id in admdict and stage_ ==103.2 and message == '❌'+maindct[lang_][2]+'❌' or user_id in admdict and stage_ == 103.2 and message == '❌'+maindct[lang_][2]+'❌' :
        gg.clear()
        cur.execute(stagee.format('{}', user_id).format(102))
        connect.commit()
        tovar = cur.execute("""SELECT {} FROM J WHERE {} !=0 """.format(l,l))

        tovar_list = []

        price_list = []
        for e in tovar:
            price_list.append(e[0])
        tovar_list.append(price_list)

        buttons = []
        tovar_list = tovar_list[0]

        def func_chunks_generators(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i: i + n]

        tovar_list = func_chunks_generators(tovar_list, 2)

        for e in tovar_list:
            b = []
            for k in e:
                k = k
                a = KeyboardButton(text='❌'+str(k))
                b.append(a)
            buttons.append(b)
        buttons.insert(0,[KeyboardButton(text=maindct[lang_][0])])


        context.bot.send_message(chat_id=user_id, text=dct[lang_][0],
                                 reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
    if user_id in admdict and stage_==102 and message[0]=='❌' and message[-1]!='❌':
        gg.clear()
        cur.execute("""
        DELETE  FROM J WHERE {} = '{}'
        """.format(l, message[1:]))
        connect.commit()

        tovar = cur.execute("""SELECT {} FROM J WHERE {} !=0 """.format(l,l))


        tovar_list = []

        price_list = []
        for e in tovar:
            price_list.append(e[0])
        tovar_list.append(price_list)

        buttons = []
        tovar_list = tovar_list[0]

        def func_chunks_generators(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i: i + n]

        tovar_list = list(func_chunks_generators(tovar_list, 2))

        for e in tovar_list:
            b = []
            for k in e:
                k = k
                a = KeyboardButton(text='❌'+str(k))
                b.append(a)
            buttons.append(b)
        buttons.insert(0,[KeyboardButton(text=maindct[lang_][0])])
        context.bot.send_message(chat_id=user_id, text='🧹💨🗑', reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
    if message != '❌'+maindct[lang_][2]+'❌' and   user_id in admdict and stage_ == 101 and message == '➕'+maindct[lang_][1]+'➕' or user_id in admdict and stage_ == 103.2 and message == '➕'+maindct[lang_][1]+'➕':
        cur.execute(stagee.format('{}', user_id).format(103))
        connect.commit()
        gg.clear()

        sss = ['w']
        context.bot.send_message(chat_id=user_id, text='Введите название должности на русском:', reply_markup=ReplyKeyboardRemove([sss], resize_keyboard=True))
    message = update.message.text
    if  message != '❌'+maindct[lang_][2]+'❌' and  message!='➕'+maindct[lang_][1]+'➕' and stage_ ==103:
        cur.execute(stagee.format('{}', user_id).format(103.1))
        connect.commit()
        gg.append(message)

        context.bot.send_message(chat_id=user_id, text='''Lavozim nomini kiriting o'zbek tilida:''')
    message = update.message.text

    if message != '❌'+maindct[lang_][2]+'❌' and   message != '➕'+maindct[lang_][1]+'➕' and stage_ == 103.1 :
        gg.append(message)
        cur.execute(stagee.format('{}', user_id).format(103.2))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text='Enter the title of the job in English:')
    message = update.message.text
    if message != '❌'+maindct[lang_][2]+'❌' and  message != '➕'+maindct[lang_][1]+'➕' and stage_ == 103.2 :

        h = gg

        for e in h:
            if e !='❌'+maindct[lang_][2]+'❌':
               gg.append(message)
               cur.execute(first_insertjJJ.format(h[0],h[1],h[2]))
               connect.commit()
               cur.execute(stagee.format('{}', user_id).format(101))
               connect.commit()
               h.clear()
               dd = [KeyboardButton(text='➕'+maindct[lang_][1]+'➕'),KeyboardButton(text='❌'+maindct[lang_][2]+'❌')]
               dd1 = [KeyboardButton(text=maindct[lang_][3])]
               context.bot.send_message(chat_id=user_id, text=maindct[lang_][0], reply_markup=ReplyKeyboardMarkup([dd,dd1], resize_keyboard=True))







def adm(update, context):
    user_id = update.message.chat_id
    text = update.message.caption
    photo_id = update.message.photo[-1].file_id
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    name = cur.execute(select_name.format(user_id)).fetchall()
    pnum = cur.execute(select_num.format(user_id)).fetchall()
    ppnum = cur.execute(select_S_NUM.format(user_id)).fetchall()
    bb = cur.execute(select_BB.format(user_id)).fetchall()
    domtype = cur.execute(select_DOMTYPE.format(user_id)).fetchall()
    dom  = cur.execute(select_DOM.format(user_id)).fetchall()
    dom1 = cur.execute(select_DOM1.format(user_id)).fetchall()
    wjob = cur.execute(select_LAV.format(user_id)).fetchall()
    status = cur.execute(select_STATUS.format(user_id)).fetchall()
    edu = cur.execute(select_EDU.format(user_id)).fetchall()
    qjob = cur.execute(select_QJOB.format(user_id)).fetchall()
    exjob = cur.execute(select_EXJOB.format(user_id)).fetchall()
    rjob = cur.execute(select_RJOB.format(user_id)).fetchall()
    langst = cur.execute(select_LANGSTAGE.format(user_id)).fetchall()
    slangst = cur.execute(select_DOP2.format(user_id)).fetchall()
    langtype = cur.execute(select_TT.format(user_id)).fetchall()
    uduplace = cur.execute(select_EDU.format(user_id)).fetchall()
    eduplace1 = cur.execute(select_EDUPLACE1.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    try:
        file = context.bot.getFile(photo_id)
        name  = name[0][0]
        pnum  = pnum[0][0]
        ppnum = ppnum[0][0]
        bb = bb[0][0]
        domtype  = domtype[0][0]
        dom  = dom[0][0]
        wjob  = wjob[0][0]
        status  = status[0][0]
        edu  = edu[0][0]
        uduplace = uduplace[0][0]
        qjob  = qjob[0][0]
        exjob  = exjob[0][0]
        rjob  = rjob[0][0]
        langst  = langst[0][0]
        slangst  = slangst[0][0]
        langtype  = langtype[0][0]
        eduplace1 = eduplace1[0][0]
        dom1  = dom1[0][0]
        lang_ = lang_[0][0]
    except Exception:
        pass
    but = [InlineKeyboardButton(text=dct[lang_][29], callback_data='start')]
    context.bot.send_message(chat_id=user_id, text=dct[lang_][27],
                                 reply_markup=InlineKeyboardMarkup([but]))

    file.download('{}.jpeg'.format(user_id))
    telegraph.create_account(short_name='1333')
    import requests
    with open(f'''{user_id}.jpeg''', 'rb') as f:
        path = requests.post('https://telegra.ph/upload', files={'file': ('file', f, 'image/jpеg')}).json()[0]['src']
        html = f'''

        <img src={path}/>



        '''

        response = telegraph.create_page(
            '{}'.format(user_id),
            html_content=html)
    import logging

    import requests
    SHEETY_ENDPOINT = 'https://api.sheety.co/cd5ffcb6d2166046577b57e44986fbf5/hrBot/prices'


    data = {
        "price": {
            "id": "{}".format(user_id),
            "rasm": "http://telegra.ph/{}".format(path),
            "fio": "{}".format(name),
            "tug`ilgansana": "{}".format(bb),
            "yashashjoyi": "{}".format(domtype),
            "yashashtumani": "{}".format(dom),
            "istalayotganlavozim": "{}".format(wjob),
            "status": "{}".format(status),
            "ma`lumoti": "{}".format(uduplace),
            "o`qiganjoyi": "{}".format(eduplace1),
            "o`qiyotganjoyi": "{}".format(dom1),
            "ishjoyisonlari":"{}".format(qjob),
            "ishjoyihaqida": "{}".format(exjob),
            "ishdanketishsababi": "{}".format(rjob),
            "ingiliztili": "{}".format(langst),
            "rustili": "{}".format(slangst),
            "telefon1": "{}".format(pnum),
            "telefon2": "{}".format(ppnum),
            "til": "{}".format(langtype),

        }
    }
    print(data)
    response = requests.post(url=SHEETY_ENDPOINT, json=data)
    logging.basicConfig()
    print("response.status_code =", response.status_code)
    print("response.text =", response.text)
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    try:
        lang_ = lang_[0][0]
        stage_ = stage_[0][0]
    except Exception:
        pass
    if stage_ == 17 :
        sleep(35)
        cur.execute("""DELETE FROM Users WHERE TG_ID = "{}" """.format(user_id))
        connect.commit()
        cur.execute(first_insert.format(user_id, 1))
        connect.commit()

        knopka_lang = [
            InlineKeyboardButton(text='РУС🇷🇺', callback_data='ru'),
            InlineKeyboardButton(text='UZB🇺🇿', callback_data='uz'),
            InlineKeyboardButton(text='УЗБ🇺🇿', callback_data='xuzb')
        ]
        context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni tanglang:\nТилни танланг:',
                                 reply_markup=InlineKeyboardMarkup([knopka_lang]))



def xuzb(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    lang_choose = cur.execute(lang.format('{}', user_id).format(3)).fetchall()
    cur.execute(upd_TT.format("{}", user_id).format("ENG"))

    connect.commit()
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    try:
        lang_ = lang_[0][0]
        stage_ = stage_[0][0]
    except Exception:
        pass
    if stage_ == 100:
        dd = [KeyboardButton(text='➕'+maindct[lang_][1]+'➕'),KeyboardButton(text='❌'+maindct[lang_][2]+'❌')]
        dd1 = [KeyboardButton(text=maindct[lang_][3])]
        context.bot.send_message(chat_id=user_id, text=maindct[lang_][0], reply_markup=ReplyKeyboardMarkup([dd,dd1], resize_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(101))
        connect.commit()
    if stage_ != 100:
         cur.execute(stagee.format('{}', user_id).format(2))
         connect.commit()
         k_but = [KeyboardButton(text='далее>>>')]
         context.bot.send_message(chat_id=user_id, text='Номзодлик анкетасини тўлдириш')
         context.bot.send_message(chat_id=user_id,
                             text='Фамилиянгиз, Исмингиз ва отангизни исмини қуйидаги кўринишда киритинг: \nРустамжонов Илхомжон Анвар ўғли', parse_mode='Markdown')
def ru(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    lang_choose = cur.execute(lang.format('{}', user_id).format(1)).fetchall()
    cur.execute(upd_TT.format("{}", user_id).format("RU"))

    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    try:
        lang_ = lang_[0][0]
        stage_ = stage_[0][0]
    except Exception:
        pass
    if stage_ == 100:

        dd = [KeyboardButton(text='➕'+maindct[lang_][1]+'➕'),KeyboardButton(text='❌'+maindct[lang_][2]+'❌')]
        dd1 = [KeyboardButton(text=maindct[lang_][3])]
        context.bot.send_message(chat_id=user_id, text=maindct[lang_][0], reply_markup=ReplyKeyboardMarkup([dd,dd1], resize_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(101))
        connect.commit()
    if stage_ != 100:
        cur.execute(stagee.format('{}', user_id).format(2))
        connect.commit()
        k_but = [KeyboardButton(text='далее>>>')]
        context.bot.send_message(chat_id=user_id, text='Заполнения анкеты кандидата')
        context.bot.send_message(chat_id=user_id,
                             text='Заполните ФИО в нижеследующем образце: \nРустамжанов Ильхом Анварович', parse_mode='Markdown')
    sleep(1)

    connect.commit()
def uz(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(2))

    cur.execute(upd_TT.format("{}", user_id).format("UZ"))
    connect.commit()
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    try:
        lang_ = lang_[0][0]
        stage_ = stage_[0][0]
    except Exception:
        pass
    if stage_ == 100:
        dd = [KeyboardButton(text='➕'+maindct[lang_][1]+'➕'),KeyboardButton(text='❌'+maindct[lang_][2]+'❌')]
        dd1 = [KeyboardButton(text=maindct[lang_][3])]
        context.bot.send_message(chat_id=user_id, text=maindct[lang_][0], reply_markup=ReplyKeyboardMarkup([dd,dd1], resize_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(101))
        connect.commit()
    if stage_ != 100:
       cur.execute(stagee.format('{}', user_id).format(2))
       connect.commit()
       k_but = [KeyboardButton(text='davom etish>>>')]
       context.bot.send_message(chat_id=user_id, text='Nomzodlik anketasini  to’ldirish')
       context.bot.send_message(chat_id=user_id,
                             text='Familiyangiz, Ismingiz va otangizni ismini quyidagi korinishda kiriting: \n_Rustamjonov Ilhomjon Anvar o’g’li_', parse_mode='Markdown')
    sleep(1)
    connect.commit()