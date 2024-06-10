import reflex as rx
import AleWebsite.Styles.styles as styles


def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        style=styles.title_style,
        align="center",
    )
    