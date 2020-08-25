# ---------------------------------------------------------------------------- #
# Title: Assignment07
# Description: Using Exceptions and Pickling
# ChangeLog (Who,When,What):
# GBiehl, 08.24.2020, Updated Assignment06 with new features
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.dat"  # The name of the binary data file
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
lstAdd = []   # A list with the requested new Task and Priority
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions
booExpMenu = False  #A Boolean to show shorter menu after first time

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "rb")
        pickle.load()
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        # TODO: Add Code Here! -- Completed
        dicRowF = {"Task": task, "Priority": priority}
        list_of_rows.append(dicRowF)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        # TODO: Add Code Here! Completed
        booTaskFound = False
        lstTemp = []
        for dicRowF in list_of_rows:
            if dicRowF['Task'].lower() == task.lower():
                booTaskFound = True
            else:
                lstTemp.append(dicRowF)
                list_of_rows = lstTemp
        if booTaskFound == False:
            print('No entry found. Check spelling.')
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        # TODO: Add Code Here! -- Completed
        objFile = open(file_name,'wb')
        for dicRowF in list_of_rows:
            pickle.dump(dicRowF["Task"] + ',' + dicRowF["Priority"] + '\n')
        objFile.close()
        return list_of_rows, 'Success'

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        if booExpMenu == False:                # Display the full menu
            """  Display a menu of choices to the user
    
            :return: nothing
            """
            print('''
            Menu of Options
            1) Add a new Task
            2) Remove an existing Task
            3) Save Data to File        
            4) Reload Data from File
            5) Exit Program
            ''')
            print()  # Add an extra line for looks
        else:                                   # Display the Express Menu
            print('Express Menu: 1-Add Task, 2-Remove Task, 3-Save to File, 4-Reload File, 5) Exit Program')

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        # TODO: Add Code Here! Completed
        strTaskF = str(input('What task should be added?: '))
        strPriorityF = str(input('What priority should it have?: '))
        return strTaskF, strPriorityF   # return task, priority

    @staticmethod
    def input_task_to_remove():
        # TODO: Add Code Here! Completed
        strTaskF = str(input('What task should be removed? '))
        return strTaskF

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.dat if it exists.
import pickle
Try:
    Processor.read_data_from_file(strFileName, lstTable)  # read file data
Except:
    print('No file found. Start with a task and value.')
    lstAdd = IO.input_new_task_and_priority()
    Processor.add_data_to_list(lstAdd[0], lstAdd[1], lstTable)
    IO.input_press_to_continue(strStatus)
    continue  # to show the menu
# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    booExpMenu = True
    strChoice = IO.input_menu_choice()  # Get menu option
    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        # TODO: Add Code Here -- Completed
        lstAdd = IO.input_new_task_and_priority()
        Processor.add_data_to_list(lstAdd[0], lstAdd[1], lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        # TODO: Add Code Here -- Completed
        strTask = IO.input_task_to_remove()
        lstTable = Processor.remove_data_from_list(strTask, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            # TODO: Add Code Here! Completed
            Processor.write_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            # TODO: Add Code Here! -- Completed
            Processor.read_data_from_file(strFileName, lstTable)  # read file data
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  #  Exit Program
        print("Goodbye!")
        break   # and Exit
