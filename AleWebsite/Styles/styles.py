from enum import Enum
import reflex as rx
from .colors import Colors, TextColor
from .fonts import Font

#Constants for the website
MAX_WIDTH = "700px"

#Sizes for the website
class Size(Enum):
    ZERO = "0! important"
    SMALL = "0.5em"
    MSMALL = "0.8em"
    MEDIUM = "1.25em"
    BMEDIUM = "1.5em"
    DEFAULT = "2em"
    LARGE = "3em"
    XLARGE = "4em"
    
#Base styles for the website
BASE_STYLE = {
    "background_color": Colors.BACKGROUND.value,
    "color": TextColor.HEADER.value,
    "font_family": Font.BODY.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.MSMALL.value,
        "background_color": Colors.CONTENT.value,
        "color": TextColor.BODY.value,
        "cursor": "pointer",
        "_hover": {
            "color": TextColor.HEADER.value,
            "background_color": Colors.ALTERNATIVE.value,
            },
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {},
    }
}

button_text = dict(
    font_size=Size.MEDIUM.value,
    weight="bold",
)

title_style = dict(
    font_size=Size.DEFAULT.value,
    weight="bold",
    width="100%",
)

navbar_style = dict(
    font_size=Size.BMEDIUM.value,
    width="100%",
)