from plyer import notification 
import time
while True:

    notification.notify(
        title = "this will be the title. ",
        message = "type your message here. ",
        # app_icon = "C:\Users\NSC\Downloads\clock.ico"
        timeout = 4
                       ) 
    time.sleep(10)
