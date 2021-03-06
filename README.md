# regexplain

Don't you hate it when you have to type your phone number into a website, and it shows an error saying "Invalid input", and you try three different ways of inserting hyphens, zeroes and leading plus signs, to no avail, as it is being matched by a mystery regular expression, that you have no clue what the pattern should be, because showing the regex was deemed too difficult for users to understand?

Your users will hate that too... unless you explain whatever regular expression is validating that input, in plain language.

Now you can, in python, using regexplain.

It's a compiler that compiles a regular expression to run on a certain type of wet CPU that runs on glucose and oxygen, known as a human brain.

Of course these programmable CPUs can be broadly categorised by their own instruction sets known as natural languages, which it compiles for.


Here are some examples:

<pre>
a
A pattern which matches the letter 'a'
b
A pattern which matches the letter 'b'
ab
A pattern which matches 'ab'
a b
A pattern which matches 'a b'
a\tb
A pattern which matches the letter 'a'
    followed by a tab character
    followed by the letter 'b'
\n
A pattern which matches a line feed
\r
A pattern which matches a carriage return
\t
A pattern which matches a tab character
\s
A pattern which matches a tab or space
\S
A pattern which matches any character other than a tab or space
\w
A pattern which matches any word character
\W
A pattern which matches any non-word character
\b
A pattern which matches a word boundary
.
A pattern which matches any character
\.
A pattern which matches '.'
^
A pattern which matches the start of the text
$
A pattern which matches the end of the text
.+
A pattern which matches any character, one or more times
.*
A pattern which matches any character, zero or more times
.*?
A pattern which matches any character, zero or more times, but as few as possible
a|b
A pattern which matches the letter 'a' or the letter 'b'
a?
A pattern which matches the letter 'a', (optional)
[abc]
A pattern which matches 'a', 'b' or 'c'
[^abc]
A pattern which matches any character other than 'a', 'b' or 'c'
[a-]
A pattern which matches '-' or 'a'
[^]]
A pattern which matches any character other than ']'
[^\]]
A pattern which matches any character other than ']'
[]]
A pattern which matches ']'
[\]]
A pattern which matches ']'
[\\]]
A pattern which matches '\' or ']'
[a-z]
A pattern which matches a letter from 'a' to 'z'
[a-9]
A pattern which matches a character from 'a' to '9'
[0-9]
A pattern which matches a number from 0 to 9
[a-z0-9]
A pattern which matches a letter from 'a' to 'z' or a number from 0 to 9
[a-z_]
A pattern which matches '_' or a letter from 'a' to 'z'
[a-z_]{3}
A pattern which matches '_' or a letter from 'a' to 'z', 3 times
[a-z_]{3,5}
A pattern which matches '_' or a letter from 'a' to 'z', 3 to 5 times
[a-z_]{3,5}?
A pattern which matches '_' or a letter from 'a' to 'z', 3 to 5 times, but as few as possible
[a-z_]{3,5}?a
A pattern which matches '_' or a letter from 'a' to 'z', 3 to 5 times, but as few as possible
    followed by the letter 'a'
[A-Z]{2}[0-9]{8,12}
A pattern which matches a letter from 'A' to 'Z', 2 times
    followed by a number from 0 to 9, 8 to 12 times
N/A|[A-Z]{2}[0-9]{8,12}
A pattern which matches one of the following:
    'N/A'
    or a letter from 'A' to 'Z', 2 times
        followed by a number from 0 to 9, 8 to 12 times
(abc)
A pattern which matches a group, which matches 'abc'
abc+
A pattern which matches 'ab'
    followed by the letter 'c', one or more times
(?P&lt;group_abc&gt;abc)
A pattern which matches a group named 'group_abc', which matches 'abc'
(?P&lt;group_abc2&gt;abc)(?P&lt;group2&gt;def)
A pattern which matches a group named 'group_abc2', which matches 'abc'
    followed by a group named 'group2', which matches 'def'
((?P&lt;group_abc3&gt;abc))
A pattern which matches a group, which matches a group named 'group_abc3', which matches 'abc'
(?P=group_4)
A pattern which matches whatever was matched by group 'group_4'
^(?:(?P&lt;next_option&gt;\|)|(?:(?P&lt;StartOfText&gt;\^|\\A)|(?P&lt;EndOfText&gt;\$|\\Z)|(?P&lt;WordBoundary&gt;\\b)|(?P&lt;NonWordBoundary&gt;\\B)|(?P&lt;NamedGroup&gt;\(\?P&lt;(?P&lt;group_name&gt;[a-zA-Z_][a-zA-Z0-9_]*)&gt;)|(?P&lt;ConditionalPattern&gt;\(\?\((?P&lt;condition_group_name&gt;[a-zA-Z_][a-zA-Z0-9_]*)\))|(?P&lt;NegativeLookBehindAssertion&gt;\(\?&lt;!)|(?P&lt;LookBehindAssertion&gt;\(\?&lt;=)|(?P&lt;NegativeLookAheadAssertion&gt;\(\?!)|(?P&lt;LookAheadAssertion&gt;\(\?=)|(?P&lt;Comment&gt;\(\?#(?:\\\)|[^\)])*\))|(?P&lt;NonCapturingSubExpression&gt;\(\?:)|(?P&lt;UnnamedGroup&gt;\((?!\?)))|(?:(?P&lt;end_of_group&gt;\))|(?P&lt;CharacterSet&gt;\[\^?\]?(?:\\]|[^\]]-[^\]]|[^\]])*\])|(?P&lt;AnyCharacter&gt;\.)|(?P&lt;CharacterClass&gt;\\n|\\r|\\t|\\s|\\S|\\w|\\W|\\d|\\D)|(?P&lt;BackReference&gt;\(\?P=(?P&lt;other_group_name&gt;[a-zA-Z_][a-zA-Z0-9_]*)\))|(?P&lt;NumericBackReference&gt;\\[1-9]\d?)|(?P&lt;EscapedChar&gt;\\[^nrtsSwWdDbB\dAZ])|(?P&lt;SimpleString&gt;(?:[^.^$+*?|\\[\]{}()]|\\[^nrtsSwWdDbB\dAZ])+(?![+*?{]))|(?P&lt;SingleCharacter&gt;[^.^$+*?|\\[{}()]))(?P&lt;Repeats&gt;(?P&lt;repetition_string&gt;(\+|\*|\{\d+(?:,\d+)?\})?\??))?|(?P&lt;Nonsense&gt;.+?))
A pattern which matches the start of the text
    followed by a non-capturing sub-expression, which matches one of the following:
        a group named 'next_option', which matches '|'
        or a non-capturing sub-expression, which matches one of the following:
            a group named 'StartOfText', which matches '^' or '\A'
            or a group named 'EndOfText', which matches '$' or '\Z'
            or a group named 'WordBoundary', which matches '\b'
            or a group named 'NonWordBoundary', which matches '\B'
            or a group named 'NamedGroup', which matches '(?P&lt;'
                followed by a group named 'group_name', which matches an identifier
                followed by '&gt;'
            or a group named 'ConditionalPattern', which matches '(?('
                followed by a group named 'condition_group_name', which matches an identifier
                followed by ')'
            or a group named 'NegativeLookBehindAssertion', which matches '(?&lt;!'
            or a group named 'LookBehindAssertion', which matches '(?&lt;='
            or a group named 'NegativeLookAheadAssertion', which matches '(?!'
            or a group named 'LookAheadAssertion', which matches '(?='
            or a group named 'Comment', which matches '(?#'
                followed by a non-capturing sub-expression, which matches one of the following:
                    '\)'
                    or any character other than ')'
                zero or more times
                followed by ')'
            or a group named 'NonCapturingSubExpression', which matches '(?:'
            or a group named 'UnnamedGroup', which matches '('
                followed by a negative look-ahead check for a sub-pattern which matches '?'
        or a non-capturing sub-expression, which matches one of the following:
            a group named 'end_of_group', which matches ')'
            or a group named 'CharacterSet', which matches '['
                followed by '^', (optional)
                followed by ']', (optional)
                followed by a non-capturing sub-expression, which matches one of the following:
                    '\]'
                    or any character other than ']'
                        followed by '-'
                        followed by any character other than ']'
                    or any character other than ']'
                zero or more times
                followed by ']'
            or a group named 'AnyCharacter', which matches '.'
            or a group named 'CharacterClass', which matches '\n', '\r', '\t', '\s', '\S', '\w', '\W', '\d' or '\D'
            or a group named 'BackReference', which matches '(?P='
                followed by a group named 'other_group_name', which matches an identifier
                followed by ')'
            or a group named 'NumericBackReference', which matches '\'
                followed by a number from 1 to 9
                followed by a number, (optional)
            or a group named 'EscapedChar', which matches '\'
                followed by any character other than 'A', 'B', 'D', 'S', 'W', 'Z', 'b', 'd', 'n', 'r', 's', 't' or 'w'
            or a group named 'SimpleString', which matches a non-capturing sub-expression, which matches one of the following:
                any character other than '$', '(', ')', '*', '+', '.', '?', '[', '\', ']', '^', '{', '|' or '}'
                or '\'
                    followed by any character other than 'A', 'B', 'D', 'S', 'W', 'Z', 'b', 'd', 'n', 'r', 's', 't' or 'w'
            one or more times
                followed by a negative look-ahead check for a sub-pattern which matches '*', '+', '?' or '{'
            or a group named 'SingleCharacter', which matches any character other than '$', '(', ')', '*', '+', '.', '?', '[', '\', '^', '{', '|' or '}'
            followed by a group named 'Repeats', which matches a group named 'repetition_string', which matches a group, which matches one of the following:
                '+'
                or '*'
                or '{'
                    followed by a number, one or more times
                    followed by a non-capturing sub-expression, which matches ','
                        followed by a number, one or more times
                    (optional)
                    followed by '}'
            (optional)
                followed by '?', (optional)
            (optional)
        or a group named 'Nonsense', which matches any character, one or more times, but as few as possible
(a)
A pattern which matches a group, which matches the letter 'a'
(?:a)
A pattern which matches a non-capturing sub-expression, which matches the letter 'a'
(?P&lt;name&gt;ab)
A pattern which matches a group named 'name', which matches 'ab'
(?P=name)
A pattern which matches whatever was matched by group 'name'
not a comment(?#comment)
A pattern which matches 'not a comment'
    followed by an ignored comment: 'comment'
abc(?=pattern)
A pattern which matches 'abc'
    followed by a look-ahead check for a sub-pattern which matches 'pattern'
def(?!pattern)
A pattern which matches 'def'
    followed by a negative look-ahead check for a sub-pattern which matches 'pattern'
[abc](?&lt;=a|b)d
A pattern which matches 'a', 'b' or 'c'
    followed by a look-behind check for a sub-pattern which matches the letter 'a' or the letter 'b'
    followed by the letter 'd'
[abc](?&lt;=a|b)d
A pattern which matches 'a', 'b' or 'c'
    followed by a look-behind check for a sub-pattern which matches the letter 'a' or the letter 'b'
    followed by the letter 'd'
\3
A pattern which matches whatever was matched by group '3'
</pre>
