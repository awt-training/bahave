import ConfigParser

HEADER = "header"
USER = "user"


class PropertyReader:
    property_reader = None

    def __init__(self, properties='../config.properties'):
        self.__config = ConfigParser.RawConfigParser()
        self.__properties = self.__config.read(properties)
        assert len(self.__properties) > 0, "config.properties file must exist at root path"

    def get_base_url(self):
        return self.__config.get(HEADER, "base_url")

    def get_user(self):
        return self.__config.get(USER, "email")

    def get_token(self):
        return self.__config.get(USER, "token")

    def get_content_type(self):
        return self.__config.get(HEADER, "content_type")

    @staticmethod
    def get_property():
        if PropertyReader.property_reader is None:
            PropertyReader.property_reader = PropertyReader()
        return PropertyReader.property_reader
