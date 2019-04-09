import sys
def printWords(items):
    for eachitem in items:
        print(eachitem)

def main(argument):
    printWords(argument)
    print(sys.argv[0])

if __name__ == '__main__':
    main(sys.argv[1])
