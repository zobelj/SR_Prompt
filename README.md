# SR_Prompt
Given a json file that includes each team's Win-Loss record, this script generates a table displaying a matrix of head-to-head records and optionally generates an HTML table containing the same information. This script was created for the Sports Reference 2022 Engineering Internship Prompt. 

## Usage
When run as a standalone program, the call syntax is as follows:
```bash
gen_table.py input_file.json output_file.html
```

*input_file.sjon* is the name of a json file in the local directory that contains each team's Win-Loss record.

*output_file.html* is the name of the desired HTML file containing the generated matrix displaying head-to-head records.

---
To be implemented into another program, the function to generate the head-to-head matrix can be imported as follows:
```python
from gen_table import gen_table
```
*gen_table()* accepts a filename as a parameter and returns a Pandas Dataframe of head-to-head records.

## Requirements
gen_table requires the following to run:
- [Python 3.8+][1]
- [Pandas 1.3.4+][2]

[1]: https://www.python.org/downloads/
[2]: https://pandas.pydata.org
