import re
import lxml.html
from lxml import etree as et


class XMLProcessor():

    def process(self, unstructured_contract, contract_name):
        """ 
        Parse the document
            Args:
                document : xml file
        """
        parser = et.HTMLParser(remove_blank_text=True)
        root_document = et.parse(unstructured_contract, parser)
        document = self._process_broken_tags(self._remove_empty_tags(root_document))
        self._create_document(document, contract_name)
    

    def _remove_empty_tags(self, xml_document):
        """ 
        Removes the empty tags [p] from the document
            Args:
                xml_document : xml file
            Returns:
                xml_document without empty paragraphs tag
        """
        tag = 'p'
        for element in xml_document.xpath(f".//*[self::{tag} and not(node())]"):
            element.getparent().remove(element)
        return lxml.html.fromstring(et.tostring(
                                    xml_document, encoding='unicode', method='xml'))


    def _process_broken_tags(self, xml_document):
        """ Broken paragraths are merged together if
        doesn't end with sentence-ending punctuation
            Args:
                xml_document : xml file
            Returns:
                xml_document with tags merged together
        """
    
        root = xml_document.xpath(".//p")
        punctuation = tuple(['.', ':', '?', '!'])
        paragraphs = [paragraph.text for paragraph in root]
        merge_paragraphs = [paragraph.strip() for paragraph in re.findall('(.*?[?!:.])', ' '.join(paragraphs))]

        for index, value in enumerate(xml_document.xpath("//p")):
            if value.text.strip().endswith(punctuation):
                value.text = 'None'
            else:
                value.getparent().remove(value)
    
        for index, value in enumerate(xml_document.xpath("//p")):
            value.text = merge_paragraphs[index]
    
        return xml_document


    def _create_document(self, xml_document, document_name):
        """ Builds a new XML document
        based on the schema provided
            Args:
                xml_document : xml file
        """
        document_tag = et.Element('document') # <document>
        doc = et.ElementTree(document_tag)

        for elem in xml_document.iter():
            if elem.tag == 'h1':
                section = et.SubElement(document_tag, 'section', title=elem.text) # <section title="">
            elif elem.tag == 'p':
                et.SubElement(section, 'clause').text = elem.text # <section><clause>
        outFile = open(document_name, 'wb')
        doc.write(outFile, xml_declaration=False, encoding='UTF-8', pretty_print=True)
