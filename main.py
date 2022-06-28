import PySimpleGUI as sg

title = "Converter"
layout = [
            [
            sg.Input(key = '-INPUT-'),
            sg.Spin(['Km to mile', 'Kg to pound', 'sec to min' ], key = "-UNITS-"),
            sg.Button("Convert", key = "-CONVERT-")
            ],
            [sg.Text("Result", key = "-OUTPUT-")]
         ]
window = sg.Window(title, layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

        
window.close()