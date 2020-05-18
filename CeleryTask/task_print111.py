import sys

sys.path.append("../..")
sys.path.append("..")

from CeleryTask import app

@app.task
def print111():
    print(111)