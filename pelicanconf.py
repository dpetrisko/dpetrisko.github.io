THEME = "pelican-themes/Flex"

# Based of example: https://github.com/alexandrevicenzi/Flex/blob/master/docs/pelicanconf.py
# https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings

AUTHOR = "Daniel (Dan) Ruelas-Petrisko"
SITEURL = "http://localhost:8000"
SITENAME = "Dan's Blog"
SITETITLE = "About Dan"
SITESUBTITLE = "Open-Source ASICs"
SITEDESCRIPTION = "Dan's personal blog about open-source hardware, software, and other topics."
SITELOGO = "/images/bp_logo.png"
FAVICON = "/favicon.ico"
BROWSER_COLOR = "#333"
PYGMENTS_STYLE = "monokai"

ROBOTS = "index, follow"

PATH = "content"
OUTPUT_PATH = "output/"
TIMEZONE = "America/Los_Angeles"

DISABLE_URL_HASH = True

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["sitemap"]

CC_LICENSE = {
    "name": "Creative Commons Attribution-NonCommercial-NoDerivatives",
    "version": "4.0",
    "slug": "by-nc-nd",
    "icon": True,
    "language": "en_US"
}

COPYRIGHT_YEAR = 2025

STATIC_PATHS = ["images", "articles", "docs", "extra"]

EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"}
}

SOCIAL = (
    ("github", "https://github.com/dpetrisko"),
    ("linkedin", "https://www.linkedin.com/in/dpetrisko/")
)

#CUSTOM_CSS = ""

MAIN_MENU = True

# Translate to English.
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

LINKS_IN_NEW_TAB = False

GITHUB_CORNER_URL = "https://github.com/dpetrisko"
