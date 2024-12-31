from taipy.gui import Markdown
from datetime import datetime, timedelta

from helpers import crateApiHelper

packageCrate = ""
versionsCrate = {
     "version":[],
     "rust":[]
}
dataDownloadCrate = {
    "day":[],
    "downloads":[]
}

def change_input(state):
    if state.packageCrate and len(state.packageCrate) > 0:
        state.dataDownloadCrate =crateApiHelper.getLastDownload(state.packageCrate)
        state.versionsCrate = crateApiHelper.getVersionsPackage(state.packageCrate)

pageCrate_md = Markdown("chartCrate.md")