from src.archtypes.game import Game
from src.archtypes.audio import Audio
from src.archtypes.book import Book
from src.archtypes.imageset import ImageSet
from src.archtypes.software import Software
from src.archtypes.video import Video

TYPEMAP = {
    "Audio": Audio,
    "Book": Book,
    "Game": Game,
    "ImageSet": ImageSet,
    "Software": Software,
    "Video": Video
}
