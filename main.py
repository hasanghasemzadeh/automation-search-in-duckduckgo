import download_app_page as dl_app_scenario
from dotenv import load_dotenv

load_dotenv()


def do_it():
    try:
        dl_app_scenario.senario_execution()
    except Exception as err:
        print(str(err))
        return str(err)

do_it()    
