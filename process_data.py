import re
import csv
import pandas as pd
from unidecode import unidecode

def change_headers(data_frame):
    return data_frame.rename(columns=lambda header: unidecode(header.lower().replace(' ','_')))
    # change_index = cleaned_headers.rename_axis('id').reset_index()
    # print(change_index)
    # return data_frame.drop('index',axis=1)

def convert_encoding(File):
    pattern = "&#(\d+);"
    regex = re.compile(pattern)

    csv_rows = []
    with open(File, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            for index, word in enumerate(row):
                match = regex.search(word)
                if match:
                    number = match.group(1)
                    row[index] = regex.sub(chr(int(number)), word)
            csv_rows.append(row)
    return change_headers(pd.DataFrame(csv_rows[1:],columns=csv_rows[0])) 
