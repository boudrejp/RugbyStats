### web scraper to take in data from ESPN Rugby StatsGuru
### author: boudrejp
### url: http://stats.espnscrum.com/statsguru/rugby/stats/index.html?class=1;page=1;spanmax1=08+Nov+2017;spanmax2=08+Nov+2017;spanmin1=08+Nov+2007;spanmin2=08+Nov+2015;spanval1=span;spanval2=span;template=results;type=player;view=match
### can simply loop thru page numbers: this query gives 1061 pages of results

import time
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import urllib

