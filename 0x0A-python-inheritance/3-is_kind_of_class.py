#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """True if obj is an instance or inherited from a_class, else False"""
    return (isinstance(obj, a_class))
