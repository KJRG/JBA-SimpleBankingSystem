units_number = int(input())
if units_number < 1:
    print("no army")
elif units_number < 10:
    print("few")
elif units_number < 50:
    print("pack")
elif units_number < 500:
    print("horde")
elif units_number < 1000:
    print("swarm")
else:
    print("legion")
