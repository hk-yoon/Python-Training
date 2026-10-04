import os
print(os.getcwd())
print(os.environ.get("RUN_MODE", "development"))
