import os

def generate_positive_desc_file():
    with open('pos.txt', 'w') as f:
        for filename in os.listdir('positive'):
            f.write('positive/' + filename + ' 1 202 385 169 175\n')

generate_positive_desc_file()