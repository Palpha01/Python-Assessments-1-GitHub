# Exercise 5: Working with JSON File

# Create a JSON file named 'StudentJson.json' with the following details

import json

# 1. Ask the user to enter the student name, ID, and course and write these contents to the JSON file
# 2. Read the contents from the JSON file and display the individual values
# 3. Append another dictionary as follows as key value pair for student 1 in StudentDetails dictionary to form a nested dictionary. Later update the JSON file
# 4. Print the individual values of the Student details reading from JSON file

json_string = '''
    {
        "Details of the student are": [
            {
                "Name": "Alpha",
                "ID": "1",
                "Course": "BSc CC"
                },
                {
                    "Group": "A",
                    "Year": 2
            }
        ]
    }
'''

data = json.loads(json_string)
print(data)