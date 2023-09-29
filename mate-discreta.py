#Generador automático de enfrentamientos o creador personalizado

import random
import flet as ft

def main(page: ft.Page):
    page.window_center()
    
    page.fonts = {
        "Pixels": "fonts/PixelifySans-VariableFont_wght.ttf",
        "Ubuntu-Bold": "fonts/Ubuntu-Bold.ttf",
        "GochiHand": "fonts/GochiHand-Regular.ttf"
    }

    page.theme = ft.Theme(font_family="Ubuntu-Bold")

    
    page.title = "Matematica Discreta (miniproyecto)"
    page.window_max_width=1000
    page.window_max_height=600
    page.bgcolor="#f1edd0"

    page.horizontal_alignment = 'CENTER'

    page.add(ft.Text(value="Simulador de enfrentamientos", size=30, text_align="CENTER", color="#55443d", weight="bold", font_family="GochiHand"))
    
    page.window_width=1000
    page.window_height=600
    
    page.window_resizable=False

    main_txt = ft.TextField(label="Ingrese los nombres de los ocho equipos...", text_align=ft.TextAlign.LEFT, 
                            width=600, border_color="#a0cab5", color="#55443d", 
                            label_style=ft.TextStyle(weight="bold", color="#55443d"),
                            text_style=ft.TextStyle(weight="bold", color="#55443d"))
    txt_versus = ft.Text(value="VS", text_align=ft.TextAlign.CENTER, color="#000706", weight="bold", font_family="Pixels", size=25)

    DragableAux = []

    def drag_accept(e):
        src = page.get_control(e.src_id)
        src.content.content.value = src.content.content.value
        src.content.bgcolor = src.content.bgcolor
        e.control.content.bgcolor = src.content.bgcolor
        e.control.content.content.value = src.content.content.value
        page.update()

    def shuffle():
        random.shuffle(DragableAux)
        page.update()

    def addToDragable():
        txt = main_txt.value
        DragableAux.append(ft.Draggable(
            group="number",
            content=ft.Container(
                width=100,
                height=35,
                bgcolor="#f38a8a",
                border_radius=5,
                content=ft.Text(txt, size=15, color="#000000", weight="bold"),
                alignment=ft.alignment.center,
            ),
        ))

    def addDragrable(e):
        txt =  main_txt.value
        if len(DragableAux) < 7:
            addToDragable()
            page.add(ft.Row(DragableAux, alignment=ft.MainAxisAlignment.CENTER))
            page.update()
            page.controls.pop()

        elif len(DragableAux) == 7:
            addToDragable()
            add_button.text = "Mezclar"
            page.add(ft.Row(DragableAux, alignment=ft.MainAxisAlignment.CENTER))
            addDragTarget()
            page.update()
        else:
            shuffle()
            page.update()

    def addDragTarget():
        page.add(ft.Container(height=35))
        page.add(
            ft.Row(
                [
                    ft.Container(width=50),
                    ft.DragTarget(
                        group="number",
                        content=ft.Container(
                            width=100,
                            height=35,
                            bgcolor="#a0cab5",
                            border_radius=5,
                            content=ft.Text("First", size=15, color="#55443d", weight="bold"),
                            alignment=ft.alignment.center,
                        ),
                        on_accept=drag_accept,
                    ),
                    ft.Container(width=100, content=txt_versus),
                    ft.DragTarget(
                        group="number",
                        content=ft.Container(
                            width=100,
                            height=35,
                            bgcolor="#a0cab5",
                            border_radius=5,
                            content=ft.Text("Second", size=15, color="#55443d", weight="bold"),
                            alignment=ft.alignment.center,
                        ),
                        on_accept=drag_accept,
                    ),
                    ft.Container(width=100),
                    ft.DragTarget(
                        group="number",
                        content=ft.Container(
                            width=100,
                            height=35,
                            bgcolor="#a0cab5",
                            border_radius=5,
                            content=ft.Text("Third", size=15, color="#55443d", weight="bold"),
                            alignment=ft.alignment.center,
                        ),
                        on_accept=drag_accept,
                    ),
                    ft.Container(width=100, content=txt_versus),
                    ft.DragTarget(
                        group="number",
                        content=ft.Container(
                            width=100,
                            height=35,
                            bgcolor="#a0cab5",
                            border_radius=5,
                            content=ft.Text("Fourth", size=15, color="#55443d", weight="bold"),
                            alignment=ft.alignment.center,
                        ),
                        on_accept=drag_accept,
                    ),
                    ft.Container(width=50),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Container(height=35),
            ft.Row(
                [
                    ft.DragTarget(
                        group="number",
                        content=ft.Container(
                            width=100,
                            height=35,
                            bgcolor="#a0cab5",
                            border_radius=5,
                            content=ft.Text("Finalist", size=15, color="#55443d", weight="bold"),
                            alignment=ft.alignment.center,
                        ),
                        on_accept=drag_accept,
                    ),
                    ft.Container(width=320, content=txt_versus),
                    ft.DragTarget(
                        group="number",
                        content=ft.Container(
                            width=100,
                            height=35,
                            bgcolor="#a0cab5",
                            border_radius=5,
                            content=ft.Text("Finalist", size=15, color="#55443d", weight="bold"),
                            alignment=ft.alignment.center,
                        ),
                        on_accept=drag_accept,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Container(height=35),
            ft.Row(
                [
                    ft.DragTarget(
                        group="number",
                        content=ft.Container(
                            width=100,
                            height=35,
                            bgcolor="#a0cab5",
                            border_radius=5,
                            content=ft.Text("Winner", size=15, color="#55443d", weight="bold"),
                            alignment=ft.alignment.center,
                        ),
                        on_accept=drag_accept,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )
  
    add_button = ft.ElevatedButton(text="Enviar", width=120, on_click=addDragrable, bgcolor="#55443d", color="#f1edd0")

    page.add(
        ft.Container(height=15),
        ft.Row(
            [
                main_txt,
                add_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Container(height=35)
    )

ft.app(target=main)