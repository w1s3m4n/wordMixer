# Word Mixer

Simple tool written in python3 for mixing words in order to create brute forcing wordlists.

## Usage

Just execute
```
usage: python wordmixer.py [-h] --inputfile INPUTFILE [--depth DEPTH]

Word wordlister for brute force attacks

optional arguments:
  -h, --help            show this help message and exit
  --inputfile INPUTFILE, -i INPUTFILE
                        The input file. One word per line. Lowercase
  --depth DEPTH, -d DEPTH
                        Depth of concatenation. Default: 3 (The higher the depth, the higher the
                        processing requirements)


```
## TODO
- [] Improve performance to avoid processing blocks
- [] Improve argument parse
- [] Add output file option
