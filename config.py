# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "22656556"))
API_HASH = getenv("API_HASH", "dc4ec57887041a067ca3f6d61d1e90cd")
BOT_TOKEN = getenv("BOT_TOKEN", "7486530187:AAFbfYpTf6XzGjz7rx40xgo-sLHbAAmL98U")
OWNER_ID = int(getenv("OWNER_ID", "7439745006"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://saini190204:DcuR9S8Bi8fIkMuQ@cluster0.sabffnh.mongodb.net/")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002158373839"))
FORCESUB = getenv("FORCESUB", "-1002135170253")
