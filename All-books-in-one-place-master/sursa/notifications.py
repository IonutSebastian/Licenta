import datetime,pymsteams

teams = pymsteams.connectorcard("")#nu am aces sa fac bot pe team All books in one place
notification = True
saveLogFile = True

def succes(messege,teamsNotification=notification,save=saveLogFile):
    """
    funcţia trimit mesajele cu colora varde pe teams si salvaza in fisirul logfile mesagul + timpul in care o fost trimise
    :param messege:str vrut trimis
    :param notif: pt teams
    :param save: pt salvare in log file
    """
    messege =f'succes\t{messege}'
    if save:# sa salvaza in fisirul logfile
        file =open("data/logFile.txt",'a+')
        file.write(f'{datetime.datetime.now()}\t{messege}'+'\n\n\n')
        file.close()
    if teamsNotification:# trimitra mesajul pe teams
        teams.text(messege)
        teams.color("38832a")
        teams.send()

def warning(messege,teamsNotification=notification,save=saveLogFile):
    """
   funcţia trimit mesajele cu colora galbena pe teams si salvaza in fisirul logfile mesagul + timpul in care o fost trimise
    :param messege:str vrut trimis
    :param save: pt salvare in log file
    :return: nu returnaza nimic
    """

    messege =f'warning\t{messege}'
    if save:# sa salvaza in fisirul logfile
        file =open("data/logFile.txt",'a+')
        file.write(f'{datetime.datetime.now()}\t{messege}'+'\n\n\n')
        file.close()

    if teamsNotification:# trimitra mesajul pe teams
        teams.text(messege)
        teams.color("e6cf00")
        teams.send()

def error(messege,teamsNotification=notification,save=saveLogFile):
    """
   funcţia trimit mesajele cu colora rosu pe teams si salvaza in fisirul logfile mesagul + timpul in care o fost trimise
    :param messege:str vrut trimis
    :param save: pt salvare in log file
    :return: nu returnaza nimic

    """
    messege =f'error\t{messege}'

    if save:# sa salvaza in fisirul logfile
        file =open("data/logFile.txt",'a+')
        file.write(f'{datetime.datetime.now()}\t{messege}'+'\n\n\n')
        file.close()

    messege = messege[:1700] if len(messege) > 1700 else messege

    if teamsNotification:# trimitra mesajul pe teams
        teams.text(messege)
        teams.color("b71515")
        teams.send()

