THEME = "pelican-themes/Flex"

# Based of example: https://github.com/alexandrevicenzi/Flex/blob/master/docs/pelicanconf.py
# https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings

AUTHOR = "Daniel (Dan) Ruelas-Petrisko"
SITEURL = "http://localhost:8000"
SITENAME = "Dan Ruelas-Petrisko's Website"
SITETITLE = SITENAME
SITESUBTITLE = "PhD, Full-Stack ASIC Engineer, Open-Source Hardware Advocate"
SITEDESCRIPTION = (
    "Dan's personal blog about open-source hardware, software, and other topics."
)
SITELOGO = "/images/headshot.jpeg"
FAVICON = "/favicon.ico"
BROWSER_COLOR = "#333"
PYGMENTS_STYLE = "monokai"

ROBOTS = "index, follow"

PATH = "content"
OUTPUT_PATH = "output/"
TIMEZONE = "America/Los_Angeles"

DISABLE_URL_HASH = True

PLUGIN_PATHS = ["pelican-plugins", "plugins"]
PLUGINS = ["bibtex_list", "jinja2content"]

THEME_TEMPLATES_OVERRIDES = ["content/templates"]

GITHUB_USER = "dpetrisko"
GITHUB_USER_TYPE = "all"
#GITHUB_SORT_BY = "created"
#GITHUB_DIRECTION = "desc"

CC_LICENSE = {
    "name": "Creative Commons Attribution-NonCommercial-NoDerivatives",
    "version": "4.0",
    "slug": "by-nc-nd",
    "icon": True,
    "language": "en_US",
}

COPYRIGHT_YEAR = 2025

ARTICLE_PATHS = ["articles"]

STATIC_PATHS = ["extra", "images", "papers"]

PAGE_PATHS = ["pages"]

EXCLUDE_PATHS = ["content/gen"]

EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}

SOCIAL = (
    ("github", "https://github.com/dpetrisko"),
    ("linkedin", "https://www.linkedin.com/in/dpetrisko/"),
    ("orcid", "https://orcid.org/0000-0002-0555-6919"),
)

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = False
HOME_HIDE_TAGS = True

DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

LINKS_IN_NEW_TAB = False

GITHUB_CORNER_URL = "https://github.com/dpetrisko"

# Disable feeds to remove Atom link from navigation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

BIBTEX_LIST_FILE = "content/papers/refs.bib"
BIBTEX_LIST_OUTPUT = "content/gen/refs.md"

MARKDOWN = {
    "extension_configs": {
        "markdown_include.include": {
            "base_path": "content/gen",
            "encoding": "utf-8",
        },
    },
    "output_format": "html5",
}
