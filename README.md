# PrinParLat

## A resource of principal parts of Latin words

PrinParLat (short for "Principal Parts Latin") is a resource listing the principal parts of Latin words (currently, only verbs are included). 
Principal parts are sets of inflected wordforms from which the content of all the other paradigm cells can be inferred (cf. Stump & Finkel 2013). The ones that are used for the verbs of PrinParLat are prs.act.inf, fut.act.ind.3.sg, prf.act.ind.1sg, prf.ptcp.nom.n.sg, fut.ptcp.nom.n.sg in most cases; prs.pass.inf and fut.pass.ind.3.sg are used for deponent verbs that lack active wordforms; prf.act.ind.3.sg is used for impersonal verbs that lack first-person wordforms.

In PrinParLat, two different layers of lexical units are used: the traditional notion of "lexeme" is used to group wordforms that share the same lexical meaning; to account for systematic variation in form in cases of overabundance, the notion of "flexeme" is used, as introduced by Fradin & Kerleroux (2003). 
For instance, the forms "lalare", "lalabit", "lallare", "lallabit" are assigned to the same flexeme because of their shared meaning ('sing a lullaby'); but different flexemes are introduced to group wordforms that display the stem "lal-" on the one hand ("lalare", "lalabit"), wordforms that display the stem "lall-" on the other hand ("lallare", "lallabit").
Similarly, the forms "lauare", "lauabit", "lauere", "lauaet" are assigned to the same lexeme because of their shared meaning ('wash'), but different flexemes are introduced to group wordforms that are inflected according the first conjugation on the one hand ("ablauare", "ablauabit"), wordforms that are inflected according to the third conjugation on the other hand ("ablauere", "ablauet").

Fine-grained information on the inflectional behaviour of each flexeme is provided by means of a list of the patterns of formal alternation that hold between all their principal parts, together with their context of application, as extracted by the Qumin toolkit (cf. Beniamine 2018). 
For instance, the alternation pattern between "lauare" and "ablauabit" ("re ⇌ bit") is different than the one between "ablauere" and "ablauet" ("er_ ⇌ _t"), so the two flexemes will be assigned to different inflection classes. On the other hand, the same alternation pattern holds between "lalare" and "lalabit" on the one hand, between "lallare" and "lallabit" on the other hand ("re ⇌ bit"), so the two flexemes will be assigned to the same inflection class.

## References

Beniamine, S. (2018). _Classifications flexionnelles. Étude quantitative des structures de paradigmes_. PhD Thesis. Université Sorbonne Paris Cité-Université Paris Diderot (Paris 7). 

Fradin, B. &  Kerleroux, F. (2003). Troubles with lexemes. In G. Booij, J. DeCesaris, A. Ralli & S. Scalise (eds.), _Selected papers from the third Mediterranean Morphology Meeting_. Barcelona: IULA – Universitat Pompeu Fabra, 177–196.

Stump, G. T. & Finkel, R. A.  (2013). _Morphological typology: From word to paradigm_. Cambridge: Cambridge University Press.

## Files

PrinParLat is released both as a set of .csv files following the Paralex standard format for paradigmatic lexicons (work in progress), and as Linked Open Data in the LiLa Knowledge Base, in .ttl format.
The ontology defining classes and properties introduced specifically for the data at hand is provided in .owl format

## Copyright

This resource is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

## Funding

This work was carried out within the context of the "LiLa: Linking Latin" project, that has received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme – Grant Agreement No. 769994.
