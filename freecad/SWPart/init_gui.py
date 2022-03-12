import FreeCAD, FreeCADGui
import PartGui

from freecad.SWPart import SWCommands

def joinDir(path) :
    import os
    __dirname__ = os.path.dirname(__file__)
    return(os.path.join(__dirname__,path))


class SWPart_Workbench (FreeCADGui.Workbench):

    def __init__(self):
        self.__class__.Icon = joinDir("Resources/icons/SWPartWorkbench.svg")
        self.__class__.MenuText = "SWPart"
        self.__class__.ToolTip = "SWPart workbench"

    def Initialize(self):
        def QT_TRANSLATE_NOOP(scope, text):
            return text

        #import SWCommands
        commands=['ExtrudeCommand']

        toolbarcommands=['ExtrudeCommand']

        self.appendToolbar(QT_TRANSLATE_NOOP('Workbench','SWPart'),toolbarcommands)
        self.appendMenu('SWPart',commands)
        FreeCADGui.addIconPath(joinDir("Resources/icons"))
        FreeCADGui.addLanguagePath(joinDir("Resources/translations"))
        FreeCADGui.addPreferencePage(joinDir("Resources/ui/SWPart-base.ui"), \
                   "SWPart")

    def Activated(self):
        "This function is executed when the workbench is activated"
        print ("Workbench Activated")
        return


    def Deactivated(self):
        "This function is executed when the workbench is deactivated"
        return

    def GetClassName(self):
        return "Gui::PythonWorkbench"

FreeCADGui.addWorkbench(SWPart_Workbench())
