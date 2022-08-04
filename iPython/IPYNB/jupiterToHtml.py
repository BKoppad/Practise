#!/usr/bin/env python
# from IPython.display import Javascript
import pwd
from nbconvert import HTMLExporter
from os import listdir,mkdir,remove
from os.path import isfile, join, dirname,realpath,splitext,exists
import shutil
import time

def output_HTML(read_file, output_file):
    import codecs
    import nbformat
    exporter = HTMLExporter()
    # read_file is '.ipynb', output_file is '.html'
    output_notebook = nbformat.read(read_file, as_version=4)
    output, resources = exporter.from_notebook_node(output_notebook)
    codecs.open(join(htmlFolder,output_file), 'w', encoding='utf-8').write(output)

def get_ipylist(dir=None):
    # listdir()
    # print("Here 1", dir_path)
    fileList=[]
    for file in listdir(dir):
        file_name, file_extension=splitext(file)
        if isfile(file) and file_extension==".ipynb":
            fileList.append(file)
            print

    return fileList

def moveTo(dir):
    fileList=get_ipylist()
    for file in fileList:
        file_name, file_extension=splitext(file)
        output_file = file_name + ".html"
        if exists(join(dir,output_file)):
            remove(join(dir,output_file))
        shutil.move(output_file,dir)


dir_path = dirname(realpath(__file__))
iPythonFilesList=get_ipylist(dir_path)
ipyHtmlDir = "HtmlFolder"
htmlFolder = join(dir_path,ipyHtmlDir)
if not exists(htmlFolder):
    mkdir(htmlFolder)

moveTo(htmlFolder)

for ipyF in iPythonFilesList:
    file_name, file_extension=splitext(ipyF)
    current_file = ipyF
    output_file = file_name + ".html"
    output_HTML(current_file, output_file)