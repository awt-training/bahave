import requests


class Authentication:
    BASE_URL_API = "https://www.pivotaltracker.com/services/v5"

    X_TRACKER_TOKEN_HEADER = "X-TrackerToken"

    singleton = Authentication.__init__()

    def __init__(self):
        self.__requestSpecification = requests.

    # RequestSpecBuilder() \
    #     .setBaseUri(BASE_URL_API) \
    #     .addHeader(X_TRACKER_TOKEN_HEADER, Environment.getInstance().getToken()) \
    #     .build();
    # }

    # / **
    # *This
    # method
    # instantiate
    # the
    # singleton
    # object
    # of
    # the
    # Authentication
    #
    #
    # class .
    #
    #     *
    # * @ return the
    # singleton
    # instance.
    # * /
    def getSingleton():
        return singleton

    # / **
    # *This
    # method
    # return the
    # Request
    # Specification
    # instance.
    # *
    # * @ return the
    # Request
    # Specification
    # instance.
    # * /
    def getRequestSpecification():
        return requestSpecification;
