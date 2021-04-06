import sys

with open("bakery.csv") as f:
    try:
        start_value = int(sys.argv[1])
        try:
            finish_value = int(sys.argv[2])
            if start_value > finish_value:
                print("начальное значение", start_value, "некорректно")
            else:
                for i, value in enumerate(f, start=1):  # 2 args > 0
                        if start_value <= i <= finish_value:
                            print(value)
                if i < finish_value or i < start_value:
                    print("В файле только", i, "записей с ценами")

        except IndexError:
            for i, value in enumerate(f, start=1):  # start_value > 0, finish_value = 0, 1 args
                if i >= start_value:
                    print(value)
            if i < start_value:
                print("В файле только", i, "записей с ценами")
    except IndexError:
        for val in f:  # start_value = 0, no args
            print(val)