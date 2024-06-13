import json
import requests
from renderQuestionFromForm import *

def renderSection(type, questions, standalone):
    output = f"""<!DOCTYPE html>
<html>
    <head>
        <title>{type}</title>
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
    output += f"""
        <h1>{type}</h1>
"""
    passages = []
    
    for question in questions:
        # question = downloadQuestion(questionInfo["cbItemBankId"])

        # if "passage" in question and not question["passage"] in passages:
        #     output += renderPassage(question["passage"])
        #     passages.append(question["passage"])

        output += renderQuestion(
            question=question,
            questionNo=question["displayNumber"],
            standalone=False,
            showPassage=True
        )
    
    if standalone: output += """
    </body>
</html>
"""
    return output

def renderForm(form, standalone):
    output = f"""<!DOCTYPE html>
<html>
    <head>
        <title>Test Form</title>
        <style>
            .sr-only {{
                display: none;
            }}
        </style>
        <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
        <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    </head>
    <body>
        <h1>Test Form</h1>
""" if standalone else ""
    for section in form:
        output += renderSection(
            type=section["id"], 
            questions=sorted(section["items"], key=lambda question: question["sequence"]), 
            standalone=False)
    
    if standalone: output += """
    </body>
</html>
"""
    return output

if __name__ == "__main__":
    with open(file="../../../Tests/OfficialPractice/SAT6/questions.json", mode='r') as formFile:
        with open(file="out/SAT6.html", mode="w") as outputFile:
            outputFile.write(renderForm(json.load(formFile), True))