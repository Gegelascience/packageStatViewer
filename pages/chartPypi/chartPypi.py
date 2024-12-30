from taipy.gui import Markdown 
from helpers import pypiApiHelper



packagePypi = "pyEanGenerator"
dataPypi = {
    "day":[],
    "downloads":[]
}

def change_input(state):
    state.dataPypi = pypiApiHelper.getLast7daysDownloadPackage(state.packagePypi)


pagePypi_md = Markdown("chartPypi.md")