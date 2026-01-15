from pelican.generators import Generator
from pelican import signals

import datetime
import os
import requests

class GitHubListGenerator(Generator):

    def __init__(self, *args, **kwargs):
        super(GitHubListGenerator, self).__init__(*args, **kwargs)

    def generate_context(self):
        """
        Called first for all generators. Populate the global context with data.
        """
        username = self.settings.get('GITHUB_USER')
        user_type = self.settings.get('GITHUB_USER_TYPE', 'owner')
        projects_list = self.settings.get('GITHUB_PROJECTS_LIST')
        if username:
            url = f"https://api.github.com/users/{username}/repos?type={user_type}"
            try:
                response = requests.get(url)
                response.raise_for_status()
                repos = response.json()
                # Filter to selected projects if list is provided
                if projects_list:
                    repos = [r for r in repos if r.get('name') in projects_list]
                # Sort by updated_at descending
                repos.sort(key=lambda x: x.get('updated_at', ''), reverse=True)
                # Create list of projects
                projects = []
                for repo in repos:
                    project = {
                        'name': repo.get('name', ''),
                        'description': repo.get('description', '') or '',
                        'language': repo.get('language', '') or 'Unknown',
                        'html_url': repo.get('html_url', ''),
                        'updated_at': datetime.datetime.fromisoformat(repo.get('updated_at', '').replace('Z', '+00:00')) if repo.get('updated_at') else None,
                        'stars': repo.get('stargazers_count', 0),
                        'forks': repo.get('forks_count', 0),
                        'upstream_url': None
                    }
                    if repo.get('fork'):
                        # Fetch full repo details to get upstream
                        owner_repo = '/'.join(repo['html_url'].split('/')[-2:])
                        full_url = f"https://api.github.com/repos/{owner_repo}"
                        try:
                            full_response = requests.get(full_url)
                            full_response.raise_for_status()
                            full_repo = full_response.json()
                            project['upstream_url'] = full_repo.get('source', {}).get('html_url')
                        except Exception as e:
                            print(f"Error fetching upstream for {owner_repo}: {e}")
                    projects.append(project)
                self.context['github_projects'] = projects
            except Exception as e:
                print(f"Error fetching GitHub projects: {e}")
                self.context['github_projects'] = []
        else:
            self.context['github_projects'] = []

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
