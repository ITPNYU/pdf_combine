# pdf_combine

## Prerequisites
- To use the script you need [pyPdf](http://pybrary.net/pyPdf/) lib. 
[Download](https://github.com/ITPNYU/pdf_combine/blob/master/pyPdf-1.13.zip?raw=true) and Install it.
``` sh
unzip pyPdf-1.13.zip
cd pyPdf-1.13
python setup.py install
```
- You may need Python Launcher (for Mac).
[Download and Install it.](https://github.com/ITPNYU/pdf_combine/blob/master/python-2.7.10-macosx10.6.pkg?raw=true)

## Use 

- Single mode.

*command line*
``` sh
python pdf_combine.pyw
```

*clicking script in GUI*

make the script executable by
```
chmod +x your_program.rb
```
- Recursive mode.
``` sh
python pdf_combine.pyw -r true
```

##Name PDFs
To combine all PDFs, you might name those files
- alphabetically
- sequentially
- consistently

ex: a-xxx.pdf, b-xxx.pdf, c-xxx.pdf ...
