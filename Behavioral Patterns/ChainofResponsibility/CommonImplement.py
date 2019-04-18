#! -*- coding:utf-8 -*-

"""
chain of responsibility pattern
"""
from abc import ABCMeta, abstractmethod
from enum import Enum, auto


class LogLevel(Enum):
    """
    Log Levels Enum.
    """
    NONE = auto()
    INFO = auto()
    DEBUG = auto()
    WARNING = auto()
    ERROR = auto()
    FUNCTIONAL_MESSAGE = auto()
    FUNCTIONAL_ERROR = auto()
    ALL = auto()


class Logger(metaclass=ABCMeta):
    def __init__(self, levels):
        self.log_levels = []
        for level in levels:
            self.log_levels.append(level)
        self.next = None

    def set_next(self, next_logger):
        """
        set next responsible logger in the chain
        :param next_logger: next responsible logger
        :return: Logger: next responsible logger
        """
        self.next = next_logger
        return self.next

    def message(self, msg, severity):
        """
        message writer handler
        :param msg: (str) message string
        :param severity(loglevel): severity of message as log level enum
        :return:
        """
        if LogLevel.ALL in self.log_levels or severity in self.log_levels:
            self.write_message(msg)
        if self.next is not None:
            self.next.message(msg, severity)

    @abstractmethod
    def write_message(self, msg):
        """
        abstract method to write a message
        :param msg: message string
        :Raises:
            NotImplementedError
        """
        raise NotImplementedError("should implement this method")


class ConsoleLogger(Logger):
    def write_message(self, msg):
        """
        overrides parent's abstract method to write to console
        :param msg: message string
        :return:
        """
        print('writing to console', msg)


class EmailLogger(Logger):
    def write_message(self, msg):
        """
        overrides parent's abstract method to write via email
        :param msg: message string
        :return:
        """
        print('send vai email', msg)

class FileLogger(Logger):
    def write_message(self, msg):
        """
        overrides parent's abstract method to write to file
        :param msg: message string
        :return:
        """
        print('write to file', msg)


if __name__ == "__main__":
    """
    building the chain of responsibility
    """
    logger = ConsoleLogger([LogLevel.ALL])
    filelogger = logger.set_next(FileLogger(
        [LogLevel.WARNING, LogLevel.ERROR]
    ))

    emaillogger = filelogger.set_next(EmailLogger(
        [LogLevel.FUNCTIONAL_MESSAGE, LogLevel.FUNCTIONAL_ERROR]
    ))


    print('-----------------will write to console and file------------')
    logger.message('hello world', LogLevel.WARNING)
    print('----------------will write to email and console')
    logger.message('this is good', LogLevel.FUNCTIONAL_MESSAGE)
    print('-----------------will write console only--------------------')
    logger.message('console only message', LogLevel.INFO)