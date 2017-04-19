#!/usr/bin/python

import client.client as c
import client.annotator_query as aq
import os

import sys

if len(sys.argv) < 2:
    print "Syntax: " + sys.argv[0] + " [textFile]"
    print "Result: Will generate a brat annotation file corresponding to the text. The file will be in the same directory \n" \
          "as the source text file and with the same name but with a .ann extension. For example if the \n" \
          "input is /foo/bar/text.txt, then /foo/bar/text.ann will be created and will contain the annotations.\n"
    exit(1)


client = c.Client("http://vm:8081/annotator/", "61297daf-147c-40f3-b9b1-a3a2d6b744fa")

inputFile = sys.argv[1]
output_file_name = os.path.basename(inputFile).split(".")[0] + ".ann"
output_directory = os.path.dirname(inputFile)

input_file_handler = open(inputFile, "r")
output_file_handler = open(output_directory + os.path.sep + output_file_name, "w")

text = input_file_handler.read()

query = aq.AnnotatorQuery(text=text, format="brat", negation=True, experiencer=True, temporality=True)
result = client.run_query(query)

output_file_handler.write(result)
