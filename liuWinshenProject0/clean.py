import sys
import re

def clean(filename, no_comments=None):
    '''Takes file as input (format: 'filename.in'), removes whitespace, and
        writes to new file. Optional functionality to also remove comments'''

    try: # attempts to open file
        f = open(filename, 'r')
    except IOError:
        print('File not found. Please try again with an existing filename.')
    else:
        with f:
            # new file replaces '.in' with '.out' on original filename
            filename = filename.rstrip('in') + 'out'
            new_f = open(filename, 'w')

            for line in f:
                clean_line = line.replace(' ', '').replace('\n','') # removes whitespace
                if no_comments is not None:                         # removes comments
                    clean_line = re.sub('(//[\w\W]*)','', clean_line)

                if clean_line is not '':  # writes to new file if line is not blank
                    new_f.write(clean_line + '\n')

def main():
    user_input = sys.argv           # parses command line arguments
    if user_input[-1] == 'no-comments':     # determines if no-comments is the last term
        clean(user_input[1], user_input[-1])
    else:
        clean(user_input[1])

if __name__ == '__main__':
    main()
