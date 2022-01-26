from cmath import log
from msilib.schema import Error
import os
# import logging as lg

# Changing the directory to a particular location in local system
os.chdir(r'C:\Users\Omkar\Python_pr\OOPs')

class data:
    # this class collects the data and saves in multiple file

    def __init__(self, filename, filetype, date, size):
        '''
        __init__(filename, filetype, date, size) will take data for given self/variable.

        filname = a str data which contains name of the file.

        filetype = a str which contains type of file (.txt, .docx, etc)

        date = str in format of 'DD/MM/YYYY'

        size = int value which is size of that file
        
        '''
        self.filename = filename
        self.filetype = filetype
        self.date = date
        self.size = size

    def open_file(self):
        ''' 
        open_file() will create a txt file in present directory.
        This fucntion adds data in that file.
        It also checks wheather a file with same name already ezits in dir
        '''
        
        if os.path.isfile(self.filename):           # checks if file already exists in given dir
            return self.filename+ " alreay exists"
        else:
            f = open(self.filename, "w+")           #creates a file with given name in dir
            f.writelines("Omkar is good at comedy")
            f.close()
            return " file is created in dir"
    
            # self.lg(e)                  #Logs error messages 
        
        
           
    
    def file_read(self):
        '''
        file_read() will read  and return data from the file
        
        '''
    
        f =open(r'C:\Users\Omkar\Python_pr\OOPs'+"\\"+self.filename, "r")
        print(f.readlines())                    # reads data from file
        f.close()
        


    def file_append(self):
        '''
        file_append() will append data in existing file in dir
        
        '''
       

        f =open(r'C:\Users\Omkar\Python_pr\OOPs'+"\\"+self.filename, "a")       # opens existing file with given name in append for which enables file to add new data
        l = " This data is appended by function def file_append"
        f.write(l)
        f.close()
        return " Data succesfully appended in file "+ self.filename




# calling class and providing respective data

File_1 = data("omkar", ".txt", "25/01/2022", 10)
File_2 = data("Tushar", ".txt", "26/01/2022",12)
File_3 = data("Sushant", ".txt", "27/01/2022",20)
File_4 = data("Arihant", ".txt", "28/01/2022", 9)


# Using Functions to perform different operation

File_1.open_file()
File_1.file_read()
File_1.file_append()


File_2.open_file()
File_2.file_read()
File_2.file_append()


File_3.open_file()
File_3.file_read()
File_3.file_append()


File_4.open_file()
File_4.file_read()
File_4.file_append()
    
    

        
    

        