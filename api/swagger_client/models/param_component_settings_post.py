# coding: utf-8

"""
    AquaPi Swagger API

    REST API for the AquaPi

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ParamComponentSettingsPost(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'piid': 'str',
        'since': 'datetime',
        'until': 'datetime'
    }

    attribute_map = {
        'piid': 'piid',
        'since': 'since',
        'until': 'until'
    }

    def __init__(self, piid=None, since=None, until=None):
        """
        ParamComponentSettingsPost - a model defined in Swagger
        """

        self._piid = None
        self._since = None
        self._until = None

        self.piid = piid
        if since is not None:
          self.since = since
        if until is not None:
          self.until = until

    @property
    def piid(self):
        """
        Gets the piid of this ParamComponentSettingsPost.

        :return: The piid of this ParamComponentSettingsPost.
        :rtype: str
        """
        return self._piid

    @piid.setter
    def piid(self, piid):
        """
        Sets the piid of this ParamComponentSettingsPost.

        :param piid: The piid of this ParamComponentSettingsPost.
        :type: str
        """
        if piid is None:
            raise ValueError("Invalid value for `piid`, must not be `None`")

        self._piid = piid

    @property
    def since(self):
        """
        Gets the since of this ParamComponentSettingsPost.

        :return: The since of this ParamComponentSettingsPost.
        :rtype: datetime
        """
        return self._since

    @since.setter
    def since(self, since):
        """
        Sets the since of this ParamComponentSettingsPost.

        :param since: The since of this ParamComponentSettingsPost.
        :type: datetime
        """

        self._since = since

    @property
    def until(self):
        """
        Gets the until of this ParamComponentSettingsPost.

        :return: The until of this ParamComponentSettingsPost.
        :rtype: datetime
        """
        return self._until

    @until.setter
    def until(self, until):
        """
        Sets the until of this ParamComponentSettingsPost.

        :param until: The until of this ParamComponentSettingsPost.
        :type: datetime
        """

        self._until = until

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ParamComponentSettingsPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
