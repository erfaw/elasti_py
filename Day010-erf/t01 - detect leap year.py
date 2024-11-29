from clear_sc import clear_screen

clear_screen()

def main():
    def leap_detector(year):
        """
        this is our Docstring
        """
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else: 
            return False


    result = leap_detector(
        int(input(
            'please input your year: \n'
        ))
    )
    print(result)

while True:
    main()
    if input(
        'retry? (y/n)'
    ).lower() != 'y':
        break