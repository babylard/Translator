# Imports
import PySimpleGUI as sg
from translate import Translator
import subprocess

# Functions
def translate_text(text, target_lang):
    translator = Translator(to_lang=target_lang)
    translation = translator.translate(text)
    return translation

def copy_to_clipboard(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

# GUI
sg.theme("Reddit")

def main():
    # List of languages
    language_options = ['English', 'Spanish', 'French', 'German', 'Italian', 'Chinese', 'Japanese', 'Korean', 'Russian', 'Arabic']

    layout = [  
        [sg.Text("Translate to:")],
        [sg.Combo(language_options, key="-LANG-")],
        [sg.Text("Input text:                                                              Output text:")],
        [sg.Multiline(key="-IN-", size=(40, 10)), sg.Output(key="-OUT-", size=(40, 10))],
        [sg.Button("Translate", key="-SUBMIT-"), sg.Button("Copy output to Clipboard", key="-COPY-")]
    ]

    window = sg.Window('Translator', layout)

    while True:
        event, values = window.Read()

        if event == sg.WIN_CLOSED:
            break
        elif event == '-SUBMIT-':
            target_lang = values["-LANG-"]
            input_text = values["-IN-"]

            # Clear the output element
            window['-OUT-'].update("")

            if target_lang and input_text:
                translated_text = translate_text(input_text, target_lang)
                print(f"{translated_text}")
        elif event == '-COPY-':
            # Use sg.OutputTextElement to get the value
            output_text = window['-OUT-'].get()
            copy_to_clipboard(output_text)

    window.Close()

# Program start
if __name__ == "__main__":
    main()