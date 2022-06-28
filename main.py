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

def convert_km_to_mile(value):
    return value * 0.621371

def convert_kg_to_pound(value):
    return value * 2.205

def convert_sec_to_min(value):
    return value / 60


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "-CONVERT-":
        user_input = float(values["-INPUT-"])
        conversion = values["-UNITS-"]
        if conversion == 'Km to mile':
            result = convert_km_to_mile(user_input)
        elif conversion == 'Kg to pound':
            result = convert_kg_to_pound(user_input)
        else:
            result = convert_sec_to_min(user_input)
        window["-OUTPUT-"].update(result)

window.close()