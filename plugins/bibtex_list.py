from pybtex.database.input import bibtex
from operator import itemgetter, attrgetter

from pelican.generators import Generator
from pelican import signals

import datetime
import os


def bibtex_to_markdown(bibfile):
    outstr = ""

    parser = bibtex.Parser()
    bib_data = parser.parse_file(bibfile)

    bib = sorted(
        bib_data.entries.items(),
        key=lambda item: int(item[1].fields["year"]),
        reverse=True,
    )

    index = 0
    for _, entry in bib:
        index += 1
        title = entry.fields["title"]
        short = entry.fields["short"]
        link = entry.fields["link"]
        authors = ", ".join(
            f"{a.first_names[0][0]}. {a.last_names[0]}" for a in entry.persons["author"]
        )
        authors = authors.replace("D. Petrisko", "**D. Petrisko**")
        authors = authors.replace("D. Ruelas-Petrisko", "**D. Ruelas-Petrisko**")
        outstr += f'{index}. {authors}. "{title}". [{short}]({link})\n'

    return outstr


class BibTeXListGenerator(Generator):

    def __init__(self, *args, **kwargs):
        super(BibTeXListGenerator, self).__init__(*args, **kwargs)

    def generate_context(self):
        """
        Called first for all generators. Populate the global context with data.
        """
        # Path to the bibtex file (customize as needed)
        bibfile = self.settings.get("BIBTEX_LIST_FILE", "content/papers/papers.bib")
        try:
            self.bibtex_markdown = bibtex_to_markdown(bibfile)
        except Exception as e:
            self.bibtex_markdown = f"Error parsing bibtex: {e}"
        # Add to global context for templates if desired
        self.context["bibtex_markdown"] = self.bibtex_markdown

    def generate_output(self, writer):
        """
        Called after generate_context. Generate output files using the writer.
        """
        # Output file path (customize as needed)
        output_path = self.settings.get("BIBTEX_LIST_OUTPUT", "output/bibtex_list.md")
        try:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(self.bibtex_markdown)
        except Exception as e:
            print(f"Error writing bibtex list: {e}")


def get_generators(generators):
    return BibTeXListGenerator


def register():
    signals.get_generators.connect(get_generators)
    signals.content_written.connect(lambda: BibTeXListGenerator().generate_output(None))
