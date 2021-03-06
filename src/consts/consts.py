import os

HOME_PATH = os.environ['HOMEPATH'].replace('\\', '/')
DEFAULT_DIR = HOME_PATH + '/Downloads'

DL_EPISODE = 1
DL_SEASON = 2
DL_SERIES = 3
CHANGE_SERIES = 4

URL_REGEX_PATTERN = r'https?:\/\/.+\/watch\/.*\/season\/[0-9]+\/episode\/[0-9]+'
DRIVER_NAME = 'chromedriver.exe'
CONFIG_NAME = 'config.txt'

VIDEO_HTML_ID = 'videojs_html5_api'
SEARCH_BAR_ID = 'liveSearch'
SERIES_NAME_XPATH = '//*[@id="watchEpisode"]/div[1]/div/h1/strong/span'

MB = 1_000_000

WAIT_FPS = 5
LOADING_TIME = 32
PROGRESS_BAR_CHAR = '█'
PROGRESS_BAR_LEN = 400
TK_PAD = 50

def WATCH_URL(SITE_URL):
    return SITE_URL + 'watch'

def SEARCH_URL(SITE_URL):
    return SITE_URL + 'search'

DEFAULT_CONFIG_VARS = {
    'site': 'sdarot.space',
    'headless': True
}