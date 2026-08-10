import os

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
EMAIL_FROM        = os.environ.get("EMAIL_FROM")
EMAIL_PASSWORD    = os.environ.get("EMAIL_PASSWORD")
EMAIL_TO          = os.environ.get("EMAIL_TO")

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
TOP_N     = 5

RSS_FEEDS = [
    # Hardware e Mini PC
    ("Tom's Hardware",    "https://www.tomshardware.com/feeds/all"),
    ("Phoronix",          "https://www.phoronix.com/rss.php"),
    ("NotebookCheck",     "https://www.notebookcheck.net/News.8.0.html?utm_source=rss&utm_medium=rss"),
    # Community Mini PC
    ("r/MiniPCs",         "https://www.reddit.com/r/MiniPCs/.rss"),
    ("r/AMD",             "https://www.reddit.com/r/Amd/.rss"),
    ("r/linux_gaming",    "https://www.reddit.com/r/linux_gaming/.rss"),
    # Linux su Mini PC
    ("GamingOnLinux",     "https://www.gamingonlinux.com/article_rss.php"),
]

BOOST_KEYWORDS = [
    # Mini PC brand
    "mini pc", "minipc", "beelink", "minisforum", "gmktec", "trigkey",
    "nipogi", "acemagic", "asus nuc", "intel nuc",
    # CPU/GPU rilevanti
    "ryzen", "amd apu", "rdna", "radeon", "780m", "890m", "880m",
    "ryzen ai", "strix point", "hawk point", "phoenix",
    "intel core ultra", "arc graphics", "xe graphics",
    # Annunci e release
    "announced", "released", "launch", "benchmark",
    "annunciato", "rilasciato", "prestazioni",
    # Linux su Mini PC
    "linux", "steamos", "bazzite", "cachyos",
    # RAM e storage
    "lpddr5", "ddr5", "nvme", "m.2",
]

PENALTY_KEYWORDS = [
    # Elettrodomestici e accessori casa
    "aspirapolvere", "lavapavimenti", "robot pulizia", "rowenta",
    "lavatrice", "frigorifero", "televisore", "smart tv",
    "microonde", "forno", "climatizzatore",
    # Desktop tower e server
    "desktop tower", "workstation", "server rack",
    "threadripper", "epyc", "xeon",
    # Mobile
    "smartphone", "iphone", "android", "tablet",
    "laptop", "notebook",
    # Gaming generico non Mini PC
    "xbox game pass", "playstation", "nintendo",
    "console gaming", "ps5", "xbox series",
    # Fuori tema
    "nft", "crypto", "blockchain", "metaverse",
    "dash cam", "smartwatch", "cuffie",
    # Offerte generiche
    "amazon offerta", "sconto amazon", "coupon",
    "black friday", "prime day",
]
