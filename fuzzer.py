#!/usr/bin/python3.5

import os
import random
import argparse

def main():
        parser = argparse.ArgumentParser(description='fuzzy tool')
        parser.add_argument('--file', '-f', action='store', type=str, help='Which file need to be fuzzy')
        parser.add_argument('--count', '-c',action='store', type=int, help='How much bytes need to read')
        args = parser.parse_args()
        read_bytes = args.count
        filename = args.file

        fileSize = os.stat(filename).st_size
        if fileSize<=read_bytes:
                print("File size is too small, please decrease the read_bytes")
                return
        full_file=b''
        hFileRead = open(filename,'br')

        seek_read1 = random.randint(0,fileSize-read_bytes)
        seek_read2 = random.randint(0,fileSize-read_bytes)
        print(seek_read1, seek_read2)

        hFileRead.seek(seek_read1,0)
        temp_bytes1=hFileRead.read(read_bytes)
        hFileRead.seek(seek_read2,0)
        temp_bytes2=hFileRead.read(read_bytes)
        hFileRead.seek(0,0)
        full_file = hFileRead.read()
        hFileRead.close()

        hFileWrite = open(filename,'bw')
        if seek_read1<seek_read2:
                hFileWrite.write(full_file[:seek_read1])
                hFileWrite.write(temp_bytes2)
                hFileWrite.write(full_file[seek_read1+read_bytes:seek_read2])
                hFileWrite.write(temp_bytes1)
                hFileWrite.write(full_file[seek_read2+read_bytes:])
        else:
                hFileWrite.write(full_file[:seek_read2])
                hFileWrite.write(temp_bytes1)
                hFileWrite.write(full_file[seek_read2+read_bytes:seek_read1])
                hFileWrite.write(temp_bytes2)
                hFileWrite.write(full_file[seek_read1+read_bytes:])
        hFileWrite.close()
        del full_file
        del hFileRead
        del hFileWrite
        del seek_read1
        del seek_read2


if __name__ == '__main__':
        main()
