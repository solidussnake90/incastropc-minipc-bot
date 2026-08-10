import os

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
EMAIL_FROM        = os.environ.get("EMAIL_FROM")
EMAIL_PASSWORD    = os.environ.get("EMAIL_PASSWORD")
EMAIL_TO          = os.environ.get("EMAIL_TO")

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
TOP_N     = 5

RSS_FEEDS = [
    # Mini PC e hardware
    ("Tom's Hardware",    "https://www.tomshardware.com/feeds/all"),
    ("Tom's Hardware IT", "https://www.tomshw.it/rss_news.xml"),
    ("Phoronix",          "https://www.phoronix.com/rss.php"),
    ("AnandTech",         "https://www.anandtech.com/rss/"),
    ("NotebookCheck",     "https://www.notebookcheck.net/News.8.0.html?utm_source=rss&utm_medium=rss"),
    # Community Mini PC
    ("r/MiniPCs",         "https://www.reddit.com/r/MiniPCs/.rss"),
    ("r/linux_gaming",    "https://www.reddit.com/r/linux_gaming/.rss"),
    ("r/AMD",             "https://www.reddit.com/r/Amd/.rss"),
    # Italiani
    ("HWUpgrade",         "https://www.hwupgrade.it/rss/news.xml"),
    ("Everyeye",          "https://www.everyeye.it/rss_news.xml"),
    # Linux gaming
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
    "snapdragon x",
    # Annunci e release
    "announced", "released", "launch", "benchmark", "review",
    "annunciato", "rilasciato", "prestazioni", "benchmark",
    # Linux su Mini PC
    "linux", "steamos", "bazzite", "cachyos",
    # RAM e storage
    "lpddr5", "ddr5", "nvme", "m.2",
]

PENALTY_KEYWORDS = [
    # Desktop tower e server
    "desktop tower", "workstation", "server rack",
    "threadripper", "epyc", "xeon",
    # Mobile non Mini PC
    "smartphone", "iphone", "android", "tablet",
    "laptop", "notebook",
    # Fuori tema
    "nft", "crypto", "blockchain", "metaverse",
    "playstation", "xbox", "nintendo",
    "dash cam", "smart tv", "smartwatch",
]
