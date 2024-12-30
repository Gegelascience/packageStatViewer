from taipy.gui import Markdown 
from helpers import pypiApiHelper
from datetime import datetime,timedelta


packagePypi = "pyEanGenerator"
dataPypi = {
    "day":[],
    "downloads":[]
}

datesPypi = [(datetime.now() - timedelta(days=7)).date(), datetime.now().date()]


def change_input(state):
    state.dataPypi = pypiApiHelper.getTimedDownloadPackage(state.packagePypi, state.datesPypi[0], state.datesPypi[1])


pagePypi_md = Markdown("chartPypi.md")