# PrinParLat

## A resource of principal parts of Latin words

PrinParLat (short for "Principal Parts Latin") is a resource listing the principal parts of Latin words. Principal parts are sets of inflected wordforms from which the content of all the other paradigm cells can be inferred (cf. Stump & Finkel 2013). Principal parts were generated from the database of the Lemlat 3.0 morphological analyzer (cf. Passarotti et al. 2017).
This is version 2.0.0, that also includes nouns and adjectives, in addition to verbs that were included in version 1.
The cells that are used as principal parts for verbs are prs.act.inf, fut.act.ind.3.sg, prf.act.ind.1sg, prf.ptcp.nom.n.sg, fut.ptcp.nom.n.sg in most cases; prs.pass.inf and fut.pass.ind.3.sg are used for deponent verbs that lack active wordforms; prf.act.ind.3.sg is used for impersonal verbs that lack first-person wordforms.
The ones that are used for nouns are nom.sg, gen.sg, abl.sg, gen.pl in most cases; nom.pl and gen.pl are used for pluralia tantum nouns that lack singular wordforms.
The ones that are used for adjectives are nom.m.sg, nom.f.sg, nom.n.sg, gen.n.sg, abl.n.sg in most cases; nom.m.pl, nom.f.pl and nom.n.pl are used for cases where no singular form could be generated from our data source.

In PrinParLat, two different layers of lexical units are used: the traditional notion of "lexeme" is used to group wordforms that share the same lexical meaning; to account for systematic variation in form in cases of overabundance, the notion of "flexeme" is used, as introduced by Fradin & Kerleroux (2003). 
For instance, the forms "lalare", "lalabit", "lallare", "lallabit" are assigned to the same flexeme because of their shared meaning ('sing a lullaby'); but different flexemes are introduced to group wordforms that display the stem "lal-" on the one hand ("lalare", "lalabit"), wordforms that display the stem "lall-" on the other hand ("lallare", "lallabit").
Similarly, the forms "lauare", "lauabit", "lauere", "lauet" are assigned to the same lexeme because of their shared meaning ('wash'), but different flexemes are introduced to group wordforms that are inflected according the first conjugation on the one hand ("lauare", "lauabit"), wordforms that are inflected according to the third conjugation on the other hand ("lauere", "lauet").

Fine-grained information on the inflectional behaviour of each flexeme is provided by means of a list of the patterns of formal alternation that hold between all their principal parts, together with their context of application, as extracted by the Qumin toolkit (cf. Beniamine 2018). 
For instance, the alternation pattern between "lauare" and "lauabit" ("re ⇌ bit") is different than the one between "lauere" and "lauet" ("er\_ ⇌ \_t"), so the two flexemes will be assigned to different inflection classes. On the other hand, the same alternation pattern holds between "lalare" and "lalabit" on the one hand, between "lallare" and "lallabit" on the other hand ("re ⇌ bit"), so the two flexemes will be assigned to the same inflection class.

## How to cite

Pellegrini, M. & Passarotti, M. & Mambrini, F. & Moretti, G. 2025. PrinParLat version 2. Online resource.

## References

Beniamine, S. (2018). _Classifications flexionnelles. Étude quantitative des structures de paradigmes_. PhD Thesis. Université Sorbonne Paris Cité-Université Paris Diderot (Paris 7). 

Fradin, B. &  Kerleroux, F. (2003). Troubles with lexemes. In G. Booij, J. DeCesaris, A. Ralli & S. Scalise (eds.), _Selected papers from the third Mediterranean Morphology Meeting_. Barcelona: IULA – Universitat Pompeu Fabra, 177–196.

Passarotti, M., Budassi, M., Litta, E., & Ruffolo, P. (2017). The Lemlat 3.0 package for morphological analysis of Latin. In G. Bouma & Y. Adesam (Eds.), _Proceedings of the NoDaLiDa 2017 workshop on processing historical language_. Linköping University Electronic Press, 24–31.

Stump, G. T. & Finkel, R. A.  (2013). _Morphological typology: From word to paradigm_. Cambridge: Cambridge University Press.

## Files

PrinParLat is released both as a set of .csv files following the Paralex standard format for paradigmatic lexicons, and as Linked Open Data in the LiLa Knowledge Base, in .ttl format.

## Copyright

This resource is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

## Funding

This work was carried out within the context of the "LiLa: Linking Latin" project, that has received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme – Grant Agreement No. 769994.
