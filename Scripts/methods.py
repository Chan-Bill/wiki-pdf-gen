
class Methods:
    
    # Handling Error
    def error_message(self, message, enter):
        print(f'{message}')
        input(enter) 

    # Close Command
    def close(self):
        print('')
        input('Press ENTER to exit')