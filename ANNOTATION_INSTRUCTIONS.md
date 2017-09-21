![Gavagai](gavagai.png)

# ParaLex
Paradigmatic term clusters in multiple languages - a resource for evaluating word spaces and other semantic similarity models.

## Instructions for adding test data to ParaLex

Please create word lists for the different categories (abbrevmonths, cities, colours, dayparts, drinks, establishments, 
organs, hotdrinks, months, nordics,vegetables, weekdays) with respect to the format as shown in the Example section below. 

See the Explanation section for further details about each type of paradigm.

Translate directly from English if mentioned in the explanation, and use the English example as a reference otherwise.

### Format 
Each column in the test data CSV sheet has a special meaning.

* **Language code**: should contain a two character ISO639-1 language code.
* **Comment**: any comment you may have regarding the specific test you are inputting into the sheet.
* **Test label**: the name of the test, see the Explanation section below for possible values.
* **Term 1 - N**: the different words in the test.

### Example

|Language code|Test label| Term 1|Term 2 |Term 3 |Term 4 |Term 5 |Term 6 |Term 7 |Term 8 |Term 9 |Term 10|Term 11|Term 12|
| ----------- | -------- | --------- |--- |---|---|---|---|---|---|---|---|---|---|
|EN| abbrevmonths| jan |feb |mar |apr |may |jun |jul |aug |oct |nov |dec|
|EN| cities| london |paris |brussels |berlin |rome |madrid |tokyo|
|EN| colours| red |green |blue |yellow |black |white |brown |orange|
|EN| dayparts |morning |evening |night |day |afternoon|
|EN| drinks |beer |wine |liquor |soda|
|EN| establishments |restaurant |bistro |cafe |diner |bar |pub |bakery|
|EN| fruit |apple |pineapple |pear |orange|
|EN| organs |vagina |penis | kidney| liver| heart| bladder|
|EN| hotdrinks |coffee |tea |cocoa|
|EN| months |january |february |march |april |may |june |july |august |september |october |november |december|
|EN| nordics |sweden |finland |denmark |norway |iceland|
|EN| vegetables |tomato |avocado |carrot |spinach |cucumber |celery |onion |salad
|EN| weekdays |monday |tuesday |wednesday |thursday |friday |saturday |sunday|


### Explanation
* **abbrevmonths**: abbreviations of months (translation)
* **cities**: names of international capitals (translation)
* **colours**: names of colours (translation, but only if possible)
* **dayparts**: names of the different parts of the day (not necessarily translation but common expressions in respective language)
* **drinks**: names of drinks (common [cold] drinks in respective language)
* **esablishments**: names of establishments (common establishments in respective language)
* **organs**: names of bodily organs
* **hotdrinks**: names of hot drinks (common hot drinks in respective language)
* **months**: names of months (translation)
* **nordics**: names of the nordic countries (translation)
* **vegetables**: names of vegetables (common vegetables in respective language)
* **weekdays**: names of weekdays (translation)
