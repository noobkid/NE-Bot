import random
import urllib.request
import time
import winsound
import smtplib


#do you want the prompt to beep? (y/n)
allowSound = y
#do you want to be sent an email? (y/n)")
allowEmail = y
# if so then enther the following 
# enter email:
user = "'"
# enter password:
password = ""
# enter smtp server (check the internet, for example search gmail smtp or hotmail smtp)
smtpAddr = ""
# enter port (should be mentioned with smtp info, probably 587)
port = 587
#end of email input
# how long do you want the delay between each cycle to be (in seconds)
delay = 30
# for how many cycles do you want the bot to run?
cycles = 8460
# enter product link:
link = ["link1","link2"]
# enter name of the product
name = ['name1', 'name2']

#################### EMAIL ##############################


def notify(product, address):

    subject = "item is available"
    body= "%s - %s" %(product, address)

    sent_from = user
    to = user
    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    %s
    """ % (sent_from, to, subject, time.asctime(), body)

    try:
        server = smtplib.SMTP( smtpAddr, port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, user, email_text)
        server.quit()


    except:
        print ('Something went wrong...', error)

# notify("test1", "test2")


#################### CHECKER ##############################

# setting beep sounds varuables
frequency = 3000  # Set Frequency To 2500 Hertz
duration1 = 1000  # Set Duration To 1000 ms == 1 second
duration2 = 100  # Set Duration To 100 ms == 0.1 second


word = "SOLD OUT" # word to check
enWord = word.encode() # change to byte type for file scan
enConf = "Add to cart".encode()
found = 0 # check if missed a window

print('playing 1 second beep for system check')
winsound.Beep(frequency, duration1) # notify of start and check sound works


for i in range(cycles):               
    print(time.asctime(), "so far there were", found, "found out of", i, "tries")
    for product in range(len(link)):                                # for each product:
        x= product * random.uniform(0.1, 0.5)                   # brief random delay for anti-bot detection
        time.sleep(x)
        site = urllib.request.urlopen(link[product]).read() # fetch site source
        if enWord in site:                         # when sold out
            print(word, "-", link[product])
        else:                                       # when available
            if enConf in site:
                print("PRODUCT AVAILABLE!", "---", link[product])
                found = found + 1
                if (allowEmail == "y"):
                    notify(name[product] ,link[product]) # send mail
                if (allowSound == "y"):
                    winsound.Beep(frequency, duration1)     # long beep
                    time.sleep(0.5)
                    for x in range(product):                #burst beeps
                        winsound.Beep(frequency, duration2)
                        time.sleep(0.15)
    print("")
    time.sleep(delay)                                  # padding delay