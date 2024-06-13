# DSAT Question Bank API

## get-questions

```
POST https://qbank-api.collegeboard.org/msreportingquestionbank-prod/questionbank/digital/get-questions
```

### Input

The body should be a JSON object containing the `asmtEventId`, `test`, and `domain`:
```json
{"asmtEventId":99,"test":2,"domain":"H,P,Q,S"}
```

`asmtEventId` should be one of the following:
| Test Name              | `asmtEventId` |
| ---------------------- | ------------- |
| PSAT 8/9               | 102           |
| PSAT 10 and PSAT/NMSQT | 100           |
| SAT                    | 99            |

`test` should be one of the following:
| Subtest Name        | `test` |
| ------------------- | ------ |
| Reading and Writing | 1      |
| Math                | 2      |

`domain` should be one of the following:
| Domain                       | `domain` |
| ---------------------------- | -------- |
| Information and Ideas        | IOI      |
| Craft and Structure          | CAS      |
| Expression of Ideas          | EOI      |
| Standard English Conventions | SEC      |

| Domain                            | `domain` |
| --------------------------------- | -------- |
| Algebra                           | H        |
| Advanced Math                     | P        |
| Problem-Solving and Data Analysis | Q        |
| Geometry and Trigonometry         | R        |

### Output

```json
{
	"0": {
		"updateDate": 1691007959816,
		"pPcc": "SAT#H",
		"questionId": "002dba45",
		"skill_cd": "H.C.",
		"score_band_range_cd": 5,
		"uId": "013b49a8-e0e3-4cde-8913-5016b184fb62",
		"skill_desc": "Linear equations in two variables",
		"createDate": 1691007959816,
		"program": "SAT",
		"primary_class_cd_desc": "Algebra",
		"ibn": null,
		"external_id": "65ac5dc5-af25-4ecf-8562-a346047750a6",
		"primary_class_cd": "H",
		"difficulty": "M"
	},
    // ...
}
```

## get-question

```
POST https://qbank-api.collegeboard.org/msreportingquestionbank-prod/questionbank/digital/get-question
```

### Input

The body should be a JSON object containing the `external_id` of the question:
```json
{"external_id":"65ac5dc5-af25-4ecf-8562-a346047750a6"}
```

### Output

```json
{
	"keys": [
		".1764",
		" .1765",
		" 3/17"
	],
	"rationale": "<p style=\"text-align: left;\">The correct answer is <math alttext=\"three seventeenths\"><mfrac>\n\t<mn>3</mn>\n\t<mn>17</mn>\n</mfrac>\n</math>. It&rsquo;s given that line <math alttext=\"j\"><mi>j</mi>\n</math> is perpendicular to line <math alttext=\"k\"><mi>k</mi>\n</math> in the <em>xy</em>-plane. This means that the slope of line <math alttext=\"j\"><mi>j</mi>\n</math> is the negative reciprocal of the slope of line <math alttext=\"k\"><mi>k</mi>\n</math>. The equation of line <math alttext=\"k\"><mi>k</mi>\n</math>, <math alttext=\"y equals minus StartFraction 17 Over 3 EndFraction x plus 5\"><mi>y</mi><mo>=</mo><mo>-</mo><mfrac><mn>17</mn><mn>3</mn></mfrac><mi>x</mi><mo>+</mo><mn>5</mn></math>, is written in slope-intercept form <math alttext=\"y equals m x plus b\"><mrow>\n\t<mi>y</mi>\n\t<mo>=</mo>\n\t<mrow>\n\t\t<mrow>\n\t\t\t<mi>m</mi>\n\t\t\t<mi>x</mi>\n\t\t</mrow>\n\t\t<mo>+</mo>\n\t\t<mi>b</mi>\n\t</mrow>\n</mrow>\n</math>, where <math alttext=\"m\"><mi>m</mi>\n</math> is the slope of the line and <math alttext=\"b\"><mi>b</mi>\n</math> is the <em>y</em>-coordinate of the <em>y</em>-intercept of the line. It follows that the slope of line <math alttext=\"k\"><mi>k</mi>\n</math> is <math alttext=\"negative StartFraction 17 Over 3 EndFraction\"><mrow>\n\t<mo>-</mo>\n\t<mfrac>\n\t\t<mn>17</mn>\n\t\t<mn>3</mn>\n\t</mfrac>\n</mrow>\n</math>. The negative reciprocal of a number is <math alttext=\"negative 1\"><mo>-</mo><mn>1</mn>\n</math> divided by the number. Therefore, the negative reciprocal of <math alttext=\"negative StartFraction 17 Over 3 EndFraction\"><mrow>\n\t<mo>-</mo>\n\t<mfrac>\n\t\t<mn>17</mn>\n\t\t<mn>3</mn>\n\t</mfrac>\n</mrow>\n</math> is <math alttext=\"StartStartFraction negative 1 OverOver negative StartFraction 17 Over 3 EndFraction EndEndFraction\"><mfrac><mrow><mo>-</mo><mn>1</mn></mrow><mrow><mo>-</mo><mstyle displaystyle=\"true\"><mfrac><mn>17</mn><mn>3</mn></mfrac></mstyle></mrow></mfrac></math>, or <math alttext=\"three seventeenths\"><mfrac>\n\t<mn>3</mn>\n\t<mn>17</mn>\n</mfrac>\n</math>. Thus, the slope of line <math alttext=\"j\"><mi>j</mi>\n</math> is <math alttext=\"three seventeenths\"><mfrac>\n\t<mn>3</mn>\n\t<mn>17</mn>\n</mfrac>\n</math>. Note that 3/17, .1764, .1765, and 0.176 are examples of ways to enter a correct answer.</p>",
	"origin": "manifold",
	"stem": "<p>Line <math alttext=\"k\"><mi>k</mi>\n</math> is defined by <math alttext=\"y equals minus StartFraction 17 Over 3 EndFraction x plus 5\"><mi>y</mi><mo>=</mo><mo>-</mo><mfrac><mrow><mn>17</mn></mrow><mrow><mn>3</mn></mrow></mfrac><mi>x</mi><mo>+</mo><mrow><mn>5</mn></mrow></math>. Line <math alttext=\"j\"><mi>j</mi>\n</math> is perpendicular to line <math alttext=\"k\"><mi>k</mi>\n</math> in the <em>xy</em>-plane. What is the slope of line <math alttext=\"j\"><mi>j</mi>\n</math>?</p>",
	"externalid": "65ac5dc5-af25-4ecf-8562-a346047750a6",
	"templateid": "7239cf53-8b85-4e79-9653-145b90572d78",
	"vaultid": "8e8b222f-ccd2-4ef0-bdce-2b534c2edbfa",
	"type": "spr",
	"answerOptions": [],
	"correct_answer": [
		".1764",
		" .1765",
		" 3/17"
	]
}
```

```json
{
	"vaultid": "8263d7fb-2f8b-4aed-ad45-f9ce16af3fe4",
	"keys": [
		"45fd0321-3db9-4535-be78-4493284d4bc2"
	],
	"rationale": "<p>Choice C is the best answer because it most logically completes the text&rsquo;s discussion of Johny Isla and the whalelike geoglyph. The text indicates that the German exhibit about the Nazca Lines included a photograph showing a whalelike geoglyph that Isla hadn&rsquo;t known about before attending the exhibit, even though Isla &ldquo;specializes in&rdquo; Nazca Lines geoglyphs. Given his expertise, and his surprise at being unfamiliar with the whale glyph, the text strongly suggests that Isla believed he would have noticed the glyph if he had been to its location. Thus, the text implies that the whalelike geoglyph is likely in a location Isla had not previously been to.&nbsp; &nbsp;</p><p>Choice A is incorrect because the text doesn&rsquo;t address either the species of whale that the geoglyph is meant to represent or its relationship to the earliest humans in the area that is now Peru. Choice B is incorrect. Although the text indicates that the photograph of the whalelike geoglyph was on display at a &ldquo;German exhibit,&rdquo; that exhibit was specifically &ldquo;about the Nazca Lines,&rdquo; which the text indicates are located in Peru. Choice D is incorrect. Although the text does indicate that the glyphs were created &ldquo;over a period of many centuries,&rdquo; the text doesn&rsquo;t address when in that period of time any particular glyphs were created. </p>",
	"origin": "proteus",
	"stem": "<p>Which choice most logically completes the text?</p>",
	"externalid": "22d51297-e8e7-46a4-ba99-2cbf96fbe30c",
	"stimulus": "<p>Geoglyphs are large-scale designs of lines or shapes created in a natural landscape. The Nazca Lines were created in the Nazca Desert in Peru by several Indigenous civilizations over a period of many centuries. Peruvian archaeologist Johny Isla specializes in these geoglyphs. At a German exhibit about the Nazca Lines, he saw an old photograph of a large geoglyph of a whalelike figure and was surprised that he didn&rsquo;t recognize it. Isla returned to Peru and used a drone to search a wide area, looking for the figure from the air. This approach suggests that Isla thought that if he hadn&rsquo;t already seen it, the whalelike geoglyph <span aria-hidden=\"true\">______</span><span class=\"sr-only\">blank</span></p>",
	"templateclusterid": "f5ce17e5-b0e1-4788-9c14-906e7cf55b76",
	"parenttemplatename": "OSP-056-INF",
	"parenttemplateid": "",
	"type": "mcq",
	"position": "0",
	"templateclustername": "",
	"answerOptions": [
		{
			"id": "22240c49-7300-4845-ae2d-b6c5797cb862",
			"content": "<p>must represent a species of whale that went extinct before there were any people in Peru.</p>"
		},
		{
			"id": "e4285e87-7f67-4476-9d2b-5d39c486ec03",
			"content": "<p>is actually located in Germany, not Peru, and isn&rsquo;t part of the Nazca Lines at all.</p>"
		},
		{
			"id": "45fd0321-3db9-4535-be78-4493284d4bc2",
			"content": "<p>is probably in a location Isla hadn&rsquo;t ever come across while on the ground.</p>"
		},
		{
			"id": "d4b27691-f53b-45d8-80d3-d7f873d920ba",
			"content": "<p>was almost certainly created a long time after the other Nazca Lines geoglyphs were created.</p>"
		}
	],
	"correct_answer": [
		"C"
	]
}
```