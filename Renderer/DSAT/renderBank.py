import json
import requests
import sys
from renderQuestion import *
import time

def renderBank(bank, standalone):
    output = f"""<!DOCTYPE html>
<html>
    <head>
        <title>Question Bank {sys.argv[1]}</title>
        <style>
            .sr-only {{
                display: none;
            }}
        </style>
        <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
        <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    </head>
    <body>
""" if standalone else ""
    for question in bank:
        output += renderQuestion(
            question=downloadQuestion(question["external_id"]),
            questionNo=question["questionId"],
            standalone=True,
            showPassage=True,
            metadata=question
        )

        time.sleep(1)
    
    if standalone: output += """
    </body>
</html>
"""
    return output

if __name__ == "__main__":
    # The question file includes an array containing a single question object.
    with open(file=sys.argv[1], mode='r') as formFile:
        with open(file="out/form.html", mode="w") as outputFile:
            outputFile.write(renderBank(json.load(formFile), True))