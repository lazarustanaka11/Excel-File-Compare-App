"""
    - This file is used to compare two excell files and return the different cells
    
"""

import pandas as pd
import numpy as np
import argparse
import os

class compare_sheets(object):
    def __init__(self):
        pass

    def colour_cells(self,data,colour="red"):
        attr = 'background-color: {}'.format(colour)
        other = data.xs('sheet1', axis='columns', level=-1)
        return pd.DataFrame(np.where(data.ne(other, level=0), attr, ''),
                            index=data.index, columns=data.columns)
    
    def compare_and_save(self,file1,file2):
        table1 = pd.read_excel(file1)
        table2 = pd.read_excel(file2)

        df1 = pd.DataFrame(table1)
        df2 = pd.DataFrame(table2)

        sheets = [df1,df2]
        #concat the data frames horizontally and label each different sheet
        one_sheet = pd.concat(sheets,axis="columns",keys = ["sheet1","sheet2"])
        desitnation = "comparison.xlsx"

        one_sheet = one_sheet.swaplevel(axis='columns')[df1.columns[1:]]
        one_sheet = one_sheet.style.apply(self.colour_cells, axis=None)
        one_sheet.to_excel(desitnation)

        return desitnation
