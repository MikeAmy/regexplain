
class NaturalLanguageOutputter(object):
    def __init__(natural_language_outputter, output):
        natural_language_outputter.output = output
        natural_language_outputter.indentation = 0

    def increase_indentation(natural_language_outputter):
        natural_language_outputter.indentation += 1

    def decrease_indentation(natural_language_outputter):
        # if there is nonsense, groups might not close.
        natural_language_outputter.indentation = max(
            0,
            natural_language_outputter.indentation-1
        )

    def write(natural_language_outputter, string):
        natural_language_outputter.output(string)

    def indent(natural_language_outputter):
        natural_language_outputter.write(
            '    ' * natural_language_outputter.indentation
        )

from english import English
from french import French
