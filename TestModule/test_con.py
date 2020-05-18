

s = None

for i in range(10):
    try:
        if s is not None and s <= 3:
            continue
        print(i)
    except:
        pass