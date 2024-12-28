from taipy.gui import Gui

from pages.chartNpm import pageNpm
#from pages.chartPypi import pagePypi

root = """
<|navbar|>
<|content|>
"""

explication = "## This is an app with taipy"

pages = {
    "/":root,
    "home":explication,
    "NPM": pageNpm,
#    "Pypi": pagePypi
}



if __name__ == "__main__":
    
    guiApp =Gui(pages=pages)

    guiApp.run(title="Infos packages",use_reloader=True)
    