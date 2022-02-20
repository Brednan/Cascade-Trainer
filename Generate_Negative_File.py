import os

from numpy import negative

def generate_negative_desc_file():
    with open('neg.txt', 'w') as f:
        for filename in os.listdir('negative'):
            f.write('negative/' + filename + '\n')

generate_negative_desc_file()