# Data-Driven Democracy
To check the posted verison visit:
`https://epfl-ada.github.io/ada-2021-project-aaaf/`

## Executive summary
Initial idea of trend detection result in in-depth analysis of USA Senat members activity. 

Having a huge 178M quotes dataset can be misleading, since the data is very sparse in the case of quotes. Handling such a big and sparse data requires very structured and step-by-step approach. Moreover, the text itself contains a lot of information, but not all of it is useful. That is why it is essential to do many assumptions and reduce the size of the sample to avoid sparse pieces of data. 

Starting from preliminary analysis with tracking some popular tags in the corpus several issues with data was found. There is a high frequency of USA speakers since the data was obtained by parsing English news. Moreover, USA speakers are conentrated in Washington, that leads to the hypothesis of high level of politicians in the dataset. Generally speaking, news are oftern based on the poilitical speech. The interesting feature of American election system is that many politiciansn are strongly connected with their native state, especially senators, who are elected by the state. Having a list of all senators from 2008 several insights about different state and parties activities was found.

Finally the popularity of several important and popular topics as `justice, taxes, education, weapon` were evaluated trought the time for different states.

## Introduction
Working with text data could be very insightful since the text data includes people's ideas and thoughts. Unlike pictures and tabular data, the text allows understanding what is in people's minds. The following project and ideas are based on the quotes dataset - Quotebank: A Corpus of Quotations from a Decade of News. This dataset is a corpus of 178M quotations. The content was extracted from 162 million English news articles published between 2008 and 2020.


## Data overview

Since it is a news article, especially in English it would be some features we should take into account. First of all, we decided to identify the “sparsity” of the data.

### AAAF Tips & Tricks
The idea is to drop the tale of the data somehow. Tale is a set of quotes that would be difficult to use to get any insights. To clean the data, we assume that each quote is an intersection of an idea and a speaker. Then we would like to eliminate “tale” people or “tale” ideas - the set of people and topics with a low number of data points. This step aims to reduce the data sample and clean the data out of noize.

### Preliminary data analysis 
Initially, our idea was to identify trends in social media; that is why we chose N topics and then filtered the quotes with the tags.We choose the most widespread topics:

`"brexit","drugs","sexism","immigration","islam","ebola","pandemy","terrorism","home violence","meat consumption","vegetarian","feminism","harassment","darknet", "fraud","privacy","climate change","global warming","carbon emission","mental disease", "mental health","burn out",
"burnout"`.

After filering the quotes with these tags we obtain: 

{% include initial_analysis/overall_quotes_distribution.html %}

As a next step we decided to take a look into dataset trough the time. We plotted some of tags occurence trough the time:

{% include initial_analysis/tags_occurence_timeline.html %}

Let's take a more detailed look on this data. On the current step we can already observe some intersting insights about the data we have:

1. For all topics we have a dramatic decrease of quotes occcurence during June 2010 and also for January, March, June and November 2016. **As we have quite big set of tags and significant number of quotes we could conclude that it could be a problem of dataset.** It is important to take into account such a details for the future analysis.
2. Besides the issues with a couple of periods, the dataset provides as a very clear and reasonable data. For example we observe very high occurence of the `financial crisis` at the end of 2008 and in the beginning of 2020. These dates correspond to big financial cirsis at USA and COVID pandemy start resepctively.
3. The second interesting example is `brexit` tag that literally does not exist before the 2016 and afer shows a disruptive growth to one of the most popular.

### Data Enrichment
Previously we descibed the concept that each point in the dataset is a pair of the idea and the person who was quoted. Of course, there are many quotes without any sense, but in this case, we could treat them as “idea-empty” phrases. We merged one of the data subsets (‘climate-change) with a **WikiData API** to get more insights into the data. As a result, we obtain personal data for the persons linked with the quote. In some cases, several persons are associated with the quote. We use a majority vote if possible or randomly in equivalent cases in such cases.
### Identifying biases
As we know, the dataset was collected by parsing the data of the news articles in English. Therefore, our dataset could be presentative only for the English-speakers part of the world. We hypothesize that USA and UK would produce a big part of the content. To check the bias, we plot the quotes distribution by countries for `climate change` for 2008.

{% include initial_analysis/countries_distribution_climate_change_2008.html %}


As we can see, the USA dominates in the dataset. Since climate change is a prevalent topic and we have also checked the distribution for other years, we could be sure that the **USA is presented the best in the dataset.**
Moving further, we decided to check the geographical data more precisely. We plotted the distribution of the States where people work or if their workplace is empty on WikiData. We used place of birth. Inside-US geographical distribution is concentrated in District of Columbia - where Washington is located.

Moving further we decided to check the geographical data more precisely. We ploted the distribution of the States where people work or in case their work place in empty on WikiData we used place of birth. Inside-US geogaphical distribution is concentrated in Distric of Columbia - there Washington is located.


{% include initial_analysis/states_distribution_climate_change_2008.html %}

Washington is a heart of American democracy - there all senators and other politicians are doing their job. 

## Project Idea
The final idea of our project was born in the working process. Meeting different insights and constraints of the data, the USA and mainly Washington was evaluated as a place with a high concentration of quotes. As we all know, it's a city with the highest density of politicians.

Politics is an essential part of many USA citizens and even not-USA people. That is why we have a lot of data from Washington and the USA. In our analysis, we would consider USA Senat members from 2008 to 2020. Senat members are always elected from their native state, and we expect them to talk about the native state's problems and challenges. We collected data for around 200 senators here: [Link](https://docs.google.com/spreadsheets/d/1Viwlaz--L4lrQ-uO6yTGSvXYHHxTXi4JFCW6ar2_j10/edit?usp=sharing)
Based on the insights about the data and several assumptions, we decided to move forward with research in this area. We will evaluate different parties, states, and senators' activity more precisely. Also, we are going to check how different states discuss several topics. This analysis would allow us to understand the activity and biases of different state representatives.
 
Based on the insights about the data and several assumptions we decided to move forward with a research in this area. More precisely we are going to evaluate different parties, states and senators activity. Also we are going to check how several topics are discussed by different states. This analysis would allow us to understand the activiy and biases of different state representative.  

## Basic analysis towards the Idea
Important to mention that we exclude `'Barack Obama', 'Donald Trump' and 'Joe Biden`' from data since when they was elected the number of quotes dramatically changed.
### Most talkative speakers
We ploted top 30 popular senators in the dataset:
{% include main_analysis/most_talkative_senators.html %}

As we can see both parties are well represented. Eventually, Bernie Sanders, being one of the independent senators generates so many quotes.  
### Parties representation
But what about parties in general? Democratic and Republican are opposite players in USA Senat. We discovered year-by-year total activity of both parties:
{% include main_analysis/parties_representation.html %}

It's clear from the data that from 2008 to the 2014 there is a clear advantage of Democratic party over the Republic one. Actually it is a Barack Obama president time, that period was very good for Democratic party, all important roles in the Senat was occupied by the Blue party.

### State activity
The next step in our analysis is to understand states activity. As an initial step we would like to check overall states activity as a number of quotes of Senators who represent the state.
{% include main_analysis/quotes_number_distrib_by_states.html %}

We should highlight that each year the distribution of most active states are different. It is very interesting to see that there are now dominant and tale states.
As a next steps we are going to check in details several interesting topics. Our goal is to check how the actual event are reflected in the quotation activity. To get the actual "activity" for each topic we would use scaled frequency. It means we are going to devide number of quotes on the topic to the overall number of quotes from the state.

## Education
We use set of topics to find senators quotes about education: `{'education', 'schools', 'school', 'student', 'teacher', 'teachers','university', 'universities', 'learning', 'study', 'studing'}`
{% include main_analysis/quotes_number_distrib_by_states_education.html %}
## Justice
We use set of topics to find senators quotes about justice: `{'justice', 'freedom', 'rights', 'equal', 'equally', 'fairly'}`
{% include main_analysis/quotes_number_distrib_by_states_justice.html %}
Justice topic is especially interesting since all states are more active in this topic near the elections. We could see from the map that 2008, 2012 and 2020 are more colored than other years. It could be interesting that senators use this topic to increase election chances.
## Taxes
We use set of topics to find senators quotes about taxes: `{'charge', 'tax', 'bill', 'bills', 'taxes', 'fee', 'fees'}`

{% include main_analysis/quotes_number_distrib_by_states_taxes.html %}
## Weapons

{% include main_analysis/quotes_number_distrib_by_states_weapons.html %}
Firearms or a weapon is a very popular topic in USA. On one hand having a weapon is one of the American citizens rights but on the other hand there are a lot of famous conflicts about it. Schoolshooting is a big issue at USA. For example there is a famous and terrible event - shooting at Sandy Hook Elementary School [link] (https://en.wikipedia.org/wiki/Sandy_Hook_Elementary_School_shooting). If we check the ratio of quotes about weapon in Connecticut state we can observe the drammatic change after the 2012. This reflects a high correlation about senators talks and real events in the state.




















