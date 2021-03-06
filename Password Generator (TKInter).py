import pyperclip
import random
import string
from tkinter import *

output_list = list()
s = output_list

numbers_imported = '0123456789'
symbols_imported = '#%$^&*!'

def listToString(s):
    str1 = ""

    for ele in s:
        str1 += ele

    return str1


class genGui:
    def __init__(self, master):
        self.master = master
        master.title('Password Generator')
        root.geometry("300x80")

        self.PassOutput_label = Label(text='')
        self.PassOutput_label.pack()

        self.GeneratorButton = Button(text='Generate Password', command=self.output_password)
        self.GeneratorButton.pack()

        self.Copy_Button = Button(text="Copy Password", command=self.copy_password)
        self.Copy_Button.pack()

    def output_password(self):
        output_list.clear()

        randomNumberOne = random.choice(numbers_imported)
        randomNumberTwo = random.choice(numbers_imported)
        randomNumberThree = random.choice(numbers_imported)
        randomNumberFour = random.choice(numbers_imported)

        randOneLower = random.choice(string.ascii_lowercase)
        randTwoLower = random.choice(string.ascii_lowercase)
        randThreeLower = random.choice(string.ascii_lowercase)
        randFourLower = random.choice(string.ascii_lowercase)

        randOneUpper = random.choice(string.ascii_uppercase)
        randTwoUpper = random.choice(string.ascii_uppercase)
        randThreeUpper = random.choice(string.ascii_uppercase)
        randFourUpper = random.choice(string.ascii_uppercase)

        randSymbolOne = random.choice(symbols_imported)
        randSymbolTwo = random.choice(symbols_imported)
        randSymbolThree = random.choice(symbols_imported)
        randSymbolFour = random.choice(symbols_imported)

        output_list.append(randomNumberOne)
        output_list.append(randomNumberTwo)
        output_list.append(randomNumberThree)
        output_list.append(randomNumberFour)

        output_list.append(randOneLower)
        output_list.append(randTwoLower)
        output_list.append(randThreeLower)
        output_list.append(randFourLower)

        output_list.append(randOneUpper)
        output_list.append(randTwoUpper)
        output_list.append(randThreeUpper)
        output_list.append(randFourUpper)

        output_list.append(randSymbolOne)
        output_list.append(randSymbolTwo)
        output_list.append(randSymbolThree)
        output_list.append(randSymbolFour)

        random.shuffle(output_list)

        printOutput = (listToString(s))

        self.PassOutput_label.config(text=printOutput)

    @staticmethod
    def copy_password():
        printOutput = (listToString(s))
        pyperclip.copy(printOutput)


root: Tk = Tk()
my_gui = genGui(root)
root.mainloop()
