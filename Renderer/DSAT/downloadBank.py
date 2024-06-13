import json
import requests
import sys
from renderQuestion import *
import time

def downloadBank(bank):
    for question in bank:
        with open(file=f'data/{question["external_id"]}.json', mode='w') as questionFile:
            questionData = downloadQuestion(question["external_id"])
            questionFile.write(str(questionData))

        time.sleep(1)

if __name__ == "__main__":
    # The question file includes an array containing a single question object.
    with open(file=sys.argv[1], mode='r') as formFile:
        downloadBank(json.load(formFile))