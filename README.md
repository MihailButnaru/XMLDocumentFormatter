Importer allows you to format the correct structure of contract files [xml files]. 
It accepts a document as an xml file and it removes the blank tags, merge broken paragraphs and
splits the documents into the correct sections.



Installation:
pip install -r requirements.txt

Example of how to use the importer is provided bellow:
```
from src.importer import Importer


if __name__ == "__main__":
    xml_importer = Importer()
    xml_importer.process_file('xml', 'contract.xml', 'new_contract.xml')
```

At the moment reads just xml files conform to the following schema from contract.xml
A new file is produced new_contract.xml 


Tests:
Runt the tests:
```
python -m pytest tests
```