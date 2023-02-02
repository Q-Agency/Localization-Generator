# Localization Generators 🌐

Easily convert your .arb files to .xlsx and vice versa with these two Python scripts.


### Requirements 📋

Before running the scripts, make sure you have installed the following libraries:

- Python 3.x
- os
- csv
- json
- collections
- Tkinter library (pre-installed in most Python installations)
- pandas
- openpyxl
- PIL

You can install the libraries by running the following command in your terminal:
```bash
pip install os csv json collections tkinter pandas openpyxl pillow
# or
pip3 install os csv json collections tkinter pandas openpyxl pillow
```

## Script 1: 'arb_to_excel.py'

This script helps you generate a translation file in .xlsx format from multiple .arb files in a project folder

Here is the example:
|Arb to Excel                                  |
|:-------------------------------------------: |
|![](arb_to_excel.gif) |

### How To Use 🚀
```bash
python arb_to_excel.py
# or
python3 arb_to_excel.py
```
This script contains functions to select the root of project folder, parse the ARB files, and generate Excel file. The following steps are performed:
1. Select the project folder
2. Extract the path of the project folder
3. Create a list of all .arb files in the "/lib/l10n" folder
4. Parse the contents of the "intl_en.arb" file as a JSON objectt
5. Parse the contents of the remaining .arb files as JSON objects and append them to the data dictionary
6. Convert the .arb files to an Excel file and save it in the "/lib/l10n" folder

## Script 2: 'excel_to_arb.py'

This script helps you generate multiple .arb files from an excel file. If a value doesn't exist, the corresponding key-value pair will not be present in the .arb file.

Here is the example:
|Excel to Arb                                  |
|:-------------------------------------------: |
|![](excel_to_arb.gif) |

### How To Use 🚀
```bash
python excel_to_arb.py
# or
python3 excel_to_arb.py
```
This script contains functions to select the excel file, select destination folder where .arb files will be saved. The steps taken by the script are:
1. Select the .xlsx file
2. Select the destination folder where .arb files will be sabed
3. Convert the excel file to a CSV file and then to a dictionary
4. Generate .arb files for different languages using the dictionary

 
# Contributors ✨

<a href="https://hr.linkedin.com/in/adrijanomicevic"><img src="https://media-exp1.licdn.com/dms/image/C4E03AQGrVjCdENO4Bg/profile-displayphoto-shrink_200_200/0/1648504265358?e=2147483647&v=beta&t=bZ5pols8a-FTl7Q4F6ADIbt4Hagl66Cg_5aS7eeT5Ig" width="100px;"><br /><sub><b>Adrijan Omićević</b></sub></a>

