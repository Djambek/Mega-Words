# import kivy module 
import kivy
import time
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
import random
# this restrict the kivy version i.e 
# below this kivy version you cannot 
# use the app or software 
kivy.require("1.9.1")

# base Class of your App inherits from the App class. 
# app:always refers to the instance of your application 
from kivy.app import App
f = open('slovar.txt', 'r', encoding="utf-8")
word = str(f.read())
word = word.split()
f.close()
'''for i in range(1, 5900):
    tmp = random.randint(0,len(word)-1)
    word.remove(word[tmp])
print(len(word))
#print(word)'''
#1500 and 900
# creates the button in kivy 
# if not imported shows the error 
from kivy.uix.button import Button
was_word = set()
# class in which we are creating the button 
class ButtonApp(App):
    #was_word.append(' ')
    df = 0

    def build(self):
        self.uncorrect = 0
        gl = GridLayout()
        self.correct_answer = 0
        self.text1 = word[random.randint(0, len(word)-1)]
        #was_word.append(self.text1)
        print (self.text1)
        #was_word.add(self.text1)
        self.l = Label(text=self.text1, pos = (350, 0), size = (10,160), font_size='30sp', color=(1,0,0,1)   )
        self.btn = Button(text='Не было',
             font_size="20sp",
             background_color=(1, 0, 0, 1),
             color=(1, 1, 1, 1),
             size=(100, 60),
             pos=(random.randint(50, 350),random.randint(100, 500)))
        gl.add_widget(self.btn)
        self.chek = Label(text = '',size = (10,160), pos = (150,0), font_size='25sp')
        self.answer = Label(text="Правильные ответы {}".format(self.correct_answer), size=(10, 160), pos=(600, 0), font_size='20sp')
        self.answer1 = Label(text="Неравильные ответы {}".format(self.uncorrect), size=(10, 160), pos=(600, -25),font_size='20sp')
        self.btn1 = Button(text='Было',
                      font_size="20sp",
                      background_color=(0, 1, 0, 1),
                      color=(1, 1, 1, 1),
                      size=(100, 60),
                      size_hint=(.2, .2),
                      pos=(random.randint(450, 550), random.randint(100, 500)))
        gl.add_widget(self.btn1)
        gl.add_widget(self.l)
        gl.add_widget(self.chek)
        gl.add_widget(self.answer)
        gl.add_widget(self.answer1)
    #    bind() use to bind the button to function callback
        self.btn.bind(on_press=self.callback)
        self.l.bind(on_press=self.callback)
        self.btn1.bind(on_press=self.callback1)

        return gl


# callback function tells when button pressed
    def callback(self, event):
        text = self.l.text
        tmp = random.randint(0, 1)
        if (tmp or len(was_word) == 0):
            self.l.text = word[random.randint(0, len(word) - 1)]
        else:
            self.l.text = random.choice(tuple(was_word))
        self.btn.pos = (random.randint(50, 350),random.randint(100, 500))
        self.btn1.pos = (random.randint(400, 500), random.randint(100, 500))
        if text in was_word:
            self.chek.text = 'Не угадал'
            self.uncorrect += 1
            self.answer1.text = 'Неправильные ответы: '+str(self.uncorrect)


        else:
            self.chek.text = 'Молодец'
            self.correct_answer += 1
            self.answer.text = 'Правильные ответы: '+str(self.correct_answer)
        print (was_word)
        was_word.add(text)



        '''if df == 0:
            print('Молодец')
            self.chek.text = 'Молодец'
        if df == 1:
            self.chek.text = 'Не угадал'

        print(was_word)
        '''
    def callback1(self, event):
        text = self.l.text
        tmp = random.randint(0, 1)
        if (tmp or len(was_word) == 0):
            self.l.text = word[random.randint(0, len(word)-1)]
        else:
            self.l.text = random.choice(tuple(was_word))
        self.btn.pos = (random.randint(50, 350),random.randint(100, 500))
        self.btn1.pos = (random.randint(400, 500), random.randint(100, 500))

        if text in was_word:
            print('Молодец')
            self.chek.text = 'Молодец'
            self.correct_answer +=1
            self.answer.text = 'Правильные ответы: '+str(self.correct_answer)

        else:
            self.chek.text = 'Не угадал'
            self.uncorrect += 1
            self.answer1.text = 'Неправильные ответы: '+str(self.uncorrect)
        print(was_word)
        was_word.add(text)






# creating the object root for ButtonApp() class
root = ButtonApp()

# run function runs the whole program
# i.e run() method which calls the target
# function passed to the constructor.
root.run()
