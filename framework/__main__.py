from framework.app import Application
from framework.configuration import Configuration
import os


if __name__ == "__main__":

    this_folder = os.path.dirname(os.path.abspath(__file__))
    init_file = os.path.join(this_folder, 'appsettings.ini')
    
    configuration = Configuration(init_file)
    app =  Application(configuration)
    app.start()




    