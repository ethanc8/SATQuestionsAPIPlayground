import json
import sys
import requests

def downloadQuestion(questionID):
    return requests.post(
        url = "https://qbank-api.collegeboard.org/msreportingquestionbank-prod/questionbank/digital/get-question",
        data = f'{{"external_id": "{questionID}"}}'
    ).json()

def renderPassage(passage):
    return f"""
        {passage["directions"]}
        <i>{passage["attribution"] if "attribution" in passage else ""}</i>
        {passage["body"]}
"""

def renderQuestion(question, questionNo, standalone, showPassage=True, metadata=None):
    output = f"""<!DOCTYPE html>
<html>
    <head>
        <title>Question {question["externalid"]}</title>
    </head>
    <body>
""" if standalone else ""

    if metadata:
        output += f"""
<b>Difficulty:</b> {metadata["difficulty"]} <b>Skill:</b> {metadata["primary_class_cd_desc"]}: {metadata["skill_desc"]}
"""

#     if "passage" in question and showPassage:
#         output += f"""
#         <h2>Question {questionNo if questionNo is not None else question["externalid"]}</h2>
# """
#         output += renderPassage(question["passage"])
#         output += """
#         <h3>Question</h3>"""
#     else:
    output += f"""
    <h2>Question {questionNo if questionNo is not None else question["externalid"]}</h2>
"""

    if "stimulus" in question:
        output += f"""
        {question["stimulus"]}
"""
    if "stem" in question:
        output += f"""
        {question["stem"]}
    """
    if question["type"] == "mcq":
        output += f"""
        <ol type="A">"""
        for choice in question["answerOptions"]:
            output += f"""
            <li>
                {choice["content"]}            </li>"""
        output += f"""
        </ol>
        <h3>Explanation</h3>
        {question["rationale"]}"""
    elif question["type"] == "spr":
        output += f"""
        <input type="text" maxlength=4 pattern="[0-9/.]" />
        <h3>Explanation</h3>
        {question["rationale"]}"""
    else:
        print(f'Unknown answer style: {question["type"]}')
    
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

