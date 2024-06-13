import json
import sys
import requests

# def downloadQuestion(questionID):
#     return requests.post(
#         url = "https://qbank-api.collegeboard.org/msreportingquestionbank-prod/questionbank/digital/get-question",
#         body = f'{{"external_id": "{questionID}"}}'
#     ).json()[0]

def renderPassage(passage):
    return f"""
        {passage["directions"] if "directions" in passage else ""}
        <i>{passage["attribution"] if "attribution" in passage else ""}</i>
        {passage["body"]}
"""

def renderQuestion(question, questionNo, standalone, showPassage=True):
    output = f"""<!DOCTYPE html>
<html>
    <head>
        <title>Question {question["item_id"]}</title>
        <style>
            .sr-only {{
                display: none;
            }}
        </style>
    </head>
    <body>
""" if standalone else ""

    if "passage" in question and question["passage"] and showPassage:
        output += f"""
        <h2>Question {questionNo if questionNo is not None else question["item_id"]}</h2>
"""
        output += renderPassage(question["passage"])
        output += """
        <h3>Question</h3>"""
    else:
        output += f"""
        <h2>Question {questionNo if questionNo is not None else question["item_id"]}</h2>
"""

    if "prompt" in question:
        output += f"""
        {question["prompt"]}
"""
    if question["answer"]["style"] == "Multiple Choice":
        output += f"""
        <ol type="a">"""
        for choice in question["answer"]["choices"]:
            output += f"""
            <li>
                {question["answer"]["choices"][choice]["body"]}            </li>"""
        output += f"""
        </ol>
        <h3>Explanation</h3>
        {question["answer"]["rationale"]}"""
    elif question["answer"]["style"] == "SPR":
        output += f"""
        <input type="text" maxlength=4 pattern="[0-9/.]" />
        <h3>Explanation</h3>
        {question["answer"]["rationale"]}"""
    else:
        print(f'Unknown answer style: {question["answer"]["style"]}')
    if standalone: output += """
    </body>
</html>
"""
    return output

if __name__ == "__main__":
    # # The question file includes an array containing a single question object.
    # with open(file="../PSAT89_2022_SepMarch/Reading/042374-01.json", mode='r') as questionFile:
    #     print(renderQuestion(json.load(questionFile)[0], None, True))

    print(renderQuestion(
        question=downloadQuestion(sys.argv[1]),
        questionNo=None,
        standalone=True,
        showPassage=True
    ))

