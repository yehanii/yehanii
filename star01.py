for i in range(1,6):
    print("☆ "*i + "  "*(5-i) + "☆ "*(6-i))

for i in range(1,6):
    print("  "*(5-i),end='')
    print("☆ "*(i) +"  "*(i-1) +"☆ "*(6-i))