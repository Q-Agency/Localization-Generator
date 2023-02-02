import os
import csv
import json
from collections import defaultdict
import tkinter
from tkinter import Tk, filedialog
import pandas as pd
from openpyxl.styles import Alignment
import customtkinter
from PIL import Image


def select_folder():
    # Step 1: Create a GUI with a button to select or drag the "project_name" folder.
    global project_folder
    project_folder = filedialog.askdirectory(
        master=frame_1, title='Please select the "project_name" folder')
    translation_label = customtkinter.CTkLabel(
        master=frame_1, text=project_folder, font=customtkinter.CTkFont(size=12))
    translation_label.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)


def generateExcel():
    # Step 2: Upon selection or drag, extract the path of the "project_name" folder.
    l10n_folder = os.path.join(project_folder, 'lib', 'l10n')

    # Step 3: Create a list of all the .arb files in the "/lib/l10n" folder.
    arb_files = [f for f in os.listdir(l10n_folder) if f.endswith('.arb')]

    # Step 4: Open the "intl_en.arb" file first and parse its contents as a JSON object.
    data = defaultdict(list)
    global arb_data
    with open(os.path.join(l10n_folder, 'intl_en.arb'), 'r') as f:
        arb_data = json.load(f)
        for key, value in arb_data.items():
            data[key].append(value.strip())

    # Step 5: Iterate through the remaining .arb files and parse their contents as JSON objects.
    # Append the values with the same keys as a comma-separated string, and remove blank spaces.
    for arb_file in arb_files:
        if arb_file == 'intl_en.arb':
            continue
        with open(os.path.join(l10n_folder, arb_file), 'r') as f:
            arb_data1 = json.load(f)
            for key, value in arb_data.items():
                for key1, value1 in arb_data1.items():
                    if (key == key1):
                        data[key].append(value1.strip())
                        break
                    if (list(arb_data1)[-1] == key1):
                        data[key].append('')
                        continue
                    continue

    # Step 6: Write the contents of the `data` dictionary to a .csv file.
    # Use a comma-separated string for the values of each key, and remove blank spaces.
    with open(os.path.join(l10n_folder, 'translations.csv'), 'w', newline='') as f:
        # writer = csv.writer(f)
        for key, values in data.items():
            # Write each key-value pair as a separate row in the CSV file
            values = ';'.join(str(v).replace('"', '') for v in values)
            f.write(f"{key};{values}\n")

    df = pd.read_csv(os.path.join(
        l10n_folder, 'translations.csv'), delimiter=';')
    writer = pd.ExcelWriter(os.path.join(
        l10n_folder, 'translations.xlsx'), engine='openpyxl')
    df.to_excel(writer, index=False, sheet_name="Translations")
    # Get the worksheet from the writer
    sheet = writer.sheets['Translations']

    # Set the width of the first column to the maximum length of the values in that column
    sheet.column_dimensions['A'].width = max(
        [len(str(cell.value)) for cell in sheet['A']]) + 2

    # Set the width of the other columns
    for i, col in enumerate(df.columns[1:]):
        sheet.column_dimensions[chr(i + ord('B'))].width = 45

    # wrap text
    for row in sheet.iter_rows():
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical='center')

    writer.close()

    file = os.path.join(l10n_folder, 'translations.csv')
    if (os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)

    finished_label = customtkinter.CTkLabel(
        master=frame_1, text="You have successfully generated excel file", font=customtkinter.CTkFont(size=12))
    finished_label.place(
        relx=0.5, rely=0.91, anchor=tkinter.CENTER)


app = customtkinter.CTk()
app.geometry("400x280")
app.title("Arb to excel generator")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=0, padx=0, fill="both", expand=True)

image_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "../scripts")
image = customtkinter.CTkImage(Image.open(
    os.path.join(image_path, "q-image.png"),), size=(60, 60))

image_label = customtkinter.CTkLabel(master=frame_1, image=image, text="")
image_label.place(relx=0.5, rely=0.16, anchor=tkinter.CENTER)
label_1 = customtkinter.CTkLabel(
    master=frame_1, justify=tkinter.CENTER, text="ARB to Excel generator", font=customtkinter.CTkFont(size=24))
label_1.place(relx=0.5, rely=0.33, anchor=tkinter.CENTER)

select_button = customtkinter.CTkButton(
    master=frame_1, command=select_folder, text="Select project folder")
select_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


generate_button = customtkinter.CTkButton(height=40, width=200,
                                          master=frame_1, command=generateExcel, text="Generate", state="active")
generate_button.place(relx=0.5, rely=0.79, anchor=tkinter.CENTER)

app.mainloop()
