#!/usr/bin/env python3
''' convert file with formatted lines:
123.1 124.2 7
    to:
00.02.03 00.02.04 7
'''
import time, sys
def float2hhmmss(fstr):
    return time.strftime('%H.%M.%S', time.gmtime(int(fstr.split('.')[0])))

if __name__=='__main__':
    if len(sys.argv)!=3:
        print('example: python time_convert.py file_in.txt file_out.txt')
    else:
        fout = open(sys.argv[2], "w")
        with open(sys.argv[1], "r") as f:
            for row in (line.split() for line in f):
                fout.write(' '.join([ *(float2hhmmss(x) for x in row[:-1]), row[-1], '\n']))
        fout.close()
