import os, sys
import getopt
from cleantext import clean

def clean_txt(filename=''):
    #print(filename)
    if not os.path.exists(filename):
        print('Couldn\'t find file in specified path!')
        exit(1)
    cleantxt = ''
    lines = []
    with open(filename, 'r') as _file:
        line = _file.readline()
        while line:
            line.replace('\n', ' ')
            cleantxt += line
            line = _file.readline()
        cleantxt = clean(cleantxt)
    lines = cleantxt.split('.')
    with open('clean-'+filename, 'w') as _file:
        for i in lines:
            _file.write(i)
            _file.write('.\n')

clean_txt(sys.argv[1])
