import sys

def text_reader(stdin_fil):

    lister_text = []

    while 'HELP' != set(stdin_fil.readline().strip()):
        lister_text.append(stdin_fil.readline().strip().split())
        #exit(0)
    return lister_text


print(text_reader(stdin_fil=sys.stdin))