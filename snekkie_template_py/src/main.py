'''
Imports docstring: Explain why you need to import what you are importing
'''
def main() -> int:
    '''
    Function docstring: Explain what the main() function does. 
    '''
    return 0


while __name__ == '__main__':
    '''
    Docstring: Here the exit code is stored in the 'code' variable. The exit code is then evaluated in an if-elif-else block. Explain what each exit code means and what the program will do about it.
    '''
    code: int = main()
    if code == 0:  # Exit code 0 means that the program was successful
        break
    elif code == 1:  # Exit code 1 is a generic error. Not very detailed so make another exit code if you want to add more detail to the error, or if you want the program to do soemthing to handle the error itself.
        raise Exception("Exit code 1: Generic error.")
    else:  # If there was no exit code (make sure that the main() function returns an exit code
        raise Exception("No exit code.")
