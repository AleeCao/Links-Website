import reflex as rx
from AleWebsite.Components.title import title
from AleWebsite.Styles.colors import Colors, TextColor

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="/avatar2.jpg", 
                size="8", 
                radius="full",
                bg=Colors.BACKGROUND.value,
                padding="2px",
                border=f'4.5px solid {Colors.SECONDARY.value}',
                ),
            rx.vstack(
                title("Hi, I’m Alexis Cao"),
                rx.text("@alee_cao", 
                        size="4", 
                        weight="bold",
                        color= Colors.PRIMARY.value
                        ),
                padding_y="0.5em",
            ),
        ),
        rx.text("""I'm a junior Backend, highly interested in developing and implementing microservices architecture.
        I am a System Engineer student who is interested in back-end software development and implement. I have experience in programing languages such as C; Python and Node js. (express and NestJS freamework). I have also knowledge in deployment, CI/CD tools and Cloud Services (AWS). 
        I would like to test my skills in a environment that could allow me to grow professionally.""", size="3",
        color= TextColor.BODY.value
        ),
        spacing='4',
        align="start",
    )