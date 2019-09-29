from src.core.xml_processor import XMLProcessor

class SerializerFactory:
    """
    Serializer Interface, customized behaviour
    based on different format
    """
    def get_format(self, format):
        """
        It evaluates the type of the format and decides
        the concrete implementation to create and return
            Args:
                format (str): type of the format
        """
        if format == 'xml':
            return XMLProcessor()
        elif format == 'doc':
            # TODO: doc format based on a different schema [not required now to be implemented]
            raise NotImplementedError
        else:
            raise ValueError(format)

factory = SerializerFactory()