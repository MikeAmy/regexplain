from class_extension import add_method
from parse import (
    AnyCharacter,
    BackReference,
    CharacterClass,
    CharacterSet,
    digits,
    EndOfText,
    EscapedChar,
    Group,
    Identifier,
    letters,
    NamedGroup,
    NonCapturingSubExpression,
    NonWordBoundary,
    Nonsense,
    RepeatablePattern,
    Repeats,
    Sequence,
    SimpleString,
    SingleCharacter,
    StartOfText,
    UnnamedGroup,
    WordBoundary,
    Comment, LookAheadAssertion, LookBehindAssertion, NegativeLookAheadAssertion, NegativeLookBehindAssertion)


@add_method(Group)
def explain(group, output):
    output.which_matches()
    if len(group.sequence_options) > 1:
        if all(
            len(sequence_options) == 1 and
            isinstance(
                sequence_options[0],
                (SimpleString, SingleCharacter, EscapedChar)
            ) for sequence_options in group.sequence_options
        ):
            group.sequence_options[0].explain(output)
            for sequence in group.sequence_options[1:-1]:
                output.comma()
                sequence.explain(output)
            output._or_()
            group.sequence_options[-1].explain(output)
        else:
            output.one_of_the_following()
            output.write('\n')
            output.increase_indentation()
            output.indent()
            group.sequence_options[0].explain(output)
            for sequence in group.sequence_options[1:]:
                output.write('\n')
                output.indent()
                output.or_()
                sequence.explain(output)
            output.decrease_indentation()
    else:
        group.sequence_options[0].explain(output)
    if group.repeats:
        output.write('\n')
        output.indent()
        group.repeats.explain(output)


@add_method(NonCapturingSubExpression)
def explain(non_capturing_subexpression, output):
    output.a_non_capturing_subexpression()
    output.comma()
    super(Group.NonCapturingSubExpression, non_capturing_subexpression).explain(output)


@add_method(BackReference)
def explain(backreference, output):
    output.whatever_was_matched_by_group(
        backreference.other_group_name
    )


@add_method(NamedGroup)
def explain(named_group, output):
    output.a_group_named(named_group.group_name)
    output.comma()
    super(Group.NamedGroup, named_group).explain(output)


@add_method(UnnamedGroup)
def explain(unnamed_group, output):
    output.a_group()
    output.comma()
    super(Group.UnnamedGroup, unnamed_group).explain(output)


@add_method(SimpleString)
def explain(simple_string, output):
    pattern = simple_string.character_pattern
    if len(pattern) == 1:
        if letters.match(pattern):
            output.the_letter()
        elif digits.match(pattern):
            output.the_digit()
        else:
            output.the_single_character()
    else:
        output.the_string()
    output.string(pattern)


@add_method(EscapedChar)
def explain(escaped_char, output):
    super(Group.EscapedChar, escaped_char).explain(output)


@add_method(SingleCharacter)
def explain(single_character, output):
    if single_character.character_pattern == ' ':
        output.a_space()
    else:
        if letters.match(single_character.character_pattern):
            output.the_letter()
        elif digits.match(single_character.character_pattern):
            output.the_number()
        else:
            output.the_single_character()
        output.string(single_character.character_pattern)
    super(Group.SingleCharacter, single_character).explain(output)


@add_method(StartOfText)
def explain(start_of_text, output):
    output.the_start_of_the_text()


@add_method(EndOfText)
def explain(end_of_text, output):
    output.the_end_of_the_text()


@add_method(WordBoundary)
def explain(word_boundary, output):
    output.a_word_boundary()


@add_method(NonWordBoundary)
def explain(non_word_boundary, output):
    output.a_non_word_boundary()


@add_method(AnyCharacter)
def explain(any_character, output):
    output.any_character()
    super(Group.AnyCharacter, any_character).explain(output)


@add_method(Repeats)
def explain(repeats, output):
    if repeats.limits == (0, 1):
        output.optional()
    else:
        if repeats.limits == (0, None):
            output.zero_or_more_times()
        elif repeats.limits == (1, None):
            output.one_or_more_times()
        else:
            if repeats.limits[1] is not None:
                output.from_n_to_m_times(*repeats.limits)
            else:
                output.n_times(repeats.limits[0])
        if repeats.greedily == False:
            output.but_as_few_as_possible()


@add_method(CharacterSet)
def explain(charset, output):
    if charset.exclude_chars:
         output.any_character_other_than()
    if charset.chars:
        chars = list(charset.chars)
        if len(chars) > 1:
            chars.sort()
            output.string(chars[0])
            for character in chars[1:-1]:
                output.comma()
                output.string(character)
            output._or_()
            output.string(chars[-1])
        else:
            output.string(chars[0])
    if charset.chars and charset.ranges:
        if len(charset.chars) > 1:
            output.comma()
        output._or_()
    if charset.ranges:
        method, range_start, range_end = charset.ranges[0]
        getattr(output, method)(range_start, range_end)
        for method, range_start, range_end in charset.ranges[1:]:
            output._or_()
            getattr(output, method)(range_start, range_end)
    super(CharacterSet, charset).explain(output)


@add_method(Identifier)
def explain(charset, output):
    output.an_identifier()


@add_method(CharacterClass)
def explain(character_class, output):
    if character_class.character_pattern == 'S':
        output.any_character_other_than()
        output.a_tab_or_space()
    else:
        getattr(output, dict(character_class.codes)[character_class.character_pattern])()
    super(CharacterClass, character_class).explain(output)


@add_method(RepeatablePattern)
def explain(repeatable_pattern, output):
    if repeatable_pattern.repeats:
        output.comma()
        repeatable_pattern.repeats.explain(output)


@add_method(Sequence)
def explain(sequence, output):
    if sequence:
        sequence[0].explain(output)
    for pattern in sequence[1:]:
        output.write('\n')
        output.increase_indentation()
        output.indent()
        output.followed_by()
        pattern.explain(output)
        output.decrease_indentation()


@add_method(Nonsense)
def explain(nonsense, output):
    output.some_nonsense(nonsense.character_pattern)


@add_method(Comment)
def explain(comment, output):
    output.a_comment(comment.string)


@add_method(LookAheadAssertion)
def explain(lookahead_assertion, output):
    output.lookahead_assertion(True)
    super(LookAheadAssertion, lookahead_assertion).explain(output)


@add_method(LookBehindAssertion)
def explain(lookbehind_assertion, output):
    output.lookbehind_assertion(True)
    super(LookBehindAssertion, lookbehind_assertion).explain(output)


@add_method(NegativeLookAheadAssertion)
def explain(negative_lookahead_assertion, output):
    output.lookahead_assertion(False)
    super(NegativeLookAheadAssertion, negative_lookahead_assertion).explain(output)


@add_method(NegativeLookBehindAssertion)
def explain(negative_lookbehind_assertion, output):
    output.lookbehind_assertion(False)
    super(NegativeLookBehindAssertion, negative_lookbehind_assertion).explain(output)


class ConditionalPattern(Group):
    regex = r'\(\?\((?P<condition_group_name>[a-zA-Z_][a-zA-Z0-9_]*)\)'
