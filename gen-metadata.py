from paralex import paralex_factory

extra_cols_forms = [
    {
        "name": "flexeme",
        "type": "string",
        "title": "Flexeme identifier",
        "description": "Reference to identifier(s) of the flexeme(s) to which the forms can be assigned, colon separated.",
    },
]

extra_cols_flexemes = [
    {
        "name": "flexeme_id",
        "type": "string",
        "title": "Flexeme identifier",
        "description": "Identifier of the flexeme.",
    },
    {
        "name": "inflection_class",
        "title": "Inflection class identifier",
        "description": "This identifier groups together lexemes of the same inflection class.",
        "type": "string",
        "rdfProperty": "https://www.paralex-standard.org/paralex_ontology.xml#inflection_class"
    },
    {
        "name": "lila_id_lemma",
        "type": "integer",
        "title": "lemma ID",
        "description": "ID of the corresponding lemma in the LiLa Knowledge Base.",
    },
    {
        "name": "hasInflectionType",
        "type": "string",
        "title": "Inflection Type",
        "description": "Code corresponding to the Inflection Type (i.e., traditional, coarse-grained inflection class) assigned to the lemma in the LiLa Knowledge Base.",
    },
]
extra_cols_inflectionclasses_patterns = [
    {
        "name": "inflectionclasses-patterns_id",
        "type": "integer",
        "title": "ID",
        "description": "Identifier for the row.",
    },
    {
        "name": "inflection_class",
        "title": "Inflection class identifier",
        "description": "This identifier groups together lexemes of the same inflection class.",
        "type": "string",
        "rdfProperty": "https://www.paralex-standard.org/paralex_ontology.xml#inflection_class"
    },
    {
        "name": "pattern",
        "type": "string",
        "title": "Pattern identifier",
        "description": "Reference to the identifier of the alternation pattern.",
    },
]

extra_cols_patterns = [
    {
        "name": "pattern_id",
        "type": "string",
        "title": "Pattern ID",
        "description": "Identifier of the alternation pattern.",
    },
    {
        "name": "pattern_alternation",
        "title": "Alternation pattern",
        "description": "Alternation pattern between two cells.",
        "type": "string",
    },
    {
        "name": "cell_left",
        "title": "Left cell",
        "description": "Reference to the identifier of the cells on the left for the relevant alternation pattern.",
        "type": "string",
    },
    {
        "name": "cell_right",
        "title": "Right cell",
        "description": "Reference to the identifier of the cells on the right for the relevant alternation pattern.",
        "type": "string",
    },
]


package = paralex_factory("PrinParLat",
                          {
                              "forms": {"path": "forms.csv",
                                        "schema": 
                                          {"fields": extra_cols_forms}
                                        },
                              "cells": {"path": "cells.csv"},
                              "features-values": {"path": "features-values.csv"},
                              "flexemes": {"path": "flexemes.csv",
                                          "schema": 
                                            {"fields": extra_cols_flexemes,
                                          "primaryKey": "flexeme_id"}
                                          },
                              "graphemes": {"path": "graphemes.csv"},
                              "inflectionclasses-patterns": {"path": "inflectionclasses-patterns.csv",
                                        "schema": 
                                          {"fields": extra_cols_inflectionclasses_patterns,
                                          "primaryKey": "inflectionclasses-patterns_id"}
                                        },
                              "lexemes": {"path": "lexemes.csv"},
                              "patterns": {"path": "patterns.csv",
                                        "schema": 
                                          {"fields": extra_cols_patterns,
                                          "primaryKey": "pattern_id",
                                          "foreignKeys": [
                                            {"fields": "cell_left",
                                            "reference": 
                                            {"resource": "cells",
                                            "fields": "cell_id"}
                                          },
                                          {"fields": "cell_right",
                                            "reference": 
                                            {"resource": "cells",
                                            "fields": "cell_id"}                                          
                                          }
                                          ]
                                          }
                                        }
                          },
                          citation="Pellegrini, M. & Passarotti, M. & Mambrini, F. & Moretti, G. 2023. PrinParLat. Online resource.",
                          version="1.1",
                          keywords=["Latin", "verbs", "principal parts", "inflection classes"],
                          id="http://doi.org/10.5281/zenodo.8027826",
                          contributors=[{'title': 'Matteo Pellegrini', 'role': 'author'},
						  {'title': 'Marco Passarotti', 'role': 'contributor'},
						  {'title': 'Francesco Mambrini', 'role': 'contributor'},
						  {'title': 'Giovanni Moretti', 'role': 'contributor'}],
                          licenses=[{'name': 'CC BY-SA 4.0 DEED',
                                     'title': 'Creative Commons Attribution-ShareAlike 4.0 International',
                                     'path': 'https://creativecommons.org/licenses/by-sa/4.0/'}]
)
package.to_json("PrinParLat.json")