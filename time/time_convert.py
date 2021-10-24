#!/usr/bin/env python3
''' convert file with formatted lines:
123.1 222.5 7
    to:
00.02.03 7
'''
import time, sys
if __name__=='__main__':
    if len(sys.argv)!=3:
        print('example: python time_convert.py file_in.txt file_out.txt')
    else:
        fout = open(sys.argv[2], "w")
        with open(sys.argv[1], "r") as f:
            for row in (line.split() for line in f):
                fout.write(' '.join([time.strftime('%H.%M.%S', time.gmtime(int(row[0].split('.')[0]))),row[-1],'\n']))
        fout.close()
