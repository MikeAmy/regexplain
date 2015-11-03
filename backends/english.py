from backends import NaturalLanguageOutputter


class English(NaturalLanguageOutputter):
    def A_pattern(english):
        english.write("A pattern ")

    def one_of_the_following(english):
        english.write("one of the following:")

    def the_start_of_the_text(engish):
        engish.write("the start of the text")

    def the_end_of_the_text(engish):
        engish.write("the end of the text")

    def but_as_few_as_possible(english):
        english.write(', but as few as possible')

    def one_or_more_times(english):
        english.write('one or more times')

    def zero_or_more_times(english):
        english.write('zero or more times')

    def any_character(english):
        english.write('any character')

    def any_character_other_than(english):
        english.write('any character other than ')

    def optional(english):
        english.write('(optional)')

    def n_times(english, n):
        english.write(str(n))
        english.write(" times")

    def from_n_to_m_times(english, n, m):
        english.write(str(n))
        english.write(" to ")
        english.write(str(m))
        english.write(" times")

    def comma(english):
        english.write(', ')

    def a_space(english):
        english.write('a space')

    def a_digit(english):
        english.write('a number')

    def then(english):
        english.write(", then ")

    def followed_by(english):
        english.write("followed by ")

    def or_(english):
        english.write('or ')

    def _or_(english):
        english.write(' or ')

    def the_string(english):
        english.write('')

    def the_single_character(english):
        return
        english.write('the character ')

    def the_letter(english):
        english.write('the letter ')

    def the_digit(english):
        english.write('the number ')

    def string(english, string):
        english.write(repr(string).replace(r'\\', '\\'))

    def a_line_feed(english):
        english.write('a line feed')

    def a_carriage_return(english):
        english.write('a carriage return')

    def a_tab_character(english):
        english.write('a tab character')

    def a_tab_or_space(english):
        english.write('a tab or space')

    def any_word_character(english):
        english.write('any word character')

    def any_non_word_character(english):
        english.write('any non-word character')

    def a_word_boundary(english):
        english.write('a word boundary')

    def a_letter_from_a_to_z(english, a, z):
        english.write("a letter from ")
        english.string(a)
        english.write(' to ')
        english.string(z)

    def a_character_from_a_to_n(english, a, n):
        english.write("a character from ")
        english.string(a)
        english.write(' to ')
        english.string(n)

    def a_digit_from_n_to_m(english, n, m):
        english.write("a number from ")
        english.write(str(n))
        english.write(' to ')
        english.write(str(m))

    def a_group(english):
        english.write('a group')

    def a_group_named(english, name):
        english.write('a group named ')
        english.string(name)

    def a_non_capturing_subexpression(english):
        english.write('a non-capturing sub-expression')

    def which_matches(english):
        english.write('which matches ')

    def whatever_was_matched_by_group(english, group_name):
        english.write('whatever was matched by group ')
        english.string(group_name)

    def some_nonsense(english, nonsense):
        english.write('some nonsense that breaks this pattern:')
        english.string(nonsense)

    def an_identifier(english):
        english.write('an identifier')

    def lookahead_assertion(english, positive):
        english.write('a ')
        if not positive:
            english.write('negative ')
        english.write('look-ahead check for a sub-pattern ')

    def lookbehind_assertion(english, positive):
        english.write('a ')
        if not positive:
            english.write('negative ')
        english.write('look-behind check for a sub-pattern ')

    def a_comment(english, comment):
        english.write('an ignored comment: ')
        english.string(comment)
