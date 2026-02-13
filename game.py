import flet as ft

def main(page: ft.Page):
    mensagem = ft.Text("Escolha a raça correta do cachorro!!", color="#4d3018")
    resposta_correta = "Pastor Alemão"

    def verificar_resposta(e):
        if e.control.content == resposta_correta:
            mensagem.value = "Parabéns, você acertou!!"
        else:
            mensagem.value = "Resposta errada"    
        page.update()

    page.bgcolor = "#dbc79d"
    page.title = "Game: Adivinhe a imagem"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "Adivinhe a Imagem",
                    size=24,
                    weight="bold"
                ),
                ft.Image(
                    src="images/zaza.jpg",
                    height=200
                ),
                ft.Row(
                    controls=[
                        ft.Button(
                            content="Spitz-Alemão",
                            bgcolor="brown",
                            color="white",
                            on_click=verificar_resposta
                        ),
                        ft.Button(
                            content="Pastor Alemão",
                            bgcolor="brown",
                            color="white",
                            on_click=verificar_resposta
                        ),
                        ft.Button(
                            content="Golden Retriever",
                            bgcolor="brown",
                            color="white",
                            on_click=verificar_resposta
                        )
                    ],
                    alignment=ft.CrossAxisAlignment.CENTER,
                    wrap=True
                ),
                mensagem
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.run(main)