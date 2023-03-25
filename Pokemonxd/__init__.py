# poke PLAYER

from Pokemonxd.modules.core.app import App
from Pokemonxd.modules.core.bot import Bot
from Pokemonxd.modules.core.dir import dirr
from Pokemonxd.modules.core.git import git
from Pokemonxd.misc import dbb, heroku, sudo

from .console import LOGGER

# Directories
dirr()

# Check Git Updates
# git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
bot = Bot()

# Assistant Client
app = App()

from Pokemonxd.utilities.media import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
