while True:
    string = input()
    if string == ".":
        break
    if string[-1] != ".":
        print("no")
        continue

    string = list(string)
    a = ''
    while string:
        s = string.pop(0)
        if s in "()[]":
            a += s

        if "()" in a:
            a = a.replace("()", "")
            if "[]" in a:
                a = a.replace("[]", "")
        if "[]" in a:
            a = a.replace("[]", "")
            if "()" in a:
                a = a.replace("()", "")

    if a.strip() == '':
        print("yes")
    else:
        print("no")
