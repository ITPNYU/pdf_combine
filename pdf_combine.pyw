#!/usr/bin/env python
# To combine multi PDFs in multi folders

import os
import shutil
from argparse import ArgumentParser
from glob import glob
from pyPdf import PdfFileReader, PdfFileWriter

def merge(path, output_filename):

    output = PdfFileWriter()
    os.chdir(path)

    for pdffile in glob('*.pdf'):
        if pdffile == output_filename:
            continue
        print("Parse '%s'" % pdffile)
        document = PdfFileReader(open(pdffile, 'rb'))
        for i in range(document.getNumPages()):
            output.addPage(document.getPage(i))

    print("Start writing '%s'" % output_filename)

    output_stream = file(output_filename, "wb")
    output.write(output_stream)
    output_stream.close()
    shutil.copy(output_filename,nowdir)

    print("--- END ---")

if __name__ == "__main__":

    nowdir = os.getcwd()


    parser = ArgumentParser()

    # Add more options if you like
    # parser.add_argument("-o", "--output", dest="output_filename", default="merged.pdf",
    #                   help="write merged PDF to FILE", metavar="FILE")
    parser.add_argument("-p", "--path", dest="path", default=".",
                      help="path of source PDF files")
    parser.add_argument("-r", "--recursive", dest="all_folders", default="false",
                      help="Apply for All folders?(true/false)", metavar="RECURSIVE")

    args = parser.parse_args()

    recur = args.all_folders.lower();
    
    if recur == "false":
        print "--- SINGLE MODE ---"
        merge(args.path, nowdir.split("/")[-1] + ".pdf")

    elif recur == "true":
        print "--- RECURSIVE MODE ---"

        for dirPath, dirNames, fileNames in os.walk(nowdir):
            if dirNames == []:
                merge(dirPath, dirPath.split("/")[-1] + ".pdf")
                
    else:
        print "!!! ERROR, TRY AGAIN !!!"

