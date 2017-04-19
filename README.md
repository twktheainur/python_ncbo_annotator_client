# python_ncbo_annotator_client
A python client for the NCBO annotator/SIFR Annotator REST API

This is a simple REST client for NCBO/SIFR annotator in the Bioportal infrastructure. 

## Structure of the project

The client is located in the `client` package (`client.py`) in the ` Client` class. The client takes a URL for the bioportal annotator API and a valid API token.

The only public method for that class is `Client.annotate`  that takes an `AnnotatorQuery` instance as its only argument. 

`AnnotatorQuery` is located in `client/annotator_query.py` and  has a constructor that provides names parameters that match the REST API parameters. 

## How to use it

Below is a simple example of how to use the API for a particular use-case (annotations in the BRAT format)

```python
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


client = c.Client("http://annotator-host:PORT/annotator/", "myapitoken")

inputFile = sys.argv[1]
output_file_name = os.path.basename(inputFile).split(".")[0] + ".ann"
output_directory = os.path.dirname(inputFile)

input_file_handler = open(inputFile, "r")
output_file_handler = open(output_directory + os.path.sep + output_file_name, "w")

text = input_file_handler.read()

query = aq.AnnotatorQuery(text=text, format="brat", negation=True, experiencer=True, temporality=True)
result = client.run_query(query)

output_file_handler.write(result)

```

