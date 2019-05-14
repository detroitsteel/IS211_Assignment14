#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Controller for Website Todo List with Form"""

import re
import logging
from logging import FileHandler
import traceback
import sqlite3 as lite
from flask import Flask, render_template, request, redirect
from datetime import datetime


def fibonnaci(n):
    """One of this week’s quiz questions referred to the Fibonnaci sequence.
This sequence of numbers is defined such that the nth number of the sequence
is simply the sum of the two previous numbers in the sequence. In
formal terms, Fn = Fn­1 + Fn­2, where Fn is the n
th Fibonnaci number. Write a function in recursion.py, called
fibonnaci, which will accept one integer parameter (lets call it n) and returns the n

th element of the Fibonnaci

sequence."""
    if n <= 1:
        return n
    else:
        return (fibonnaci(n - 1) + fibonnaci(n - 2))

def gcd(a, b):
    """The greatest common divisor, or GCD, of two integers is the largest
    number that divides both of them with no remainder. Euclid’s algorithm
    is one method to find the GCD of two numbers. Mathematically, we know
    that if r is the remainder when a is divided by b, then gcd(a, b) =
    gcd(b, r). Write a recursive function called gcd that takes parameters
    a and b and returns their greatest common divisor. Think about what the base
    case is for this algorithm."""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def compareTo(s1, s2):
    """When comparing strings, we can always use the == operator in Python.
    However, let us define our own function to compare two strings,
    but lets do so recursively. Write a function called compareTo(s1, s2)
    that will:
        • a negative number if s1 < s2,
        • 0 if s1 == s2, and
        • a positive number if s1 > s2
    Again, think about what the base case is here, which will help clarify
    how to implement the recursion.
    """
    le1 = len(s1)
    le2 = len(s2)
    return le1 - le2
