Data set name: PrinParLat

Citation (if available): Pellegrini, M. & Passarotti, M. & Mambrini, F. & Moretti, G. 2025. PrinParLat version 2. Online resource

Data set developers: Matteo Pellegrini, Marco Passarotti, Francesco Mambrini, Giovanni Moretti

Data sheet author: Matteo Pellegrini

Others who contributed to this document:

# Motivation

**For what purpose was the dataset created?** 

This dataset was created to supplement the LiLa Knowlede Base of intreoperable resources for Latin with information of wordorms other than the citation forms.
More specifically, it provides the principal parts (i.e., a set of wordforms that allow for the inference of the whole paradigm) of Latin words, as well as a fine-grained classification of their inflectional behavior.
Two different layers of lexical units are used: the traditional notion of "lexeme" is used to group wordforms that share the same lexical meaning; to account for systematic variation in form in cases of overabundance, the notion of "flexeme" is used (see the readme for further details).

**Who created the dataset (for example, which team, research group) and on behalf of which entity (for example, company, institution, organization)?** 

This dataset was created by Matteo Pellegrini, supported by other members of the CIRCSE Research Centre (Francesco Mambrini, Giovanni Moretti, and the director, Marco Passarotti) at the Catholic University of the Sacred Heart in Milan. 

**Who funded the creation of the dataset?** 

This dataset was created in the context of the ERC Consolidator Grant "Linking Latin. Building a Knowledge Base of Linguistic Resources for Latin" (Grant agreement ID: 769994)

# Composition

Paralex datasets document paradigms of inflected forms.

**Are forms given as orthographic, phonetic, and or phonemic sequences ?** 

Forms are given in orthographic transcription. This is due to lack of systematic information on vowel length, that makes it difficult to obtain phonetic/phenemic transcriptions.

**How many instances are there in total?**

- Number of inflected forms: 226,354 (including 4,120 defective cells): 40,434 for verbs, 116,653 for nouns, 69,267 for adjectives
- Number of lexemes: 40,000: 8,014 for verbs, 20,935 for nouns, 11,051 for adjectives
- Number of flexemes: 60,740: 10,998 for verbs, 33,718 for nouns, 16,024 for adjectives
- Maximal paradigm size in cells: 8 for verbs, 5 for nouns, 8 for adjectives

**Language varieties** 

-   BCP-47 language tag: lat
-   Language variety description: Latin, as spoken in the Classical, Pre-Classical and Post-Classical times

**Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set?** 

The dataset provides only principal parts, rather than full paradigms of Latin verbs. 

**Is any information missing from individual instances?** 

In the forms table, in some cases the analysed_orth_form is missing because this could not be obtained automatically from our data source, and the analysis was not trivial to perform manually.
In the flexemes table, in some cases the inflection_class is missing - namely, for flexemes for which only one cell is attested, as the inflectional classification cannot be applied in this cases.
In the flexemes table, in some cases the lila_id_lemma is missing, because there was no lemma in the LiLa Knowledge Base to which the flexeme could be linked.

Verbs that are explicitly marked as impersonals in our data source are coded as defective of non-3rd person singular finite forms.
Verbs that are explicitly marked as deponents in our data source are coded as defective of morphologically active forms.
Verbs that are explicitly marked as "perfectum tantum" in our data source are coded as defective of imperfective forms.
Missing forms that are not marked as defective should be interpreted as missing data. These forms can be missing because the form is not necessary to allow for inference of the full paradigm, or because it cannot be generated on the basis of the information provided by our data source.

**Are there any errors, sources of noise, or redundancies in the dataset?** 

There is no systematic source of errors, noise or redundancy in the dataset (although of course there probably are occasional mistakes).
No explicit indication of (un)certainty is expressed, as the same procedure is applied to obtain all forms in the dataset.

**Is the dataset self-contained, or does it link to or otherwise rely on external resources (for example, websites, tweets, other datasets)?**

The dataset is self-contained, but it is also linked to the LiLa Knowledge Base of interoperable resources for Latin (via the column "lila_id_lemma" in the flexemes table). Therefore, it is also available as RDF triples, and it can be accessed throug the LiLa Query interface (https://lila-erc.eu/query/) or by querying the LiLa triplestore (https://lila-erc.eu/sparql/)

# Collection process

**What is provenance for each table (lexemes, cells, forms, frequencies, sounds, features), as well as for segmentation marks if any ? Are any information derived from other datasets?**

The data of the resource, including segmentations, are obtained from the database of a morphological analyzer of Latin, Lemlat 3.0 (https://github.com/CIRCSE/LEMLAT3).

**How were paradigms separated between lexemes (eg. in the case of homonyms or variants)? What theoretical or practical choices were made?**

The assignment of forms to lexemes reflects the information that can be inferred from our data source.

**How was the paradigm structure (set and labels of paradigm cells) decided ? What theoretical or practical choices were made ?**

The set of paradigm cells has been selected so as to allow for inference for full paradigms for each verb.

**What is the expertise of the contributors with the documented language ?**

Matteo Pellegrini, Marco Passarotti and Francesco Mambrini are experts of the Latin language.
Giovanni Moretti is responsible for all the technical aspects regarding the conversion to RDF triples and linking to the LiLa Knowledge Base.

**How was the data collected (for example, manual human curation, generation by software programs, software APIs, etc)?** 

The data have been generated by applying a python script to the data of our source.

**Who was involved in the data collection process (for example, students, crowdworkers, contractors) and how were they compensated (for example, how much were crowdworkers paid)?**

Only the dataset contributors listed above were involved in the data generation process, as part of their work for the LiLa ERC-funded project.

**Over what timeframe was the data collected?** Does this timeframe match the creation timeframe of the data associated with the instances (for example, recent crawl of old news articles)? If not, please describe the timeframe in which the data associated with the instances was created.

The work for the creation of this resource has been carried out starting in 2021, and it is still ongoing. 
The data of this resource have been obtained from the database of Lemlat 3.0, as documented in Passarotti, M & Budassi, M & Litta, E. & Ruffolo, P. 2017. *The Lemlat 3.0 Package for Morphological Analysis of Latin*. Proceedings of the NoDaLiDa 2017 Workshop on Processing Historical Language.

**Were any ethical review processes conducted (for example, by an institutional review board)?** 

No ethical review process was needed.

# Preprocessing/cleaning/labeling.

**How were the inflected forms obtained ?**  

The inflected forms have been generated by means of a script that started from the stems provided in Lemlat's database and appended the appropriate inflectional endings to them. 

**If relevant, how were the forms segmented ?**

The forms have been segmented according to the stems and endings provided by Lemlat's database.

# Uses

**Has the dataset been used for any published work already?** 

The RDF version of the dataset has been used for the linking of Latin stems of the "Lexicon der Indogermanisches Verben" to the LiLa Knowledge Base (see Boano, V. & Mambrini, F. & Passarotti, M. & Ginevra, R. 2023. *Modelling and Publishing the “Lexicon der indogermanischen Verben” as Linked Open Data*. CLiC-it 2023: 9th Italian Conference on Computational Linguistics, Nov 30 - Dec 02, 2023, Venice, Italy. 

**What (other) tasks could the dataset be used for?**

The dataset can be used to generate full paradigms for Latin words (and any subsequent NLP task they can be used for), or for detailed studies of their inflectional behavior.

# Distribution.

**How will the dataset be distributed (for example, tarball on website, API, GitHub)?** Does the dataset have a digital object identifier (DOI)?

The dataset is released both as a set of .csv files following the Paralex standard format for paradigmatic lexicons, and as Linked Open Data in the LiLa Knowledge Base, in .ttl format.

DOI: http://doi.org/10.5281/zenodo.8027826

This is version 2, that also includes nouns and adjectives, in addition to verbs that were included in version 1.

**When will the dataset be distributed?**

The dataset is already available.

**Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?** 

The dataset is distributed under a Creative Commons Attribution-ShareAlike 4.0 International license (CC BY-SA 4.0, https://creativecommons.org/licenses/by-sa/4.0/).

# Maintenance

**Who will be supporting/hosting/maintaining the dataset?**

The dataset is maintained by the CIRCSE Research Centre.

**How can the owner/curator/manager of the dataset be contacted (for example, email address)?**

The curator of the dataset can be contacted by email at matteo.pellegrini@unicatt.it.

**Will the dataset be updated (for example, to correct labeling errors, add new instances, delete instances)?** 

The dataset will be updated whenever significant changes will be done. This will be communicated to dataset consumers in the GitHub repository.
