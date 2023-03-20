import flet as ft
import logica as logica
import matplotlib
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart
import variables as var

matplotlib.use("svg")
def main(page: ft.Page):

    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }

    grafica = ft.Container()
    dlg = ft.AlertDialog(title=ft.Text("Los valores ingresados no son válidos⚠️😲🤔",color=ft.colors.BLACK),shape=ft.RoundedRectangleBorder(radius=4))
    
    def open_alert(e):
        page.dialog = dlg
        dlg.open= True
        page.update()

    def resolver(e:ft.ContainerTapEvent):
        c_bol = int(boletos.value)
        c_pr = int(premios.value)
        c_org = int(organizadores.value)
        if logica.verificar_entrada(c_bol,c_pr,c_org) == True and logica.verificar_numeros(c_bol,c_pr,c_org) == True:
            espacio = logica.espacio_muestral(c_bol,c_pr)
            pa,pb,pc,pd = probabilidad(c_bol,c_org,c_pr,espacio)
            valores=[pa,pb,pc,pd]
            print(valores)
        
            fig, ax = plt.subplots()
            ax.bar(var.puntos,valores,label = var.bar_labels, color = var.bar_colors)
            ax.set_ylabel("Probabilidad (%)")
            ax.set_xlabel("Evento")
            ax.set_title("Probabilidad de los Eventos")
            ax.legend()
            plt.ylim(0,100)
            plt.figure(figsize=(55,55))
            grafica.content = MatplotlibChart(fig, expand=False, isolated = True)

            probabilidad_eventos.value = "La probabilidad cálculada para los eventos es: " +"P(A) = " + str(pa) +" ,P(B) = "+ str(pb) + " ,P(C) = "+ str(pc) + " ,P(D) = "+ str(pd)

            page.update()
        else:
            open_alert(e)
    
    def probabilidad(boletos,organizadores,premios, espacio):
        #Resolviendo el punto a 
        comb_a = logica.combinatoria_simple(organizadores,premios)
        prob_a = logica.calcular_probabilidad(comb_a,espacio)
       
        # Resolviendo el punto b
        # n1_b = organizadores
        r1_b = logica.calcular_premios(premios)
        n2_b = boletos-organizadores
        r2_b = premios-r1_b
        comb_b = logica.combinatoria_doble(organizadores,r1_b,n2_b,r2_b)
        prob_b = logica.calcular_probabilidad(comb_b,espacio)

        #Resolviendo el punto c 
        #n1_c = organizadores
        #r1_c = 1
        #n2_c = n2_b
        r2_c = premios-1
        comb_c = logica.combinatoria_doble(organizadores,1,n2_b,r2_c)
        prob_c = logica.calcular_probabilidad(comb_c,espacio)

        #Resolviendo el punto d
        #n_d = n2_b
        #r_d = premios
        comb_d = logica.combinatoria_simple(n2_b,premios)
        prob_d = logica.calcular_probabilidad(comb_d,espacio)

        return prob_a,prob_b,prob_c,prob_d
    
    # Inicio págica web
    page.title = "Aplicación Estadística"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor ="#FFFFFF"

    page.appbar = ft.AppBar(
        automatically_imply_leading=False,
        title=ft.Text("Aplicación Probabilidad | Métodos de Conteo",color="#F5E9CF", size = 35),
        leading= ft.Icon(ft.icons.AREA_CHART_ROUNDED,color="#F5E9CF"),
        bgcolor= "#4D455D",
        actions=[
            ft.Container(ft.Text("© Catalina Cruz Ostos, 2023",color="#F5E9CF",italic=True,size=14),
                         padding=ft.Padding(right=30,left=0,bottom=0,top=0))
        ],
    )
    titulo = ft.Container(ft.Text("Enunciado del Problema 2.51", font_family="RobotoSlab",size=25, color = ft.colors.BLACK, text_align=ft.TextAlign.LEFT))
    enunciado = ft.Container(ft.Text("Una fraternidad local está realizado una rifa en la que se han de vender A boletos 🎟️, uno por cliente. Hay B premios 🏆 para ser concebidos. Si los C organizadores de la rifa compran un boleto cada uno. ¿Cuál es la probabilidad 📈 de que los C organizadores ganen...",size = 15,font_family="RobotoSlab"))
    preguntas = ft.Text("A. Todos los premios 🎉🤑🎉? \nB. Exactamente el 60% de los premios 😊🎖️😊? \nC. Exactamente uno de los premios 😒💰😒? \nD. Ninguno de los premios 😭😭😭",font_family="RobotoSlab")
    boletos= ft.TextField(label="Cantidad Boletos",border_color="#353E44",color= ft.colors.BLACK, hint_text=" 👁️ Ingrese valores positivos entre 10 y 100",
                         label_style=ft.TextStyle(color=ft.colors.BLACK,size=14))
    premios = ft.TextField(label="Cantidad Premios",border_color="#353E44",color=ft.colors.BLACK, hint_text=" 👁️ Ingrese valores positivos entre 2 y 10 (Menor a la cantidad de organizadores)",
                         label_style=ft.TextStyle(color=ft.colors.BLACK,size=14))
    organizadores = ft.TextField(label="Número Organizadores",border_color="#353E44",color=ft.colors.BLACK, hint_text=" 👁️ Ingrese valores positivos entre 3 y 11",
                         label_style=ft.TextStyle(color=ft.colors.BLACK,size=14))
    button = ft.ElevatedButton("Resolver",bgcolor="#E96479",color="#4D455D",scale=1.1,icon=ft.icons.ARROW_FORWARD_IOS,on_click = resolver)
    
    probabilidad_eventos = ft.Text(size=14)

    columna = ft.Column(controls=[titulo,enunciado,preguntas,boletos,premios,organizadores,button,probabilidad_eventos],
                        expand=True,spacing=10,horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.START)
    columna_dos = ft.Column(controls=[grafica,probabilidad_eventos], expand=True,spacing=2,horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.START)


    #Descripción del algoritmo 
    titulo_teoria = ft.Text("Teoría Aplicada")
    definicion = ft.Text("Combinatoria: https://es.wikipedia.org/wiki/Combinatoria ")

    espacio = ft.Text("DEFINICIÓN 2.4 Un espacio muestral discreto es aquel que está formado ya sea por un número finito o una contable de puntos muestrales distritos.")
    evento = ft.Text("DEFINICIÓN 2.2 Un evento simple no se puede descomponer. Cada evento simple corresponde a un punto muestral.")
    espacio_def = ft.Text("DEFINICIÓN 2.3 El espacio muestral asociado con un experimento es el conjunto formado por todos los posibles puntos muestrales.")
    referencia = ft.Container(ft.Text("Wackerly D., Mendenhall W. & Sheaffer R. (2010). Estadística matemática con aplicaciones (Sección N°2.6, Ejercicio N°2.51, pág. 49). México. Editorial: Cengage Learning Inc. Edición: Digital).",italic=True))
    creditos = ft.Text("© Juan Diego Suárez, por la referencia original. Contacto: judsuarez@udistrital.edu.co")

    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                content=ft.Container(
                    content=ft.Row(controls=[columna,columna_dos])
                ),
                tab_content= ft.Row(controls=[ft.Icon(ft.icons.SETTINGS,color="#4D455D"),
                                              ft.Text("Aplicación del Algoritmo",color="#4D455D")])
            ),
            ft.Tab(
                content=ft.Container(content=ft.Column(controls=[titulo_teoria,definicion,espacio,evento,espacio_def,referencia,creditos],expand=True,spacing=2,horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.END)),
                tab_content=ft.Row(controls=[ft.Icon(ft.icons.INSERT_CHART, color="#4D455D"),
                                             ft.Text("Descripción del Algoritmo", color="#4D455D")])
            ),
        ],
        expand=4,
    )
    page.add(t)
    

ft.app(target=main)


