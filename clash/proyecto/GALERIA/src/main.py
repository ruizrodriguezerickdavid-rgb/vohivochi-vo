import flet as ft


def main(page: ft.Page):
    page.title="Galeria"
    page.bgcolor=ft.Colors.BLACK38

    cartas = [
        {
            "nombre": "pekka",
            "tipo": "tanque",
            "daño":"muy alto",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/vohivochi-vo/refs/heads/main/prkka.jpg",     
        },  
        { 
            "nombre": "bambardero",
            "tipo": "tropa",
            "daño":"mediano y de area ",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/vohivochi-vo/refs/heads/main/bombas.jpg",
        },
        {
            "nombre": "dragones esqueleto",
            "tipo": "aerea",
            "daño":"madiano y en area",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/vohivochi-vo/refs/heads/main/dra%20esque.jpg",
        },  
        {
            "nombre": "duendes",
            "tipo": "tropa",
            "daño":"poco alto",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/vohivochi-vo/refs/heads/main/duesndes.jpg",
        },
        {
            "nombre": "bola de fuego",
            "tipo": "hechizo",
            "daño":"area",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/vohivochi-vo/refs/heads/main/fuego.jpg",
        },
        {
            "nombre": "duendes con lanza",
            "tipo": "tropa",
            "daño":"normal",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/vohivochi-vo/refs/heads/main/lanza.jpg",
        },
        {
            "nombre": "mago",
            "tipo": "tropa",
            "daño":"alto y en area",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/vohivochi-vo/refs/heads/main/mago.jpg",
            
        },   
        {
            "nombre": "lapida",
            "tipo": "estructura",
            "daño":"bajo",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/vohivochi-vo/refs/heads/main/lanza.jpg",
        },
        {
            "nombre": "murcielagos",
            "tipo": "aerea",
            "daño":"poco alto",
            "imagen": "https://raw.githubusercontent.com/ruizrodriguezerickdavid-rgb/vohivochi-vo/refs/heads/main/murcie.jpg",            
        },
    ]

    indice_actual=[0]

    contenedor=ft.Container(
        content=ft.Column([]),
        width=500,
        height=580,
        bgcolor=ft.Colors.BLUE_300,
        alignment=ft.alignment.center,
        padding=30
    )

    boton_siguiente = ft.ElevatedButton(text="Siguiente sobreviviente")

    def mostrar_carta():
        carta=cartas[indice_actual[0]]
        contenedor.content=ft.Column([
            ft.Image(src=carta["imagen"],width=300,height=300,fit=ft.ImageFit.CONTAIN),
            ft.Text(carta["nombre"],size=20,weight=ft.FontWeight.BOLD),
            ft.Text(f"Daño: {carta ['daño']}",size=16),
            ft.Text(f"Tipo: {carta ["tipo"]}",size=14,italic=True)
        ],alignment=ft.MainAxisAlignment.CENTER)
        
        if indice_actual[0]==len(cartas)-1:
            boton_siguiente.text="Volver al inicio"
        else:
            boton_siguiente.text="Siguiente carta"
        page.update()

    def siguiente_click(e):
        indice_actual[0]=(indice_actual[0]+1)%len(cartas)
        mostrar_carta()
    boton_siguiente.on_click=siguiente_click



    page.add(
        ft.Container(
            content=ft.Column([
                contenedor,
                boton_siguiente
            ],alignment=ft.MainAxisAlignment.CENTER,
              horizontal_alignment=ft.CrossAxisAlignment.CENTER,
              spacing=20
        ),

            alignment=ft.alignment.center,
            expand=True
        )
    ) 
    mostrar_carta() 


ft.app(main)
