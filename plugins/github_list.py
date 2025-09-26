from pelican.generators import Generator
from pelican import signals


class GitHubListGenerator(Generator):

    def __init__(self, *args, **kwargs):
        super(GitHubListGenerator, self).__init__(*args, **kwargs)

    def generate_context(self):
        """
        Called first for all generators. Populate the global context with data.
        """
        # Path to the GitHub file (customize as needed)
        bibfile = self.settings.get("GitHub_LIST_FILE", "content/papers/papers.bib")
        try:
            self.github_markdown = GitHub_to_markdown(bibfile)
        except Exception as e:
            self.github_markdown = f"Error parsing GitHub: {e}"
        # Add to global context for templates if desired
        self.context["github_markdown"] = self.github_markdown

    def generate_output(self, writer):
        """
        Called after generate_context. Generate output files using the writer.
        """
        # Output file path (customize as needed)
        output_path = self.settings.get("GitHub_LIST_OUTPUT", "output/GitHub_list.md")
        try:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(self.github_markdown)
        except Exception as e:
            print(f"Error writing GitHub list: {e}")


def get_generators(generators):
    return GitHubListGenerator


def register():
    signals.get_generators.connect(get_generators)
    #signals.content_written.connect(lambda: GitHubListGenerator().generate_output(None))


def initialize(gen):
    if not 'GITHUB_USER' in gen.settings.keys():
        logger.warning('GITHUB_USER not set')
    else:
        gen.plugin_instance = GithubProjects(gen)

def fetch(gen, metadata):
    gen.context['github_projects'] = gen.plugin_instance.process()


#def register():
#    signals.article_generator_init.connect(initialize)
#    signals.article_generator_context.connect(fetch)