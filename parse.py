# -*- coding: utf-8 -*-

import re
from class_extension import ClassExtension


digits = re.compile(r'\d')
letters = re.compile(r'[a-zA-Z]')


class UnrepeatablePattern(object):
    def __init__(unrepeatable_pattern, repeats, **unused):
        if repeats:
            raise Exception('Nothing to repeat')


class StartOfText(UnrepeatablePattern):
    regex = r'\^|\\A'


class EndOfText(UnrepeatablePattern):
    regex = r'\$|\\Z'


class WordBoundary(UnrepeatablePattern):
    regex = r'\\b'


class NonWordBoundary(UnrepeatablePattern):
    regex = r'\\B'


class Repeats(object):
    regex = r'(?P<repetition_string>(\+|\*|\{\d+(?:,\d+)?\})?\??)'

    def __init__(repeats, repetition_string, **unused):
        if repetition_string == '?':
            repeats.limits = (0, 1)
        else:
            repeats.greedily = not repetition_string.endswith('?')
            if not repeats.greedily:
                repetition_string = repetition_string[:-1]
            if repetition_string.startswith('{'):
                repeats.limits = map(int, repetition_string[1:-1].split(','))
                if len(repeats.limits) == 1:
                    repeats.limits = (repeats.limits[0], None)
            else:
                repeats.limits = ('*+'.index(repetition_string[0]), None)


class RepeatablePattern(object):
    def __init__(repeatable_pattern, repeats=None, **unused):
        repeatable_pattern.repeats = repeats


class Group(RepeatablePattern):
    pass


class CharacterClass(RepeatablePattern):
    codes = (
        ('n', 'a_line_feed'),
        ('r', 'a_carriage_return'),
        ('t', 'a_tab_character'),
        ('s', 'a_tab_or_space'),
        ('S', 'any_character_other_than_a_tab_or_space'),
        ('w', 'any_word_character'),
        ('W', 'any_non_word_character'),
        ('d', 'a_digit'),
        ('D', 'a_non_digit'),
    )
    regex = r'|'.join(r'\\'+char for char, description in codes)

    def __init__(character_class, character_pattern, **kwargs):
        super(CharacterClass, character_class).__init__(**kwargs)
        character_class.character_pattern = character_pattern[1]


class BaseCharacterSet(RepeatablePattern):
    regex = (
        r'\[\^?\]?'
            r'(?:'
                r'\\]'
                r'|[^\]]-[^\]]'
                r'|[^\]]'
            r')*'
        r'\]'
    )

    def __init__(charset, character_pattern, parent, **kwargs):
        super(BaseCharacterSet, charset).__init__(**kwargs)
        charset.chars = set()
        charset.ranges = list()
        charset.char_classes = set()
        charset.exclude_chars = False
        character_pattern = character_pattern[1:-1]
        include_char = charset.chars.add
        if character_pattern[0] == '^':
            character_pattern = character_pattern[1:]
            charset.exclude_chars = True
        if character_pattern[0] == ']':
            include_char(']')
            character_pattern = character_pattern[1:]
        elif character_pattern[0:2] == r'\]':
            include_char(']')
            character_pattern = character_pattern[2:]
        i = 0
        while i < len(character_pattern):
            char_i = character_pattern[i]
            try:
                next_char = character_pattern[i+1]
            except IndexError:
                include_char(char_i)
                break
            else:
                if char_i == '\\':
                    if next_char == '\\':
                        include_char("\\")
                    elif next_char == ']':
                        include_char(']')
                    else:
                        if next_char in CharacterClass.codes:
                            charset.char_classes.append(
                                CharacterClass.codes[next_char]
                            )
                        else:
                            include_char(next_char)
                    i += 2
                elif next_char == '-':
                    if i + 2 >= len(character_pattern):
                        include_char(char_i)
                        include_char('-')
                        i += 2
                    else:
                        range_start = char_i
                        range_end = character_pattern[i + 2]
                        if digits.match(range_start) and digits.match(range_end):
                            charset.ranges.append(
                                (
                                    "a_digit_from_n_to_m",
                                    range_start,
                                    range_end
                                )
                            )
                        elif letters.match(range_start) and letters.match(range_end):
                            charset.ranges.append(
                                (
                                    "a_letter_from_a_to_z",
                                    range_start,
                                    range_end
                                )
                            )
                        else:
                            charset.ranges.append(
                                (
                                    "a_character_from_a_to_n",
                                    range_start,
                                    range_end
                                )
                            )
                        i += 3
                else:
                    include_char(char_i)
                    i += 1
        charset.__class__ = CharacterSet
        if (
            # Identifier:
            charset.chars == set(('_'))
            and set(charset.ranges) == set((
                ("a_letter_from_a_to_z", 'A', 'Z'),
                ("a_letter_from_a_to_z", 'a', 'z'),
                ("a_digit_from_n_to_m", '0', '9'),
            ))
            and charset.repeats
            and charset.repeats.limits == (0, None)
            and charset.repeats.greedily
        ):
            previous_sequence_options = parent.sequence_options[-1]
            try:
                previous_charset = previous_sequence_options[-1]
            except IndexError:
                pass
            else:
                if (
                    isinstance(previous_charset, Group.CharacterSet)
                    and previous_charset.chars == set(('_'))
                    and set(previous_charset.ranges) == set((
                        ("a_letter_from_a_to_z", 'A', 'Z'),
                        ("a_letter_from_a_to_z", 'a', 'z'),
                    ))
                    and not previous_charset.repeats
                ):
                    previous_sequence_options.pop()
                    charset.__class__ = Identifier


class CharacterSet(BaseCharacterSet):
    pass


class Identifier(CharacterSet):
    pass


def named_group_from_class(PatternClass):
    return r'(?P<{pattern_class.__name__}>{pattern_class.regex})'.format(
        pattern_class=PatternClass
    )


class AnyCharacter(RepeatablePattern):
    regex = r'\.'


class PreviousGroupContents(RepeatablePattern):
    regex = r'\\d{1:2}'


class EscapedOctal(RepeatablePattern):
    regex = r'\\(?:0\d+|\d{3})'


class SingleCharacter(RepeatablePattern):
    regex = r'[^.^$+*?|\\[{}()]'

    def __init__(single_character, character_pattern, parent, **kwargs):
        super(SingleCharacter, single_character).__init__(**kwargs)
        single_character.character_pattern = character_pattern
        previous_sequence_option = parent.sequence_options[-1]
        try:
            previous_pattern = previous_sequence_option[-1]
        except IndexError:
            pass
        else:
            if not single_character.repeats:
                if (
                    isinstance(previous_pattern, (SingleCharacter, SimpleString))
                    and not previous_pattern.repeats
                ):
                    previous_sequence_option.pop()
                    single_character.character_pattern = (
                        previous_pattern.character_pattern + single_character.character_pattern
                    )


class EscapedChar(SingleCharacter):
    regex = r'\\[^nrtsSwWdDbB\dAZ]'

    def __init__(escaped_char, character_pattern, **kwargs):
        super(EscapedChar, escaped_char).__init__(
            character_pattern = character_pattern[1:],
            **kwargs
        )


class SimpleString(UnrepeatablePattern):
    regex = r'(?:[^.^$+*?|\\[\]{}()]|\\[^nrtsSwWdDbB\dAZ])+(?![+*?{])'

    def __init__(simple_string, character_pattern, parent, **unused):
        super(SimpleString, simple_string).__init__(**unused)
        simple_string.character_pattern = re.sub(r'\\([^nrtsSwWdDbB\dAZ])', r'\1', character_pattern)

        previous_sequence_option = parent.sequence_options[-1]
        try:
            previous_pattern = previous_sequence_option[-1]
        except IndexError:
            pass
        else:
            if (
                isinstance(previous_pattern, (SingleCharacter, SimpleString))
                and not previous_pattern.repeats
            ):
                previous_sequence_option.pop()
                simple_string.character_pattern = (
                    previous_pattern.character_pattern + simple_string.character_pattern
                )


class UnnamedGroup(Group):
    regex = r'\((?!\?)'


class NamedGroup(Group):
    regex = r'\(\?P<(?P<group_name>[a-zA-Z_][a-zA-Z0-9_]*)>'

    def __init__(named_group, group_name, repeats, **kwargs):
        named_group.group_name = group_name
        super(Group.NamedGroup, named_group).__init__(repeats=repeats, **kwargs)


class BackReference(object):
    regex = r'\(\?P=(?P<other_group_name>[a-zA-Z_][a-zA-Z0-9_]*)\)'

    def __init__(backreference, other_group_name, **kwargs):
        backreference.other_group_name = other_group_name


class NumericBackReference(BackReference):
    regex = r'\\[1-9]\d?'

    def __init__(numeric_backreference, character_pattern, other_group_name=None, **kwargs):
        super(NumericBackReference, numeric_backreference).__init__(
            other_group_name=character_pattern[1:],
            **kwargs
        )


class NonCapturingSubExpression(Group):
    regex = r'\(\?:'


class Comment(object):
    regex = r'\(\?#(?:\\\)|[^\)])*\)'

    def __init__(comment, character_pattern, **kwargs):
        comment.string = character_pattern[3:-1]


class LookAheadAssertion(Group):
    regex = r'\(\?='


class NegativeLookAheadAssertion(Group):
    regex = r'\(\?!'


class LookBehindAssertion(Group):
    regex = r'\(\?<='


class NegativeLookBehindAssertion(Group):
    regex = r'\(\?<!'


class ConditionalPattern(Group):
    regex = r'\(\?\((?P<condition_group_name>[a-zA-Z_][a-zA-Z0-9_]*)\)'


class StringHolder(object):
    def __init__(string_holder, remaining_string):
        string_holder.remaining_string = remaining_string

    def consume(string_holder, length):
        string_holder.remaining_string = string_holder.remaining_string[length:]

    def __str__(string_holder):
        return string_holder.remaining_string


class Sequence(list):
    pass


unrepeatable_patterns = (
    StartOfText,
    EndOfText,
    WordBoundary,
    NonWordBoundary,
    NamedGroup,
    ConditionalPattern,
    NegativeLookBehindAssertion,
    LookBehindAssertion,
    NegativeLookAheadAssertion,
    LookAheadAssertion,
    Comment,
    NonCapturingSubExpression,
    UnnamedGroup
)
repeatable_patterns = (
    CharacterSet,
    AnyCharacter,
    CharacterClass,
    BackReference,
    NumericBackReference,
    EscapedChar,
    SimpleString,
    SingleCharacter,
)
unrepeatable_named_groups = map(
    named_group_from_class,
    unrepeatable_patterns
)
repeatable_named_groups = map(
    named_group_from_class,
    repeatable_patterns
)


class Nonsense(object):
    def __init__(nonsense, character_pattern, remaining_string, **unused):
        nonsense.character_pattern = character_pattern
        next_match = Group.pattern_regex.search(
            remaining_string.remaining_string
        )
        remaining_string.consume(next_match.start())


class GroupAsPattern(Group):
    __metaclass__ = ClassExtension

    pattern_regex = (
        r'(?P<next_option>\|)' + (
            '|(?:' + (
                '|'.join(unrepeatable_named_groups)
            ) + ')' +
            '|(?:' + r'(?P<end_of_group>\))|' + (
                '|'.join(repeatable_named_groups)
            ) + ')' +
                named_group_from_class(Repeats) + '?'
        ) + r'|(?P<Nonsense>.+?)'
    )

    Nonsense = Nonsense
    regex_part_pattern = ('^(?:' + pattern_regex + ')')
    pattern_regex = re.compile(regex_part_pattern)

    def __init__(group, remaining_string, parent=None, **kwargs):
        super(Group, group).__init__(**kwargs)
        if isinstance(remaining_string, StringHolder):
            string_holder = remaining_string
        else:
            string_holder = StringHolder(remaining_string)
        group.parent = parent
        group.sequence_options = [Sequence()]
        while string_holder.remaining_string:
            try:
                match = group.pattern_regex.match(string_holder.remaining_string)
                group_dict = dict(match.groupdict())
                repeats = group_dict.pop('Repeats')
                repetition_string = group_dict.pop('repetition_string')
                if repeats:
                    repeats = Repeats(
                        repetition_string=repetition_string
                    )
                for character_pattern_name, character_pattern in group_dict.iteritems():
                    if not character_pattern_name in ('other_group_name',):
                        character_pattern = group_dict[character_pattern_name]
                        if character_pattern is not None:
                            break
                if character_pattern is not None:
                    pattern_class_or_method = getattr(group, character_pattern_name)
                    string_holder.consume(len(match.group(0)))
                    result = pattern_class_or_method(
                        character_pattern=character_pattern,
                        remaining_string=string_holder,
                        parent=group,
                        repeats=repeats,
                        **group_dict
                    )
                    if result is not None:
                        group.sequence_options[-1].append(result)
                else:
                    raise Exception("No match!? Check regex.")
            except Group.ParseCompleted:
                return

    class ParseCompleted(Exception):
        pass

    def end_of_group(group, repeats, **unused):
        group.repeats = repeats
        raise Group.ParseCompleted()

    def next_option(group, repeats, **unused):
        assert not repeats
        group.sequence_options.append(Sequence())

for Pattern in unrepeatable_patterns + repeatable_patterns:
    setattr(Group, Pattern.__name__, Pattern)


class Pattern(Group):
    def explain(pattern, output):
        output.A_pattern()
        super(Pattern, pattern).explain(output)
        output.write('\n')

