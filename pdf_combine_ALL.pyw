#!/usr/bin/env python
# To combine multi PDFs in multi folders
# only RECURSIVE MODE

import os
import shutil
from argparse import ArgumentParser
from glob import glob
from pyPdf import PdfFileReader, PdfFileWriter

def merge(path, output_filename):

    error = 0
    output = PdfFileWriter()
    os.chdir(path)

    for pdffile in glob('*.pdf'):
    
        if pdffile == output_filename:
            continue
        print("Parse '%s'" % pdffile)

        try:
            document = PdfFileReader(open(pdffile, 'rb'))
            for i in range(document.getNumPages()):
                output.addPage(document.getPage(i))
        except:
            print("Error!")
            error = 1 
            errorLogs.append(pdffile +','+ output_filename + '\n')
            break

    if error == 0:
        print("Start writing '%s'" % output_filename)

        output_stream = file(output_filename, "wb")
        output.write(output_stream)
        output_stream.close()
    
        if output_filename != (nowdir.split("/")[-1] + ".pdf"):
            shutil.copy(output_filename,nowdir)

        print("--- END ---")

    else:
        print("--- ERROR ---")


if __name__ == "__main__":

    errorLogs = []
    nowdir = os.getcwd()
    f = open('pdf_comb.txt','w+',0)

    parser = ArgumentParser()

    # Add more options if you like
    # parser.add_argument("-o", "--output", dest="output_filename", default="merged.pdf",
    #                   help="write merged PDF to FILE", metavar="FILE")
    parser.add_argument("-p", "--path", dest="path", default=".",
                      help="path of source PDF files")
    parser.add_argument("-r", "--recursive", dest="all_folders", default="false",
                      help="Apply for All folders?(true/false)", metavar="RECURSIVE")

    args = parser.parse_args()

    recur = "true";
    
    if recur == "false":
        print "--- SINGLE MODE ---"
        merge(args.path, nowdir.split("/")[-1] + ".pdf")

    elif recur == "true":
        print "--- RECURSIVE MODE ---"

        for dirPath, dirNames, fileNames in os.walk(nowdir):
            if dirNames == []:
                folder_name = dirPath.split("/")[-1]
                print("Folder: '%s'" % folder_name)
                merge(dirPath, folder_name + ".pdf")
                
    else:
        print "!!! ERROR, TRY AGAIN !!!"

    for log in errorLogs:
        print log
        f.write(str(log))

    f.close()

