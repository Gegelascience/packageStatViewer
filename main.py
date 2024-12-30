from taipy.gui import Gui

from pages.chartNpm.chartNpm import pageNpm_md
from pages.chartPypi.chartPypi import pagePypi_md

root = """
<|navbar|>
<|content|>
"""

explication = "## This is an app with taipy"

pages = {
    "/":root,
    "home":explication,
    "NPM": pageNpm_md,
    "Pypi": pagePypi_md
}



if __name__ == "__main__":
    
    guiApp =Gui(pages=pages)

    guiApp.run(title="Infos packages",use_reloader=True)
    