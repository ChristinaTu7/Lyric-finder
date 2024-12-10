import os
import sys

def count_keyword(path_name, keyword):
    kcount = 0
    for d, s, f in os.walk(path_name):
        for file in f:
            file_path = os.path.join(d, file) 
            with open(file_path) as my_file:
                text = my_file.read()
                kcount += text.count(keyword)
    return kcount


def main():
    try:
        path_name = sys.argv[1]
    except:
        print(f"Usage: {sys.argv[0]} pathname")
        sys.exit(1)
    prompt = "Enter a word you want to count: "
    keyword = input(prompt)

    try:
        if len(keyword) < 3:
            raise ValueError("keyword entered is too short.")
    except ValueError as excpt:
        print(excpt)

    kcount = count_keyword(path_name, keyword)
    print(f"{keyword} appears {kcount} times.")

if __name__ == '__main__':
    main()