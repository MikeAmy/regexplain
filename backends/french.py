# -*- coding: utf-8 -*-

from backends import NaturalLanguageOutputter


class French(NaturalLanguageOutputter):
    def A_pattern(french):
        french.write("Un motif ")

    def one_of_the_following(french):
        french.write("l'une des choses suivantes:")

    def the_start_of_the_text(french):
        french.write("le début du texte")

    def the_end_of_the_text(french):
        french.write("la fin du texte")

    def but_as_few_as_possible(french):
        french.write(', mais aussi peu que possible')

    def one_or_more_times(french):
        french.write('une ou plusieurs fois')

    def zero_or_more_times(french):
        french.write('zéro ou plusieurs fois')

    def any_character(french):
        french.write("n'importe quel caractère")

    def any_character_other_than(french):
        french.write('un caractère autre que ')

    def optional(french):
        french.write('(optionnel)')

    def n_times(french, n):
        french.write(str(n))
        french.write(" fois")

    def from_n_to_m_times(french, n, m):
        french.write(" de ")
        french.write(str(n))
        french.write(u" à ")
        french.write(str(m))
        french.write(" fois")

    def comma(french):
        french.write(', ')

    def a_space(french):
        french.write('un espace')

    def a_digit(french):
        french.write('un chiffre')

    def then(french):
        french.write(", puis ")

    def followed_by(french):
        french.write("suivi par ")

    def or_(french):
        french.write('ou ')

    def _or_(french):
        french.write(' ou ')

    def the_string(french):
        french.write('la chaîne de caractère')

    def the_single_character(french):
        return
        french.write('le caractère ')

    def the_letter(french):
        french.write('la lettre ')

    def the_digit(french):
        french.write('le chiffre ')

    def string(french, string):
        french.write(repr(string).replace(r'\\', '\\'))

    def a_line_feed(french):
        french.write('un saut de ligne')

    def a_carriage_return(french):
        french.write('un retour à la ligne')

    def a_tab_character(french):
        french.write('une tabulation')

    def a_tab_or_space(french):
        french.write('une tabulation ou un espace')

    def any_word_character(french):
        french.write('n\'importe quel caractère alphabéthique')

    def any_non_word_character(french):
        french.write('n\'importe quel caractère non-alphabétique')

    def a_word_boundary(french):
        french.write('une séparation de mots')

    def a_letter_from_a_to_z(french, a, z):
        french.write("une lettre de ")
        french.string(a)
        french.write(' à ')
        french.string(z)

    def a_character_from_a_to_n(french, a, n):
        french.write("un caractère de ")
        french.string(a)
        french.write(' à ')
        french.string(n)

    def a_digit_from_n_to_m(french, n, m):
        french.write("un chiffre de ")
        french.write(str(n))
        french.write(' à ')
        french.write(str(m))

    def a_group(french):
        french.write('un group')

    def a_group_named(french, name):
        french.write('un motif nommé ')
        french.string(name)

    def a_non_capturing_subexpression(french):
        french.write('une sous-expression non-capturée')

    def which_matches(french):
        french.write('correspondant à ')

    def whatever_was_matched_by_group(french, group_name):
        french.write('tout ce qui correspond au groupe ')
        french.string(group_name)

    def some_nonsense(french, nonsense):
        french.write('les non-sens qui cassent le motif:')
        french.string(nonsense)

    def an_identifier(french):
        french.write('un identifiant')

    def lookahead_assertion(french, positive):
        french.write('une ')
        french.write('vérification anticipée d\'un motif ')
        if not positive:
            french.write('négatif ')

    def lookbehind_assertion(french, positive):
        french.write('une ')
        french.write('vérification à posteriori d\'un motif ')
        if not positive:
            french.write('négatif ')

    def a_comment(french, comment):
        french.write('un commentaire ignoré: ')
        french.string(comment)

