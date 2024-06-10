import reflex as rx

def footer() -> rx.Component:
    return rx.hstack(
        rx.image(src="favicon.ico", width="100px", height="auto")
        
    )