#getting text from srt files and create txt file
import os, os.path,glob
from pathlib import Path
import pysrt
readdirectory = "./subsrt" #srt file directory
writedirectory = "./subtxt/" # text file directory
for filename in glob.glob(os.path.join(readdirectory,"*.srt")):
    subs = pysrt.open(filename)
    filename = Path(filename).stem
    subtext = open(writedirectory + str(filename) + ".txt","w+")
    for sub in subs:
        char_str = '' .join((z for z in sub.text if not z.isdigit()))
        subtext.write(char_str)
    subtext.close()   