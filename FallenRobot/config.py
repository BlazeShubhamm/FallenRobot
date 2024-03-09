class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 22347692
    API_HASH = "f6104693b63671c0fa92343ca8e22183"

    CASH_API_KEY = "QWY7Y3V1DCLJSFP7"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://zjnkdsga:nsbtJ01ry62-bmkAKhT7RkZbkwuuhxNy@rain.db.elephantsql.com/zjnkdsga"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002050018620)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://blazeshubham:blazeshubham@cluster0.exxpe0n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "DevilsHeavenMF"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6740360553:AAHVJz-WmRfz6LvNxAoYpdI1xO4NvM97d7M"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "B8BMO8EJAM51"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1356469075  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
