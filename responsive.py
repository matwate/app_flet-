import flet as ft

def main(page: ft.Page):
    page.title = "Responsive App"

    # Crea un layout vertical principal
    main_layout = ft.Column(
        expand=True,
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Crea un TextView
    text = ft.Text(value="¡Esta es una aplicación responsive!", text_align=ft.TextAlign.CENTER)

    # Crea una imagen
    image = ft.Image(
        src=f"/images/logo.png",
        fit=ft.ImageFit.CONTAIN,
        repeat=ft.ImageRepeat.NO_REPEAT,
    )

    # Agrega los controles al layout principal
    main_layout.controls.append(text)
    main_layout.controls.append(image)

    # Agrega el layout principal a la página
    page.add(main_layout)

ft.app(target=main, assets_dir="assets")