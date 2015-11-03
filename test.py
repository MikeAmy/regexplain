#!/usr/bin/env python
from backends import English, French
from parse import Pattern, Group
import explain


regex_explanations = (
    ('a', ("'a'")),
    ('b', ("'b'")),
    ('ab', ("'ab'")),
    ('a b', ("'a b'")),
    (r'a\tb', ("'a', then a tab character, then 'b'")),
    (r'\n', ("a line feed")),
    (r'\r', ("a carriage return")),
    (r'\t', ("a tab character")),
    (r'\s', ("a tab or space")),
    (r'\S', ("any character other than a tab or space")),
    (r'\w', ("any word character")),
    (r'\W', ("any non-word character")),
    (r'\b', ("a word boundary")),
    ('.', ('any character')),
    (r'\.', ("'.'")),
    ('^', ('the start of the text')),
    ('$', ('the end of the text')),
    ('.+', ('any character, one or more times')),
    ('.*', ('any character, zero or more times')),
    ('.*?', ('any character, zero or more times, but as few as possible')),
    ('a|b', ("'a' or 'b'")),
    ('a?', ("'a' (optional)")),
    ('[abc]', ("'a' or 'b' or 'c'")),
    ('[^abc]', ("any character other than 'a' or 'b' or 'c'")),
    ('[a-]', ("'a' or '-'")),
    (r'[^]]', ("any character other than ']'")),
    (r'[^\]]', ("any character other than ']'")),
    (r'[]]', ("']'")),
    (r'[\]]', ("']'")),
    (r'[\\]]', ("'\\' or ']'")),
    ('[a-z]', ("a letter from 'a' to 'z'")),
    ('[a-9]', ("a character from 'a' to '9'")),
    ('[0-9]', ("a digit from 0 to 9")),
    ('[a-z0-9]', ("a letter from 'a' to 'z' or a digit from 0 to 9")),
    ('[a-z_]', ("a letter from 'a' to 'z' or '_'")),
    ('[a-z_]{3}', ("a letter from 'a' to 'z' or '_', 3 times")),
    ('[a-z_]{3,5}', ("a letter from 'a' to 'z' or '_', 3 to 5 times")),
    ('[a-z_]{3,5}?', ("a letter from 'a' to 'z' or '_', 3 to 5 times, but as few as possible")),
    ('[a-z_]{3,5}?a', ("a letter from 'a' to 'z' or '_', 3 to 5 times, but as few as possible, then 'a'")),
    ('[A-Z]{2}[0-9]{8,12}', "a letter from 'A' to 'Z', 2 times, then a digit from 0 to 9, 8 to 12 times"),
    ('N/A|[A-Z]{2}[0-9]{8,12}', "'N/A' or a letter from 'A' to 'Z', 2 times, then a digit from 0 to 9, 8 to 12 times"),
    ('(abc)', "A group, matching: 'abc'"),
    ('abc+', "'ab', then the letter 'c' (optional)"),
    ('(?P<group_abc>abc)', "A group named 'group_name', matching: 'abc'"),
    ('(?P<group_abc2>abc)(?P<group2>def)', "A group named 'group_name', matching: 'abc'"),
    ('((?P<group_abc3>abc))', "A group named 'group_name', matching: 'abc'"),
    ('(?P=group_4)', "whatever was matched by group 'group_name'"),
    (Group.regex_part_pattern, 'long'),

    ('(a)', "a group containing the letter 'a'"),
    ('(?:a)', "a non-capturing group containing the letter 'a'"),
    ('(?P<name>ab)', "a group named 'name' containing the letter 'a' then the letter 'b'"),
    ('(?P=name)', "whatever was matched in 'name'"),
    ('(?#comment)', 'an ignored comment'),
    ('abc(?=pattern)', "looks ahead for 'pattern'"),
    ('def(?!pattern)', "looks ahead for no 'pattern'"),
    ('[abc](?<=a|b)d', "looks behind for 'a' or 'b'"),
    ('[abc](?<=a|b)d', "looks behind for no 'a' or 'b'"),
    ('\\3', "whatever was matched in group 3"),

#    ('x(?#comment)+', 'equivalent to x+'),
)

import sys

def test():
    for regex, explanation in regex_explanations:
        print regex
        Pattern(regex).explain(English(sys.stdout.write))

test()
