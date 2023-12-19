try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("на нуль ділити не можна")
finally:
    print("Якись код")
