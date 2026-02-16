import FreeSimpleGUI as sg
import sys

layout0 = [
    [sg.Text("escreva o nome do arquivo que deseja ler: ")],
    [sg.InputText()],
    [sg.Button("ok")]

]

def cat(archive):
    try:
        with open (archive[0], "r") as r:
            dados = r.read()
            return dados
    except Exeption as e:
        print(e)
        sys.exit(1)
window = sg.Window("cat", layout0)

while True:
    event, archive = window.read()

    if event == "ok":
        data = cat(archive)
        exec2(data);
        break
    window.close()

    layout1 = [
        [sg.Text(data)],
        [sg.Button("exit")]
    ]


window1 = sg.Window("data", layout1)

while True:
    event1 = window1.read()

    if event1 == "exit":
        break
window1.close()


