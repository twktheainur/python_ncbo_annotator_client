import httplib, urllib
import urlparse


class Client:
    def __init__(self, annotator_url, api_key):
        self.annotator_url = annotator_url
        self.api_key = api_key

    def run_query(self, query):
        """
        Run a bioportal annotator query and return the result
        :param query: An AnnotatorQuery object 
        :return: A string containing the server response
        """

        parsed_url = urlparse.urlparse(self.annotator_url)

        params = {'text': query.text,
                  'longest_match_only': str(query.longest_match_only).lower(),
                  'whole_word_only': str(query.whole_word_only).lower(),
                  'exclude_synonyms': str(query.exclude_synonyms).lower(),
                  'expand_mappings': str(query.expand_mappings).lower(),
                  'expand_class_hierarchy': str(query.expand_class_hierarchy).lower(),
                  'class_hierarchy_max_level': str(query.class_hierarchy_max_level),
                  'format': query.format,
                  'negation': str(query.negation).lower(),
                  'experiencer': str(query.experiencer).lower(),
                  'temporality': str(query.temporality).lower(),
                  'lemmatize': str(query.lemmatize).lower()
                  }

        if len(query.ontologies) > 0:
            params['ontologies'] = ','.join(query.ontologies)

        if len(query.semantic_types) > 0:
            params['semantic_types'] = ','.join(query.semantic_types)

        if len(query.semantic_groups) > 0:
            params['semantic_groups'] = ','.join(query.semantic_groups)

        if len(query.score) > 0:
            params['score']=query.score

        headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                   "Accept": "text/xml, application/json, text/html, text/plain",
                   "Authorization": "apikey token="+self.api_key}

        conn = httplib.HTTPConnection(parsed_url.hostname, parsed_url.port)

        conn.request("POST", parsed_url.path, urllib.urlencode(params), headers)
        response = conn.getresponse()

        if response.status != 200 and response.status != 302:
            raise Exception("Error - HTTP status" + str(response.status) + " : " + response.reason + " [Response body: "+ response.read()+"]")

        return response.read()
