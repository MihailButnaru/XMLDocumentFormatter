from src.importer import Importer


if __name__ == "__main__":
    xml_importer = Importer()
    xml_importer.process_file('xml', 'contract.xml', 'new_contract.xml')