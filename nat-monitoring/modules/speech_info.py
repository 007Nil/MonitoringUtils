import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate',170)

def info_running_on_bat():
    engine.say(f'Device running on battery.')
    engine.runAndWait()
    engine.stop()
def alert_bat_critical(bat_threshold):
    engine.say(f'Battery threshold reached. Battery is less than {str(bat_threshold)}')
    engine.runAndWait()
    engine.stop()

def info_charger_connected():
    engine.say('Charger connected. Thank you')
    engine.runAndWait()
    engine.stop()

