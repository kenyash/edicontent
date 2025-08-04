##this program parses throuh the edi
### this file is for personal use so i hard coded some aspects



def open_file_edi():
    """opens file, returns the contents of the opened file"""
    with open('sf2.edi', 'r') as edifile: #opening edi file
        edicontents = edifile.read() #saving contents to a list for parsing
    return edicontents


def remove_chars(file):
    """takes file as argument
    removes new lines and cariages and
    returns modified file"""
    chars_to_r = ["\n", "\r"] 
    for char in chars_to_r:
        file = file.replace(char, "") #replaces, carriges and new lines in file with emptyspace
    return file

def declaring_seperators(file):
    """ takes file as an argument,
    finds both row and element delimeter,
    assumes file follows standard ansi x12 format
    returns a tuple of the seperators"""
    
    rowseperator = file[-1] #ansi x12 will usually have row delimeter as ending element on every file
    elementseperator = file[3] #ansi x12 will usually have file beginning with isa followed by row del
    print(f'This is row seperator {rowseperator}')
    print(f'This is element seperator {elementseperator}')
    nt=  (rowseperator, elementseperator)
    return nt


def spliting_by_row(file, row_delimiter):
    """takes file, and row delimiter as an argument
    splits based on row delimeter 
    prints rows, and item number split by delimeter returns nothing""" 
    split_row = file.split(row_delimiter) #splits based on row delimeter 
    for item, row in enumerate(split_row): #iterates through list based on row delimeter and indexes each item with enumerate
          print(row)
    print(split_row)
    return 
    
def del_split(file_content, row_delimiter, element_delimiter):
    """
    Takes a file, row delimiter, and element delimiter.
    
    Creates a list of rows, parses through each row, and grabs the header segment.
    It then prints the header segment, index of the segment, and the associated value.
    This function returns nothing but prints the formatted data.
    """
    rows = [row for row in file_content.split(row_delimiter) if row] # list comp of each row in file based on row_delimiter
    for row in rows:
        elements = row.split(element_delimiter) # split row_list based on element delimiter
        element_id = elements[0] # grabs the header segment 
        for idx, item in enumerate(elements): # iterates through the element delimited list and indexes each item with enumerate
            if idx == 0: # if beginning new row, then add a new line before it
                print('\n')
            print(f'{element_id} {idx:02d} {item}') # print id, index, and item itself
            
