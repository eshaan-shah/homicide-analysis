'''
Authors: Eshaan Shah, Anindo Saha, Rohit Mudaliar
This py file is the Graphical User Interface
'''

import tkinter as tk
from helperForGUI import makePrediction

class GUI(tk.Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.vicSexFrame = tk.Frame(master)
        self.vicAgeFrame = tk.Frame(master)
        self.weaponFrame = tk.Frame(master)
        self.relFrame = tk.Frame(master)
        self.predFrame = tk.Frame(master)
        self.vicSexFrame.pack(side='left')
        self.vicAgeFrame.pack(side='left')
        self.weaponFrame.pack(side='left')
        self.relFrame.pack(side='left')
        self.predFrame.pack(side='left')
        self.pack()
        self.createWidgets()

    def predictCallback(self):
        '''
        callback for predict button
        :return:
        '''
        selSex=self.vicSex.curselection()[0]
        selAge=self.vicAge.curselection()[0]
        selWeapon=self.weaponList.curselection()[0]
        selRelation=self.relList.curselection()[0]
        sex1, sex2, age1, age2 = makePrediction(selSex, selAge, selRelation, selWeapon)
        self.predSexText.delete("1.0", "end")
        self.predSexText.insert("1.0", "Decision Tree: " + str(sex1) + "\n")
        self.predSexText.insert("end", "Adaboost: " + str(sex2))
        self.predAgeText.delete("1.0", "end")
        self.predAgeText.insert("1.0", "Decision Tree: " + str(age1) + "\n")
        self.predAgeText.insert("end", "Adaboost: " + str(age2))

    def createPrediction(self):
        '''
        creates the prediction panel
        :return:
        '''
        self.predLabel = tk.Label(self.predFrame, text="Predictions")
        self.predSexLabel = tk.Label(self.predFrame, text="Predicted Sex: ")
        self.predAgeLabel = tk.Label(self.predFrame, text="Predicted Age:")
        self.predButton = tk.Button(self.predFrame, text = "Click Here! ", command=self.predictCallback)
        self.predSexText = tk.Text(self.predFrame, height=2, width=25)
        self.predAgeText = tk.Text(self.predFrame, height=2, width=25)
        self.predLabel.pack()
        self.predButton.pack()
        self.predSexLabel.pack()
        self.predSexText.pack()
        self.predAgeLabel.pack()
        self.predAgeText.pack()

    def createRelationship(self):
        '''
        creates the relationship panel
        :return:
        '''
        self.relLabel = tk.Label(self.relFrame, text="Relationship")
        self.relList = tk.Listbox(self.relFrame, height=15, exportselection=0)
        self.relList.insert(tk.END, "Acquaintance")
        self.relList.insert(tk.END, "Wife")
        self.relList.insert(tk.END, "Stranger")
        self.relList.insert(tk.END, "Girlfriend")
        self.relList.insert(tk.END, "Ex-Husband")
        self.relList.insert(tk.END, "Brother")
        self.relList.insert(tk.END, "Stepdaughter")
        self.relList.insert(tk.END, "Husband")
        self.relList.insert(tk.END, "Sister")
        self.relList.insert(tk.END, "Friend")
        self.relList.insert(tk.END, "Family")
        self.relList.insert(tk.END, "Neighbor")
        self.relList.insert(tk.END, "father")
        self.relList.insert(tk.END, "In-Law")
        self.relList.insert(tk.END, "Son")
        self.relList.insert(tk.END, "Ex-Wife")
        self.relList.insert(tk.END, "Boyfriend")
        self.relList.insert(tk.END, "Mother")
        self.relList.insert(tk.END, "Common-Law Husband")
        self.relList.insert(tk.END, "Common-Law Wife")
        self.relList.insert(tk.END, "Stepfather")
        self.relList.insert(tk.END, "Stepson")
        self.relList.insert(tk.END, "Stepmother")
        self.relList.insert(tk.END, "Daughter")
        self.relList.insert(tk.END, "Boyfriend")
        self.relList.insert(tk.END, "Employer")
        self.relList.insert(tk.END, "Employee")
        self.relLabel.pack()
        self.relList.pack()

    def createWeapon(self):
        '''
        creates the weapon panel
        :return:
        '''
        self.weaponLabel = tk.Label(self.weaponFrame, text="Weapon Used")
        self.weaponList = tk.Listbox(self.weaponFrame, height=15, exportselection=0)
        self.weaponList.insert(tk.END, "Blunt Object")
        self.weaponList.insert(tk.END, "Strangulation")
        self.weaponList.insert(tk.END, "Rifle")
        self.weaponList.insert(tk.END, "Knife")
        self.weaponList.insert(tk.END, "Firearm")
        self.weaponList.insert(tk.END, "Shotgun")
        self.weaponList.insert(tk.END, "Fall")
        self.weaponList.insert(tk.END, "Handgun")
        self.weaponList.insert(tk.END, "Drowning")
        self.weaponList.insert(tk.END, "Suffocation")
        self.weaponList.insert(tk.END, "Explosives")
        self.weaponList.insert(tk.END, "Fire")
        self.weaponList.insert(tk.END, "Drugs")
        self.weaponList.insert(tk.END, "Gun")
        self.weaponList.insert(tk.END, "Poison")
        self.weaponLabel.pack()
        self.weaponList.pack()

    def createVicSex(self):
        '''
        creates the victim sex panel
        :return:
        '''
        self.vicSexLabel = tk.Label(self.vicSexFrame, text="Victim Sex")
        self.vicSex = tk.Listbox(self.vicSexFrame, height=2, exportselection=0)
        self.vicSex.insert(tk.END, "Male")
        self.vicSex.insert(tk.END, "Female")
        self.vicSexLabel.pack()
        self.vicSex.pack()

    def createVicAge(self):
        '''
        creates the victim age panel
        :return:
        '''
        self.vicAgeLabel = tk.Label(self.vicAgeFrame, text="Victim Age")
        self.vicAge = tk.Listbox(self.vicAgeFrame, height=10, exportselection=0)
        self.vicAge.insert(tk.END, "1-10")
        self.vicAge.insert(tk.END, "11-20")
        self.vicAge.insert(tk.END, "21-30")
        self.vicAge.insert(tk.END, "31-40")
        self.vicAge.insert(tk.END, "41-50")
        self.vicAge.insert(tk.END, "51-60")
        self.vicAge.insert(tk.END, "61-70")
        self.vicAge.insert(tk.END, "71-80")
        self.vicAge.insert(tk.END, "81-90")
        self.vicAge.insert(tk.END, "90+")
        self.vicAgeLabel.pack()
        self.vicAge.pack()

    def createWidgets(self):
        '''
        creates the widget
        :return:
        '''
        self.createVicSex()
        self.createVicAge()
        self.createWeapon()
        self.createRelationship()
        self.createPrediction()

root = tk.Tk()
app = GUI(master = root)
app.mainloop()
