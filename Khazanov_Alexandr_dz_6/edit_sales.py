import os
import sys
if len(sys.argv) != 3:
    print("requested 2 args: number entry, value entry")
else:
    try:
        num = int(sys.argv[1])
        with open("bakery.csv", 'r', encoding='utf-8') as f:
            temp_file = open("temp_file", 'a', encoding='utf-8')
            for i, value in enumerate(f, start=1):
                if i == num:
                    temp_file.write(str(sys.argv[2]) + "\n")
                else:
                    temp_file.write(value)
            if i < num:
                print("File contents only", i, "entries")
        temp_file.close()
        os.remove('bakery.csv')
        os.rename('temp_file', 'bakery.csv')
    except ValueError:
        print("First arg has to be integer")

