import tkinter as tk
from tkinter import ttk  
from ttkthemes import ThemedTk
from tkinter import messagebox
from tkinter import filedialog as fd
import files_compare
import subprocess
import time

class compare_sheets(object):
    def __init__(self):
        self.window = ThemedTk(theme="adapta")
        self.window.title("Excel Compare")
        self.window.geometry("650x300")
        self.window.minsize(450,200)
        self.window.configure(background="black")
        self.label = tk.Label(text="Compare two excel sheets".upper(),
                              background="black",
                              foreground="#4FFC6C"
                            )
        self.label.pack()
        self.progress_label = tk.Label(self.window)
        self.file1 = self.file2 = None
        self.comparator = files_compare.compare_sheets() #the file  comparing script
        self.pg = ttk.Progressbar(self.window,orient=tk.HORIZONTAL,length=200,cursor="spider",mode="indeterminate")
        self.pg["value"] = 0
    
    def select_sheet_from_computer(self,caller):
        """
            This method is called by the sheet buttons to select a sheet from pc
        """
        types = (
                ('Excel files', '*.xlsx'),
                ('All files', '*.*')
            )
        filename = fd.askopenfilename(filetypes=types)

        if caller == "sheet1":
            self.file1 = filename
        else:
            self.file2 = filename
        
        print("\nSelected file : \n {}\n".format(filename))
    
    def progress(self,value):
        """
            This method should show the progress bar
        """

        self.pg.place(relx=0.5, rely=0.9, anchor=tk.CENTER,height=20)
        self.progress_label.place(relx=0.5, rely=0.83, anchor=tk.CENTER)
        self.window.update()
        if value == 100:
            return
        self.pg["value"] = value
        self.progress_label.config(text=str(value)+"%")
        self.window.update()
        
        self.compare_command()

    def compare_command(self):
        """
            Perfom the comparison and update the progress by clicking compare_button
        """
        self.pg["value"] = 50
        self.progress_label.config(text=str(50)+"%")
        self.window.update_idletasks()
        print("\nCOMPARING....\n")
        output_file = self.comparator.compare_and_save(self.file1,self.file2)
        self.pg["value"] = 100
        self.progress_label.config(text=str(100)+"%")
        self.window.update_idletasks()
        time.sleep(2)

        # ask user if he wants to open the output file
        # if yes open it using excel
        view = messagebox.askquestion("DONE"," View comparison file?",icon="info")
        if view == "yes":
            subprocess.check_call(['open', '-a', 'Microsoft Excel', output_file])   
        
        done = messagebox.askquestion("EXIT?","Compare more files?")
        if done == "no":
            self.window.destroy()
        else:
            self.pg["value"] = 0
            self.window.update()

    def create_buttons(self):
        """
            This method creates the buttons and positions them in the window
        """
        sheet1 = ttk.Button(text="Upload Sheet 1",
                            command= lambda  : self.select_sheet_from_computer("sheet1"))
        sheet1.place(relx=0.2, rely=0.2, anchor=tk.NW)
        
        
        sheet2 = ttk.Button(text="Upload Sheet 2",
                            command= lambda  : self.select_sheet_from_computer("sheet2"))
        sheet2.place(relx=0.8, rely=0.2, anchor=tk.NE)

        compare_button = ttk.Button(text="Compare sheets",
                                    command= lambda : self.progress(25))
        compare_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        
        self.window.mainloop()

if __name__ == "__main__":
    show = compare_sheets()
    show.create_buttons()