
class Methods:
    # Loadbar
    def loadbar(self, iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
        percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
        if iteration == total:
            print()

    # Handling Error
    def error_message(self, message, enter):
        print(f'{message}')
        input(enter) 

    # Close Command
    def close(self):
        print('')
        input('Press ENTER to exit')