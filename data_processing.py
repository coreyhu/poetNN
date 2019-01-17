import pandas as pd
import os

DATA_PATH = './stanzas.txt'

def read_stanzas(path, lines_per_stanza, lines_per_sentence):
    """

    :param path: path to datafile
    :param lines_per_stanza: number of lines per stanza
    :param breaks_per_sentence: how many lines each sentence occupies
    :return:
    """
    with open(path, 'r') as f:
        lines = f.readlines()

        lines = [line[:-1].lower() for line in lines if line != '\n']

        first_lines = lines[::2]
        second_lines = lines[1::2]

        assert len(first_lines) == len(second_lines)
        pairs = list(zip(first_lines, second_lines))

        for pair in pairs:






if __name__ == '__main__':
    read_stanzas(DATA_PATH)