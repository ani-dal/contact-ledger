import datetime
import logging

dateOfContact = input("Enter the date of contact: ")

logging.basicConfig(filename=str(dateOfContact)+".log", format='%(asctime)s %(msecs)d %(message)s',datefmt='%H:%M:%S',level=logging.INFO)

active = True

while active:

    usrName = input("Your Name: ")
    Cperson = input("The person you met: ")
    timeOfContact = input("The time of the day when you met this person: ")
    purpose = input("Purpose of this meeting? ")
    comments = input("Comments(if any): ")

    message = {
        "name":str(usrName),
        "Person of Contact":str(Cperson),
        "Time of contact":str(timeOfContact),
        "Purpose":str(purpose),
        "Comments":str(comments)
    }
    logging.info(message)
    """
    logging.info('Name: '+str(usrName))
    logging.info('Person Contacted: '+str(Cperson))
    logging.info('Time of Contact : '+str(timeOfContact))
    logging.info('Purpose: '+str(purpose))
    logging.info('Comments: '+str(comments))
    """
    
    warnFlag = input("Are there any warnings?(y/n) ")

    if warnFlag == 'y':
        logging.basicConfig(filename=str(dateOfContact)+".log", format='%(asctime)s %(msecs)d %(levelname)s %(message)s',datefmt='%H:%M:%S',level=logging.WARNING)
        warning = input("Enter warning: ")
        logging.warning(warning.upper())

    else:
        continue

    loopFlag = input("Is ther more?(y/n) ")

    if loopFlag == 'n':
        active = False
