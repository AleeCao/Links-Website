import reflex as rx
from AleWebsite.Styles.styles import Size
import AleWebsite.Styles.styles as styles

        
def button_link(text: str, url: str, icon: str) -> rx.Component:  
        return rx.link(
            rx.button(
                rx.hstack(
                    rx.image(
                        src=icon,
                        width=styles.Size.DEFAULT.value,
                        heigth=styles.Size.DEFAULT.value,
                        margin=styles.Size.MSMALL.value,
                    ),
                    rx.vstack(
                        rx.text(
                            text,
                            style=styles.button_text,
                        ),
                        align="start",
                        padding_top=styles.Size.MSMALL.value,
                    ),
                    width="100%",
                    align_items='start',
                ),
                width="100%",
            ),
            href=url,
            width="100%",
            is_external=True,
        )