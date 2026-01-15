from pelican.generators import Generator
from pelican import signals

import datetime
import os
import requests
from collections import defaultdict

class GitHubListGenerator(Generator):

    def __init__(self, *args, **kwargs):
        super(GitHubListGenerator, self).__init__(*args, **kwargs)

    def generate_context(self):
        """
        Called first for all generators. Populate the global context with data.
        """
        projects_list = self.settings.get('GITHUB_PROJECTS_LIST')
        if projects_list:
            repos = []
            for project in projects_list:
                org = project.get('org')
                name = project.get('name')
                if org and name:
                    url = f"https://api.github.com/repos/{org}/{name}"
                    try:
                        response = requests.get(url)
                        response.raise_for_status()
                        repo = response.json()
                        repos.append(repo)
                    except Exception as e:
                        print(f"Error fetching GitHub repo {org}/{name}: {e}")
            # Now process repos
            # Sort by updated_at descending
            repos.sort(key=lambda x: x.get('updated_at', ''), reverse=True)
            # Create list of projects
            projects = []
            project_types = {p['name']: p['type'] for p in projects_list}
            for repo in repos:
                project = {
                    'name': repo.get('name', ''),
                    'description': repo.get('description', '') or '',
                    'language': repo.get('language', '') or 'Unknown',
                    'html_url': repo.get('html_url', ''),
                    'updated_at': datetime.datetime.fromisoformat(repo.get('updated_at', '').replace('Z', '+00:00')) if repo.get('updated_at') else None,
                    'stars': repo.get('stargazers_count', 0),
                    'forks': repo.get('forks_count', 0),
                    'upstream_url': None,
                    'type': project_types.get(repo.get('name'), 'unknown')
                }
                projects.append(project)

            github_projects_by_type = defaultdict(list)
            for p in projects:
                github_projects_by_type[p['type']].append(p)
            self.context['github_projects_by_type'] = dict(github_projects_by_type)
        else:
            self.context['github_projects_by_type'] = {k: [] for k in ['lead', 'maintainer', 'contributor', 'tester']}

    def generate_output(self, writer):
        """
        Called after generate_context. Generate output files using the writer.
        """
        # Not needed for template usage, but keeping for compatibility
        pass


def get_generators(generators):
    return GitHubListGenerator


def register():
    signals.get_generators.connect(get_generators)
