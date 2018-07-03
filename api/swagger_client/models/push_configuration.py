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


class PushConfiguration(object):
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
        'minairtemperature': 'float',
        'maxairtemperature': 'float',
        'minwatertemperature': 'float',
        'maxwatertemperature': 'float',
        'brightnesstreshhold': 'float',
        'feederfrequency': 'float',
        'togglepushnotifications': 'int',
        'waterflowsensitivity': 'float'
    }

    attribute_map = {
        'piid': 'piid',
        'minairtemperature': 'minairtemperature',
        'maxairtemperature': 'maxairtemperature',
        'minwatertemperature': 'minwatertemperature',
        'maxwatertemperature': 'maxwatertemperature',
        'brightnesstreshhold': 'brightnesstreshhold',
        'feederfrequency': 'feederfrequency',
        'togglepushnotifications': 'togglepushnotifications',
        'waterflowsensitivity': 'waterflowsensitivity'
    }

    def __init__(self, piid=None, minairtemperature=None, maxairtemperature=None, minwatertemperature=None, maxwatertemperature=None, brightnesstreshhold=None, feederfrequency=None, togglepushnotifications=None, waterflowsensitivity=None):
        """
        PushConfiguration - a model defined in Swagger
        """

        self._piid = None
        self._minairtemperature = None
        self._maxairtemperature = None
        self._minwatertemperature = None
        self._maxwatertemperature = None
        self._brightnesstreshhold = None
        self._feederfrequency = None
        self._togglepushnotifications = None
        self._waterflowsensitivity = None

        if piid is not None:
          self.piid = piid
        if minairtemperature is not None:
          self.minairtemperature = minairtemperature
        if maxairtemperature is not None:
          self.maxairtemperature = maxairtemperature
        if minwatertemperature is not None:
          self.minwatertemperature = minwatertemperature
        if maxwatertemperature is not None:
          self.maxwatertemperature = maxwatertemperature
        if brightnesstreshhold is not None:
          self.brightnesstreshhold = brightnesstreshhold
        if feederfrequency is not None:
          self.feederfrequency = feederfrequency
        if togglepushnotifications is not None:
          self.togglepushnotifications = togglepushnotifications
        if waterflowsensitivity is not None:
          self.waterflowsensitivity = waterflowsensitivity

    @property
    def piid(self):
        """
        Gets the piid of this PushConfiguration.

        :return: The piid of this PushConfiguration.
        :rtype: str
        """
        return self._piid

    @piid.setter
    def piid(self, piid):
        """
        Sets the piid of this PushConfiguration.

        :param piid: The piid of this PushConfiguration.
        :type: str
        """

        self._piid = piid

    @property
    def minairtemperature(self):
        """
        Gets the minairtemperature of this PushConfiguration.

        :return: The minairtemperature of this PushConfiguration.
        :rtype: float
        """
        return self._minairtemperature

    @minairtemperature.setter
    def minairtemperature(self, minairtemperature):
        """
        Sets the minairtemperature of this PushConfiguration.

        :param minairtemperature: The minairtemperature of this PushConfiguration.
        :type: float
        """

        self._minairtemperature = minairtemperature

    @property
    def maxairtemperature(self):
        """
        Gets the maxairtemperature of this PushConfiguration.

        :return: The maxairtemperature of this PushConfiguration.
        :rtype: float
        """
        return self._maxairtemperature

    @maxairtemperature.setter
    def maxairtemperature(self, maxairtemperature):
        """
        Sets the maxairtemperature of this PushConfiguration.

        :param maxairtemperature: The maxairtemperature of this PushConfiguration.
        :type: float
        """

        self._maxairtemperature = maxairtemperature

    @property
    def minwatertemperature(self):
        """
        Gets the minwatertemperature of this PushConfiguration.

        :return: The minwatertemperature of this PushConfiguration.
        :rtype: float
        """
        return self._minwatertemperature

    @minwatertemperature.setter
    def minwatertemperature(self, minwatertemperature):
        """
        Sets the minwatertemperature of this PushConfiguration.

        :param minwatertemperature: The minwatertemperature of this PushConfiguration.
        :type: float
        """

        self._minwatertemperature = minwatertemperature

    @property
    def maxwatertemperature(self):
        """
        Gets the maxwatertemperature of this PushConfiguration.

        :return: The maxwatertemperature of this PushConfiguration.
        :rtype: float
        """
        return self._maxwatertemperature

    @maxwatertemperature.setter
    def maxwatertemperature(self, maxwatertemperature):
        """
        Sets the maxwatertemperature of this PushConfiguration.

        :param maxwatertemperature: The maxwatertemperature of this PushConfiguration.
        :type: float
        """

        self._maxwatertemperature = maxwatertemperature

    @property
    def brightnesstreshhold(self):
        """
        Gets the brightnesstreshhold of this PushConfiguration.

        :return: The brightnesstreshhold of this PushConfiguration.
        :rtype: float
        """
        return self._brightnesstreshhold

    @brightnesstreshhold.setter
    def brightnesstreshhold(self, brightnesstreshhold):
        """
        Sets the brightnesstreshhold of this PushConfiguration.

        :param brightnesstreshhold: The brightnesstreshhold of this PushConfiguration.
        :type: float
        """

        self._brightnesstreshhold = brightnesstreshhold

    @property
    def feederfrequency(self):
        """
        Gets the feederfrequency of this PushConfiguration.

        :return: The feederfrequency of this PushConfiguration.
        :rtype: float
        """
        return self._feederfrequency

    @feederfrequency.setter
    def feederfrequency(self, feederfrequency):
        """
        Sets the feederfrequency of this PushConfiguration.

        :param feederfrequency: The feederfrequency of this PushConfiguration.
        :type: float
        """

        self._feederfrequency = feederfrequency

    @property
    def togglepushnotifications(self):
        """
        Gets the togglepushnotifications of this PushConfiguration.

        :return: The togglepushnotifications of this PushConfiguration.
        :rtype: int
        """
        return self._togglepushnotifications

    @togglepushnotifications.setter
    def togglepushnotifications(self, togglepushnotifications):
        """
        Sets the togglepushnotifications of this PushConfiguration.

        :param togglepushnotifications: The togglepushnotifications of this PushConfiguration.
        :type: int
        """

        self._togglepushnotifications = togglepushnotifications

    @property
    def waterflowsensitivity(self):
        """
        Gets the waterflowsensitivity of this PushConfiguration.

        :return: The waterflowsensitivity of this PushConfiguration.
        :rtype: float
        """
        return self._waterflowsensitivity

    @waterflowsensitivity.setter
    def waterflowsensitivity(self, waterflowsensitivity):
        """
        Sets the waterflowsensitivity of this PushConfiguration.

        :param waterflowsensitivity: The waterflowsensitivity of this PushConfiguration.
        :type: float
        """

        self._waterflowsensitivity = waterflowsensitivity

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
        if not isinstance(other, PushConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other