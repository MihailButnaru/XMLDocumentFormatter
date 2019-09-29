"""
Importer accepts a document [contract, unstructured] as an XML file, it applyies different
transformations to the document and a new contract is created following
the structured[correct] schema.
"""
from src.serializers.serializer import serialize
from src.core.xml_processor import XMLProcessor

class Importer():

    def process_file(self, format, unstructured_file, filename):
        """ Accepts an unstructured xml file and a transformation is applied
        following the correct structure of the document
            Args:
                format (str) : format of the file [xml at the moment]
                unstructured_file : name of the file
                filename : name of the new file with the transformation
        """
        serialize.serializer(unstructured_file, format, filename)
