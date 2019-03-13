# situation_cluster_naming
This program take the cluster file and original document file as input and output the name of each cluster.

## Format

### cluster file
cluster file is a json line file, with each line represent a cluster. cfile.json is an sample.

Each line should be a json object as follows:
```
{"doc": ["simpost-1101", "simpost-1110", "simpost-1116", "simpost-1125", "simpost-1145"], "id": 4}
```
doc field and id field are required.

### original document file
original document file is the data contains the information of each document. tfile.json is an sample.

each line is an json object as follows:
```
{"text": "The streets are shattered by water , and there 's been everywhere .", "location": "Rakotinsi", "type": "evac", "id": "simpost-0314", "time": "2018-09-20T23:41:35Z"}
```
location, id and type are required, other fields are optional.

## Environment
this code should run with python 3.6. library codecs and argparse should be installed.

## How to run

```
usage: python nameselector.py [-h] -c cluster_file -t original_file -o output_file

arguments:
  -h, --help        show this help message and exit
  -c cluster_file   path to input cluster file
  -t original_file  path to input raw file
  -o output_file    path to output
```

## Sample output
outsample.json is the sample output by running 

```
python nameselector.py  -c cfile -t tfile -o outsample.json
```
Compared to the cfile.json, it adds the name for each cluster. The name is related to type filed of original document file, so please make sure this filed to be precise and correct.
