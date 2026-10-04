import traceback
try:
    1 / 0
except ZeroDivisionError:
    traceback.print_exc()
