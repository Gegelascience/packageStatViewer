from taipy.gui import Gui, Markdown

from pages.chartNpm.chartNpm import pageNpm_md
from pages.chartPypi.chartPypi import pagePypi_md
from pages.home.home import home_md

root = """
<|navbar|>
<|content|>
"""



pages = {
    "/":root,
    "home":home_md,
    "NPM": pageNpm_md,
    "Pypi": pagePypi_md
}



if __name__ == "__main__":
    
    guiApp =Gui(pages=pages)

    guiApp.run(title="Infos packages",use_reloader=True)
    