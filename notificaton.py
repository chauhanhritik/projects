from plyer import notification 
import time                        #for setting timer
while True:

    notification.notify(
        title = "this will be the title. ",
        message = "type your message here. ",
        timeout = 4                #how long the notification is supposed to be displayed
                       ) 
    time.sleep(10)                 #show the notification again after 10 seconds.
