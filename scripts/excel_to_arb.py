import pandas as pd
import json
import numpy as np
import os
from PIL import Image

import tkinter
from tkinter import filedialog

import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


def translation_button_event():
    global translation_file
    translation_file = filedialog.askopenfilename(
        filetypes=[("Excel file", "*.xlsx")])
    translation_label = customtkinter.CTkLabel(
        master=frame_1, text=translation_file, font=customtkinter.CTkFont(size=12))
    translation_label.place(relx=0.5, rely=0.48, anchor=tkinter.CENTER)


def directory_button_event():
    global directory_path
    directory_path = filedialog.askdirectory()
    directory_label = customtkinter.CTkLabel(
        master=frame_1, text=directory_path, font=customtkinter.CTkFont(size=12))
    directory_label.place(
        relx=0.5, rely=0.68, anchor=tkinter.CENTER)


def generate_button_event():

    excel_file = pd.read_excel(translation_file,)
    excel_file.to_csv("tmp.csv", index=None, header=True,
                      sep=";", encoding='utf-8')
    csv_file = pd.DataFrame(pd.read_csv(
        "tmp.csv", sep=";", index_col=0))

    file_with_removed_nan = csv_file.replace(np.nan, "")
    dictionary = file_with_removed_nan.to_dict(orient="dict")
    list_of_languages = pd.DataFrame.from_dict(
        dictionary, orient='columns').columns.tolist()

    for i in list_of_languages:
        filename = 'intl_' + str(i) + '.arb'
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'w', encoding='utf-8') as file:
            tmp_dict = {"@@locale": "{}".format(i)}
            tmp_dict.update(dictionary.get(i))
            dictionary.update()
            modifiedDict = {}
            for key, value in tmp_dict.items():
                if value != "":
                    modifiedDict[key] = value
            json.dump(modifiedDict, file, indent=2,
                      ensure_ascii=False,)

    file = os.path.join('tmp.csv')
    if (os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)

    finished_label = customtkinter.CTkLabel(
        master=frame_1, text="You have successfully generated .arb files", font=customtkinter.CTkFont(size=12))
    finished_label.place(
        relx=0.5, rely=0.93, anchor=tkinter.CENTER)


app = customtkinter.CTk()
app.geometry("500x350")
app.title("Excel to arb generator")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=0, padx=0, fill="both", expand=True)

image_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "../scripts")
image = customtkinter.CTkImage(Image.open(
    os.path.join(image_path, "q-image.png"),), size=(60, 60))

image_label = customtkinter.CTkLabel(master=frame_1, image=image, text="")
image_label.place(relx=0.5, rely=0.12, anchor=tkinter.CENTER)
label_1 = customtkinter.CTkLabel(
    master=frame_1, justify=tkinter.CENTER, text="EXCEL to ARB generator", font=customtkinter.CTkFont(size=24))
label_1.place(relx=0.5, rely=0.26, anchor=tkinter.CENTER)

translation_button = customtkinter.CTkButton(
    master=frame_1, command=translation_button_event, text="Select translation")
translation_button.place(relx=0.5, rely=0.38, anchor=tkinter.CENTER)

destination_button = customtkinter.CTkButton(
    master=frame_1, command=directory_button_event, text="Select destination")
destination_button.place(relx=0.5, rely=0.58, anchor=tkinter.CENTER)

generate_button = customtkinter.CTkButton(height=40, width=200,
                                          master=frame_1, command=generate_button_event, text="Generate", state="active")
generate_button.place(relx=0.5, rely=0.83, anchor=tkinter.CENTER)

app.mainloop()
