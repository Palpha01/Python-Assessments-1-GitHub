# Exercise 3: Reading to a List

# The file numbers.txt has a list of 100 integer numbers each on a newline
# Create a python program that puts this data into a list, then output the values in integer format

def read_numbers(data_path):
    
    try:
        with open("Chapter IV/Texts/Numbers.txt","r") as file:
            noombers = [int(line.strip()) for line in file]
        return noombers
    except FileNotFoundError:
        print("Error: File '{data_path}' not found.")
        return []
    except ValueError as e:
        print("Error: {e}. the file '{data_path}' contains non-integer values.")
        
if __name__ == "__main__":
    data_path = "Chapter IV/Texts/Numbers.txt"
    
    noomberlist = read_numbers(data_path)
    
    for noombers in noomberlist:
        print(noombers)