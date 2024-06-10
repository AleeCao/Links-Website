import reflex as rx
from AleWebsite.Components.navbar import navbar
from AleWebsite.Components.footer import footer
from AleWebsite.Views.header import header
from AleWebsite.Views.links import links
import AleWebsite.Styles.styles as styles

from rxconfig import config


class State(rx.State):
    pass

@rx.page(
    title="Links Website",
    image="/lightning.png",
)
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                align='center',
                max_width=styles.MAX_WIDTH,
                width='100%',
                margin_y=styles.Size.DEFAULT.value,
                padding=styles.Size.MSMALL.value
            )
        ),
    )

    

app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets = [
        "https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap",
    ]
)
app.add_page(index)
