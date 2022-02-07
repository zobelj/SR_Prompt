#!/usr/bin/env python3

import pandas as pd
import sys

def gen_table(filename):
    # read json data from file
    try:
        data_json = pd.read_json(filename)
    except:
        print("Error reading file: " + filename)
        sys.exit(1)

    # get the team names
    col_names = data_json.columns.values

    # create dataframe with head to head wins
    # row is winner, column is loser
    table = pd.DataFrame(columns=col_names, index=col_names)

    for team in col_names:
        table[team][team] = "--"

    for idx1, team1 in enumerate(col_names):
        for team2 in col_names[idx1+1:]:
            h2h_record = data_json.loc[team1, team2]
            
            # enter wins (or -- if nan) into table
            if not pd.isnull(h2h_record):
                table[team1][team2] = h2h_record['W']
                table[team2][team1] = h2h_record['L']
            else:
                table[team1][team2] = '--'
                table[team2][team1] = '--'
  
    return table

if __name__ == '__main__':

    # get arguments
    if(len(sys.argv) != 2 and len(sys.argv) != 3):
        print('Usage: gen_table.py <json_file> [<output_file>]')
        sys.exit(1)

    FILEIN = sys.argv[1] # json file with W-L records
    if(len(sys.argv) == 3):
        FILEOUT = sys.argv[2] # optional output HTML file
        if(FILEOUT[-5:] != '.html'):
            print(f"Output file '{FILEOUT}' must have .html extension")
            sys.exit(1)

    # generate table
    table = gen_table(FILEIN)

    if(table.empty):
        print("File is empty or does not exist.")
        exit()

    if(FILEOUT):
        # save html render to file
        with open(FILEOUT, 'w') as f:
            f.write(table.to_html())
    
    print("Generated table:\n", table)
