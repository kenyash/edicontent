##this program parses throuh the edi
### this file is for personal use so i hard coded some aspects
### however for a 


def open_file_edi():
    """opens sample edi file with exception thrown if no file found"""
    with open('sf1.rtf', 'r') as edifile: #opening edi file
        edicontents = edifile.read() #saving contents to a list for parsing
    return edicontents


def remove_chars(file):
    """removing new lines and cariages"""
    chars_to_r = ["\n", "\\"]
    for i in range(len(file)):
        if file[i] in chars_to_r:
            file = file.replace(file[i], " ")
    return file

def split_line(file):
    """ splitting based on delimeter"""


            

        
    
