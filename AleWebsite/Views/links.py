import reflex as rx
from AleWebsite.Components.title import title
from AleWebsite.Styles.styles import Size
from AleWebsite.Components.link_button import button_link

def links() -> rx.Component:
    return rx.vstack(
        rx.heading("These are my links", font_size=Size.BMEDIUM.value),
        button_link("GitHub", "https://github.com/AleeCao", "/icons/github.svg"),
        button_link("LinkedIn", "https://www.linkedin.com/in/alexis-cao", "/icons/linkedin.svg"),
        button_link("Docker example", "https://github.com/AleeCao/Practicas_Docker", "/icons/docker.svg"),
        button_link("NodeJS example", "https://github.com/AleeCao/Login--Nodejs-MySQL-", "/icons/node.svg"),
        button_link("Python example", "https://github.com/AleeCao/TPFinal", "/icons/python.svg"),
        button_link("Website code", "https://github.com/AleeCao/Links-Website", "/icons/web.svg"),
        rx.heading("Contact", font_size=Size.BMEDIUM.value, padding_top= Size.MEDIUM.value),
        button_link("Email", "mailto:ale.9c9gmail.com", "/icons/email.svg"),
        width="100%",
        spacing='3',
        padding_top= Size.MEDIUM.value,
    )