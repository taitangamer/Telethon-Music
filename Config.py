import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "21840776"))
    API_HASH = os.environ.get("API_HASH", "a83dc6bea8b64c2191b2fe631f1097a9")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3b9730e0042579e85c243.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/3b9730e0042579e85c243.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5418102507")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
