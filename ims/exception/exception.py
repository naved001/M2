from abc import ABCMeta


# The base class for all BMI Exceptions
# Made abstract since it is recommended to raise the specific subclass
class BMIException(Exception):
    __metaclass__ = ABCMeta


# The base class for all exceptions related to the file system like ceph
class FileSystemException(BMIException):
    __metaclass__ = ABCMeta


# The base class for all exceptions related to HaaS
class HaaSException(BMIException):
    __metaclass__ = ABCMeta


# The base class for all exceptions related to Database
class DBException(BMIException):
    __metaclass__ = ABCMeta


# The base class for all exceptions related to ISCSI
class ISCSIException(BMIException):
    __metaclass__ = ABCMeta


# The base class for all exceptions related to the BMI Config Parser
class ConfigException(BMIException):
    __metaclass__ = ABCMeta
