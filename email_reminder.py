import time
import datetime as dt
import os, sendgrid, requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()
@sched.schedule_job('cron', day = date2[2], month = date2[1], year = date2[0], hour = time3[0], minute = time3[1])

try:
    #get user info
    name = input('Enter your name here: ')
    email = input('Enter your email address here: ')

    #set the reminder
    print('Set your reminder')
    title = input('What do you need to do? ')
    date1 = input('What date do you want the reminder? format = yyyy mm dd(e.g 2019 03 30) ')
    time1 = input('What time do you want the reminder? format = hh mm(e.g 15 30 ) ')
    date2 = date1.split()
    time3 = time1.split()
    time2 = [int(time3[0]), int(time3[1]), 00] 
    send_time = dt.datetime(int(date2[0]), int(date2[1]), int(date2[2]), int(time2[0]), int(time2[1]), int(time2[2]))
    time_float = send_time.timestamp() - time.time()

    #include limit of one week
    while time_float > 604800:
        print('Your reminder is too far')
        print('Reminder should be less than one week')
        date1 = input('What date do you want the reminder? format = yyyy mm dd(e.g 2019 03 30) ')
        time1 = input('What time do you want the reminder? format = hh mm(e.g 15 30) ')
        date2 = date1.split()
        time3 = time1.split()
        time2 = [int(time3[0]), int(time3[1]), 00] 
        send_time = dt.datetime(int(date2[0]), int(date2[1]), int(date2[2]), int(time2[0]), int(time2[1]), int(time2[2]))
        time_float = send_time.timestamp() - time.time()
except Exception as e:
    print(e)

#send mail
def send_reminder():
    body = '''
        Hi {name}, today is {date1}. Don't forget to {title} by {time1}
        '''
    message = Mail(
        from_email='adelajamustapha@gmail.com',
        to_emails=email,
        subject='Personal Reminder',
        plain_text_content=body.format(name = name, date1 = date1, title = title, time1 = time1))
    try:
        sg = SendGridAPIClient(os.environ['my_sendgrid_api'])
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
    
sched.start()