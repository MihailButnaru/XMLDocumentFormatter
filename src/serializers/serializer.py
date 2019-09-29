from src.serializers.serializer_factory import factory 

class Serializer:
    """ Generic implementation of the format serializer """
    def serializer(self, serializable, service, filename):
        format_serializer = factory.get_format(service)
        return format_serializer.process(serializable, filename)

serialize = Serializer()
