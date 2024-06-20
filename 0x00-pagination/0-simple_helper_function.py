#!/usr/bin/env python3
"""
index range function
"""


def index_range(page, page_size):
    """index range"""
    a = 0
    b = 0
    for i in range(page - 1):
        a += page_size
    b = a + page_size
    return (a, b)
