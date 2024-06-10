import reflex as rx
from AleWebsite.Styles.styles import Size
from AleWebsite.Styles.styles import navbar_style
from AleWebsite.Styles.colors import Colors, TextColor

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text.span("ale", color = TextColor.BODY.value, weight="bold"),
            rx.text.span("dev", color = Colors.SECONDARY.value),
            style=navbar_style
        ),
        position='Sticky',
        bg= Colors.CONTENT.value,
        padding_x=Size.DEFAULT.value,
        padding_y=Size.MSMALL.value,
        z_index='999',
        top='0',
        )