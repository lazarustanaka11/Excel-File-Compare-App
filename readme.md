### File Compare App

 **TASK DESCRIPTION**

 - For a car manufacturer, it is important to know if the same sensor in different cars produce different  
      readings under the same conditions. The data is recorded in large files, for instance, excel files  
      or other types of files.
 - Given two identical excel files, write an application that compares for any differences in the cells.
 - If two identical columns have cells which do not have the same value, colour the cell red.
### Installation

- clone repository to desired location
- run ```pip install --upgrade pip```
- run ``` python3 -m venv <name_of_venv> ```
- activate  the venv using ``` source ./name_of_venv/bin/activate ```
- in the virtual environment install the packages in the requires.txt
- install ttkthemes using ``` python3 -m pip install git+https://github.com/RedFantom/ttkthemes ```    
- run ```pip install - e .``` from the root folder
### How to use
 - run ```python file_compare_app.py``` and supply the excel sheets to compare.
 - Example sheets and the result are found in the repository
 - Upload sheet1 and sheet2 from the computer and hit compare
 - This will create a new file called comparison.xlsx in the root folder, which can also be viewed after creation


