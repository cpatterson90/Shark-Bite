import os
# reads all files in negative dir and generates neg.txt


def generate_negative_description_file():
    with open(os.path.join(os.path.dirname(__file__),'..\\neg.txt'), 'w') as f:
        # loop over all the filenames
        for filename in os.listdir(os.path.join(os.path.dirname(__file__), '..\\negative')):
            f.write('negative/' + filename + '\n')


if __name__ == '__main__':
    generate_negative_description_file()