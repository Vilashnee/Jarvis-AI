import wolframalpha
client = wolframalpha.Client("8LJT2Q-UP4RWKLH7K")
res = client.query('temperature in Washington, DC on October 3, 2012')

import wikipedia
import PySimpleGUI as sg
import pyttsx3
engine = pyttsx3.init()
sg.theme('DarkRed')
layout = [  [sg.Text('Working on a secret project, are we, sir?')],
            [sg.Text('Enter a command'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('Jarvis 2.0', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking("Wolfram Result:" + wolfram_res, "Wikipedia Result:" + wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        res = client.query(values[0])
        wolfram_res=next(res.results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        res = client.query(values[0])
        wolfram_res = next(res.results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)
    engine.runAndWait()

window.close()