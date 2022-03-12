import FreeCAD, FreeCADGui
from PySide import QtGui, QtCore

class ExtrudeFeature:

   def Activated(self):
       print('Extrude Command')
       FreeCADGui.runCommand('Part_Extrude',0)

   def IsActive(self):
       if FreeCAD.ActiveDocument is None:
          return False
       else:
          return True

   def GetResources(self):
       return {'Pixmap': 'SWExtrude', 'MenuText':
                QtCore.QT_TRANSLATE_NOOP('SWPart', 'Extrude'), 'ToolTip':
                QtCore.QT_TRANSLATE_NOOP('SWPart', 'Extrude Object')}

FreeCADGui.addCommand('ExtrudeCommand',ExtrudeFeature())

