import json
import requests
from renderQuestion import *

def renderSection(type, questions, standalone):
    output = f"""<!DOCTYPE html>
<html>
    <head>
        <title>{type}</title>
    </head>
    <body>
""" if standalone else ""
    output += f"""
        <h1>{type}</h1>
"""
    passages = []
    
    for questionInfo in questions:
        question = downloadQuestion(questionInfo["cbItemBankId"])

        if "passage" in question and not question["passage"] in passages:
            output += renderPassage(question["passage"])
            passages.append(question["passage"])

        output += renderQuestion(
            question=question,
            questionNo=questionInfo["sequenceNum"],
            standalone=False,
            showPassage=False
        )
    
    if standalone: output += """
    </body>
</html>
"""
    return output



def getSection(type, questions):
    sectionQuestions = []
    for question in questions:
        if question["sectionType"] == type:
            sectionQuestions.append(question)
    
    return sectionQuestions

def renderForm(form, standalone):
    questions = form["questions"]
    output = f"""<!DOCTYPE html>
<html>
    <head>
        <title>Question {form["formId"]}</title>
    </head>
    <body>
""" if standalone else ""
    for section in form["sections"]:
        output += renderSection(
            type=section["description"], 
            questions=getSection(section["description"], questions), 
            standalone=False)
    
    if standalone: output += """
    </body>
</html>
"""
    return output

if __name__ == "__main__":
    # The question file includes an array containing a single question object.
    with open(file="../PSAT89_2022_SepMarch/Private/form.json", mode='r') as formFile:
        with open(file="out/form.html", mode="w") as outputFile:
            outputFile.write(renderForm(json.load(formFile), True))