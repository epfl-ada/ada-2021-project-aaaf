# ADA 2021 AAF Team Project
    Arsenii Gavrilenko
    Aleksandr Samoilenko
    Anastasiia Filippova

## 17.12.2021  Milestone 3 report 
    Arsenii Gavrilenko - Hypothesis generation, Report and github pages, Data handling
    Aleksandr Samoilenko - Hypothesis generation, Maps vizualizaton, Wikidata handling
    Anastasiia Filippova - Hypothesis generation, Web-scrapping, Data exploration

### Data story link
https://epfl-ada.github.io/ada-2021-project-aaaf/

### Executive summary of work
Initial idea of trend detection result in in-depth analysis of USA Senat members activity.

Having a huge 178M quotes dataset can be misleading, since the data is very sparse in the case of quotes. Handling such a big and sparse data requires very structured and step-by-step approach. Moreover, the text itself contains a lot of information, but not all of it is useful. That is why it is essential to do many assumptions and reduce the size of the sample to avoid sparse pieces of data.

Starting from preliminary analysis with tracking some popular tags in the corpus several issues with data was found. There is a high frequency of USA speakers since the data was obtained by parsing English news. Moreover, USA speakers are conentrated in Washington, that leads to the hypothesis of high level of politicians in the dataset. Generally speaking, news are oftern based on the poilitical speech. The interesting feature of American election system is that many politiciansn are strongly connected with their native state, especially senators, who are elected by the state. Having a list of all senators from 2008 several insights about different state and parties activities was found.

Finally the popularity of several important and popular topics as justice, taxes, education, weapon were evaluated trought the time for different states.

#### Proposed additional datasets:
WikiData API 

`https://www.wikidata.org/wiki/Wikidata:Main_Page`
> Wikidata is a free and open knowledge base that can be read and edited by both humans and machines.
Wikidata acts as central storage for the structured data of its Wikimedia sister projects including Wikipedia, Wikivoyage, Wiktionary, Wikisource, and others.
We are going to use this data source to acquire all data about speakers in out initial dataset. For example for the first analysis we are using gender and occupation merged from wiki data. 


#### Methods
We should notice the data we have is very large, that is why we are going to use prepocessing as much as we can. In our case we are going to filter quotes containg some interesting for us words(topics).
##### Raw data processing 

1. Download file from zenodo for specific year and unzip this file: 

    `wget https://zenodo.org/record/4277311/files/quotes-{YEAR}.json.bz2`

    `bzip2 -d quotes-YEAR.json.bz2`

2. Process jsons with quatations to parse quatations with tag climate change:
    
    `python3 scripts/filter.py --year={YEAR}'`
3. Megre this files with wikidata:
    
    `python3 scripts/wikidata_merge.py --year={YEAR}'`

4. Merge all json files for all years from 2008 to 2020, received 'union.json'.

5. Remove processed files:
    
    `rm quotes-{YEAR}-filtered.json` 
    
    `rm quotes-{YEAR}-wikimerged.json`

6. Creat vocabularies for countries and occupations for processed quatations:
    
    `python scripts/mapping.py --file=union.json`
    

#### Proposed timeline & internal milestones
12 Nov 2021: Milestone P2

19 Nov 2021:
> In-depth exploration of data: biases in countries, topics, speakers' occupations

26 Nov 2021:
> US senators data scrapping, formulation and testing of hypotheses

3 Dec 2021: 
>Building frontend to better present our data story.
Exploration of tools for maps visualization: Plotly / Folium.

10 Dec 2021:
> Frontend is built
All required analyses are done and well-packaged.

17 Dec 2021 Milestone P3
> Making final remarks.

