from io import StringIO
from lxml import etree as et
from tests.mock_data import structured_contract_data
from src.core.xml_processor import XMLProcessor

def test_unstructured_contract(structured_contract_data):
    """
    Tests ensures that the unstructured contract is getting formatted to the correct schema
    """
    contract_process = XMLProcessor()
    contract_process.process('contract.xml', 'new_contract.xml')

    # parsting the file
    parser = et.XMLParser(remove_blank_text=True)
    xml_file = et.parse('new_contract.xml', parser)

    # mock data
    mock_data = StringIO(structured_contract_data)
    mock_data_parse = et.parse(mock_data, parser)

    assert et.tostring(xml_file, encoding='unicode', method='xml', pretty_print=True) == et.tostring(mock_data_parse, encoding='unicode', method='xml', pretty_print=True)