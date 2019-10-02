## The idea is to track a path you take in a maze/labryinth so you can remember how to get out##
## The idea came because I am an avid D&D player, and I wanted to find a way to practice python, and ##
## make something useful related to that ##

from breezypythongui import *

class PathTracker(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title= "Path Tracker")

        self.reportText = "{}{}".format("The path you took was: ", '\n')

        self.addLabel(text= "Please Choose a Direction:", row = 0, column =0)
        self.directionList = self.addListbox(row = 1, column = 0, columnspan= 2, rowspan= 2)
        self.directionlst = ["Left","Right","Straight","Backward"]
        self.directionList.insert(0, *self.directionlst)

        self.addLabel(text = "Please describe your travel", row = 0, column = 3)
        self.addLabel(text= "Distance traveled:", row = 1, column = 3)
        self.distanceValue = self.addIntegerField(value= "0", row = 1, column = 4)
        self.unitsList = self.addListbox(row = 4, column = 3, columnspan= 2, rowspan= 2)
        self.unitlist = ["Feet","Yards","Miles", "Meters","Kilometers"]
        self.unitsList.insert(0, *self.unitlist)
        self.addButton(text = "Report", row = 6, column = 2, command = self.reportButton)
        self.addButton(text = "Reset", row = 6, column = 3, command = self.resetButton)
        self.addButton(text = "Next", row = 6, column = 1, command= self.nextButton)
        self.guidetxt = "{}{}{}{}{}".format("Press next to add your travel", '\n',"Press report to see your total "
                                                                                  "travel", '\n',
                                            "Press reset to clear your report")
        self.guideText = self.addTextArea(text = '', row = 3, column = 0, columnspan= 2,
                                          rowspan= 3)
        self.guideText["state"] = "normal"
        self.guideText.setText(self.guidetxt)
        self.guideText["state"] = "disabled"

    def nextButton(self):
        numb = self.distanceValue.getNumber()
        direction = self.directionList.getSelectedItem()
        unit = self.unitsList.getSelectedItem()
        self.reportText += "{}{}{}{}{}{}".format(direction, " ",numb, " ",unit, '\n')
        self.distanceValue.setNumber(0)

    def reportButton(self):
        reportDialog(self, self.reportText)

    def resetButton(self):
        self.reportText = "{}{}".format("The path you took was: ", '\n')
        self.distanceValue.setNumber(0)


class reportDialog(EasyDialog):
    def __init__(self, parent, report):
        self.report = report
        EasyDialog.__init__(self,parent, "Travel Path Report")

    def body(self, parent):
        self.reportArea = self.addTextArea(parent, text = '', row = 0, column = 0, rowspan= 5, columnspan= 5)
        self.reportArea["state"] = "normal"
        self.reportArea.setText(self.report)
        self.reportArea["state"] = "disabled"

    def apply(self):
        pass



def main():
    PathTracker().mainloop()

if __name__ == "__main__":
    main()