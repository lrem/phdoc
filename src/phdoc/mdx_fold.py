"""
An extension for blocks that start hidden,
but can be shown when the viewer wants it.
These are marked up as blockquote with ``fold`` class.
The motivation is adding abstracts to publication lists.
"""

import re
import markdown


class FoldExtension(markdown.Extension):

    def extendMarkdown(self, md, md_globals):
        """
        Add `FoldBlockProcessor` to the Markdown instance.
        """
        md.parser.blockprocessors.add('fold_block',
                                      FoldBlockProcessor(md.parser),
                                      '>quote')


class FoldBlockProcessor(markdown.blockprocessors.BlockProcessor):
    """
    Pretty much the original BlockQuoteProcessor with an additional class.
    """

    RE = re.compile(r'(^|\n)[ ]{0,3}\|[ ]?(.*)')

    def test(self, parent, block):
        return bool(self.RE.search(block))

    def run(self, parent, blocks):
        block = blocks.pop(0)
        m = self.RE.search(block)
        if m:
            before = block[:m.start()]  # Lines before blockquote
            # Pass lines before blockquote in recursively for parsing first.
            self.parser.parseBlocks(parent, [before])
            # Remove ``| `` from begining of each line.
            block = '\n'.join([self.clean(line) for line in
                               block[m.start():].split('\n')])
        sibling = self.lastChild(parent)
        if sibling and sibling.tag == "blockquote":
            # Previous block was a blockquote so set that as this blocks parent
            quote = sibling
        else:
            # This is a new blockquote.
            # Create a new parent element.
            quote = markdown.util.etree.SubElement(parent,
                                                   'blockquote',
                                                   {'class': 'fold'}
                                                   )
        # Recursively parse block with blockquote as parent.
        # change parser state so blockquotes embedded in lists use p tags
        self.parser.state.set('fold_block')
        self.parser.parseChunk(quote, block)
        self.parser.state.reset()

    def clean(self, line):
        """ Remove ``|`` from beginning of a line. """
        m = self.RE.match(line)
        if line.strip() == "|":
            return ""
        elif m:
            return m.group(2)
        else:
            return line
