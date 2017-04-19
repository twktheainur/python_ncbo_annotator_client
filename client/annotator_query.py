class AnnotatorQuery:
    def __init__(self, text="", ontologies=None, semantic_types=None, semantic_groups=None, longest_match_only=False,
                 whole_word_only=True, exclude_synonyms=False, expand_mappings=False, score="",
                 expand_class_hierarchy=False, class_hierarchy_max_level=0, format="json", negation=False,
                 temporality=False, experiencer=False, lemmatize=False):
        self.text = text
        if ontologies is None:
            self.ontologies = []
        else:
            self.ontologies = ontologies

        if semantic_types is None:
            self.semantic_types = []
        else:
            self.semantic_types = semantic_types

        if semantic_groups is None:
            self.semantic_groups = []
        else:
            self.semantic_groups = semantic_groups

        self.longest_match_only = longest_match_only
        self.whole_word_only = whole_word_only
        self.exclude_synonyms = exclude_synonyms
        self.expand_mappings = expand_mappings
        self.score = score
        self.expand_class_hierarchy = expand_class_hierarchy
        self.class_hierarchy_max_level = class_hierarchy_max_level
        self.format = format
        self.negation = negation
        self.experiencer = experiencer
        self.temporality = temporality
        self.lemmatize = lemmatize
