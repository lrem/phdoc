"""
This near trivial extension makes MathJax formulas AtomicStrings.
"""

import markdown


class MathJaxInlinePattern(markdown.inlinepatterns.Pattern):
    """
    Pattern for in-line math, recommended.
    """

    def __init__(self):
        markdown.inlinepatterns.Pattern.__init__(self,
                r'(?<!\\)(\\\()(.+?)(\\\))')

    def handleMatch(self, m):
        # This would be better if I could return AtomicString...
        node = markdown.util.etree.Element('span')
        node.text = markdown.util.AtomicString('\(' + m.group(3) + '\)')
        return node


class MathJaxInlinePattern2(markdown.inlinepatterns.Pattern):
    """
    Pattern for in-line math, single-dollars.
    """

    def __init__(self):
        markdown.inlinepatterns.Pattern.__init__(self,
                r'(?<!\\)(\$)(.+?)(\$)')

    def handleMatch(self, m):
        # This would be better if I could return AtomicString...
        node = markdown.util.etree.Element('span')
        node.text = markdown.util.AtomicString('$' + m.group(3) + '$')
        return node


class MathJaxBlockPattern(markdown.inlinepatterns.Pattern):
    """
    Pattern for block math. Note that block refers to mathjax behaviour, we
    allow this element in-line in the markup.
    """

    def __init__(self):
        markdown.inlinepatterns.Pattern.__init__(self,
                r'(?<!\\)(\\\[)(.+?)(\\\])')

    def handleMatch(self, m):
        # This would be better if I could return AtomicString...
        node = markdown.util.etree.Element('span')
        node.text = markdown.util.AtomicString('\[' + m.group(3) + '\]')
        return node


class MathJaxExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        # Needs to come before escape matching because \ is pretty important
        # in LaTeX
        md.inlinePatterns.add('mathjaxi', MathJaxInlinePattern(), '<escape')
        md.inlinePatterns.add('mathjaxi2', MathJaxInlinePattern2(), '<escape')
        md.inlinePatterns.add('mathjaxb', MathJaxBlockPattern(), '<escape')


def makeExtension(configs=None):
    return MathJaxExtension(configs)
