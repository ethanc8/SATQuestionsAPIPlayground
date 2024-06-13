# Question Bank API

## URL Format

`https://reporting-api.collegeboard.org/msreportingquestionbank-prod/questionbank/get-questions?as=`Assessment`&sc=`Test`&css=`Subscores

### Assessment (`as`)

| Name                   | Code |
| ---------------------- | ---- |
| PSAT 8/9               | 102  |
| PSAT 10 and PSAT/NMSQT | 100  |
| SAT                    | 99   |

### Test (`sc`)

| Name                 | Code |
| -------------------- | ---- |
| Reading              | 1    |
| Writing and Language | 2    |
| Math                 | 3    |

## Example URLs

<table><tbody><tr><td><strong>Assessment</strong></td><td><strong>Test</strong></td><td><strong>Subscores</strong></td><td><strong>URL</strong></td></tr><tr><td>PSAT 8/9</td><td>Reading</td><td>Analysis in History/ Social Studies, Analysis in Science, Command of Evidence, Words in Context, Additional Topics in Reading</td><td>https://reporting-api.collegeboard.org/msreportingquestionbank-prod/questionbank/get-questions?as=102&amp;sc=1&amp;css=7,16,23,43,47</td></tr><tr><td>SAT</td><td>Reading</td><td>Analysis in History/ Social Studies, Analysis in Science, Command of Evidence, Words in Context, Additional Topics in Reading</td><td>https://reporting-api.collegeboard.org/msreportingquestionbank-prod/questionbank/get-questions?as=99&amp;sc=1&amp;css=1,10,19,39,45</td></tr><tr><td><p>PSAT 10</p><p>PSAT/NMSQT</p></td><td>Reading</td><td>Analysis in History/ Social Studies, Analysis in Science, Command of Evidence, Words in Context, Additional Topics in Reading</td><td>https://reporting-api.collegeboard.org/msreportingquestionbank-prod/questionbank/get-questions?as=100&amp;sc=1&amp;css=4,13,21,41,46</td></tr><tr><td>PSAT 8/9</td><td>Writing and Language</td><td>Analysis in History/ Social Studies, Analysis in Science, Command of Evidence, Expression of Ideas, Standard English Conventions, Words in Context</td><td>https://reporting-api.collegeboard.org/msreportingquestionbank-prod/questionbank/get-questions?as=102&amp;sc=2&amp;css=8,17,24,27,38,44</td></tr><tr><td>SAT</td><td>Writing and Language</td><td>Analysis in History/ Social Studies, Analysis in Science, Command of Evidence, Expression of Ideas, Standard English Conventions, Words in Context</td><td>https://reporting-api.collegeboard.org/msreportingquestionbank-prod/questionbank/get-questions?as=99&amp;sc=2&amp;css=2,11,20,25,36,40</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr><tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr></tbody></table>

## Example questions

### 18028

| Paramater               | Value                                 |
| ----------------------- | ------------------------------------- | ---------------------- |
| ID #                    | 18028                                 |
| Difficulty              | 2                                     |
| Cross-Test and Subscore | Expression of Ideas, Words in Context |
| Primary Dimension       | Expression of Ideas                   | Effective language use |
| Secondary Dimension     | Syntax                                |
| Tertiary Dimension      | N/A                                   |
| Passage Text Complexity | Grades 9-10                           |

```
{
    "conPriDimCd": 6,
    "iCmpntId": 18028,
    "conSecDimCd": 23,
    "textCompDimCd": 14,
    "prevIbn": null,
    "calDimCd": null,
    "uId": "99942971-80be-4c6a-b08a-ef1cc9a7f351",
    "ssTierDimCd": 27,
    "asId": 102,
    "scDimCd": 2,
    "ibn": "01812-04",
    "diffDimCd": 2,
    "conTerDimCd": null,
    "prevICmpntId": null
},
{
    "conPriDimCd": 6,
    "iCmpntId": 18028,
    "conSecDimCd": 23,
    "textCompDimCd": 14,
    "prevIbn": null,
    "calDimCd": null,
    "uId": "8ece61c0-5609-47c9-af98-932961e2af4b",
    "ssTierDimCd": 44,
    "asId": 102,
    "scDimCd": 2,
    "ibn": "01812-04",
    "diffDimCd": 2,
    "conTerDimCd": null,
    "prevICmpntId": null
},
```

### 18443

```
  {
    "conPriDimCd": 6,
    "iCmpntId": 18443,
    "conSecDimCd": 21,
    "textCompDimCd": 14,
    "prevIbn": null,
    "calDimCd": null,
    "uId": "c84a42ed-2e70-473b-8f79-f00292494298",
    "ssTierDimCd": 17,
    "asId": 102,
    "scDimCd": 2,
    "ibn": "06780-09",
    "diffDimCd": 2,
    "conTerDimCd": null,
    "prevICmpntId": null
  },
  {
    "conPriDimCd": 6,
    "iCmpntId": 18443,
    "conSecDimCd": 21,
    "textCompDimCd": 14,
    "prevIbn": null,
    "calDimCd": null,
    "uId": "b284b75f-d9fd-479f-9bfb-ed2448d4439a",
    "ssTierDimCd": 27,
    "asId": 102,
    "scDimCd": 2,
    "ibn": "06780-09",
    "diffDimCd": 2,
    "conTerDimCd": null,
    "prevICmpntId": null
  },
  {
    "conPriDimCd": 6,
    "iCmpntId": 18443,
    "conSecDimCd": 21,
    "textCompDimCd": 14,
    "prevIbn": null,
    "calDimCd": null,
    "uId": "67b7b67d-9d2b-4aa9-a4d8-70e680293264",
    "ssTierDimCd": 44,
    "asId": 102,
    "scDimCd": 2,
    "ibn": "06780-09",
    "diffDimCd": 2,
    "conTerDimCd": null,
    "prevICmpntId": null
  },
```
