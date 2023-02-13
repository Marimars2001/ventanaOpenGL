from OpenGL.GL import *
import glfw
import math

def dibujar_cielo():
    glBegin(GL_TRIANGLES)
    #Cielo
    glColor3f(0.0,1.0,1.0)
    #Se ocupan tres vértices para que funcione.
    glVertex3f(-1.0,1.0,0.0)
    glVertex3f(-1.0,-0.5,0.0)
    glVertex3f(1.0,-0.5,0.0)
    
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-1.0,0.0)
    glVertex3f(-1.0,1.0,0.0)
    
    glEnd()

def dibujar_sol():
    glBegin(GL_TRIANGLE_FAN)
    #Sol
    glColor3f(1.0,1.0,0.0)
    circulo_x= 0.7
    circulo_y= 0.68
    glVertex3f(0.0 + circulo_x, 0.0 + circulo_y, 0.0)

    for grados in range(0,361,10):
        radianes= grados * math.pi/180.0
        glVertex3f(0.18 * math.cos(radianes) + circulo_x, 0.18 * math.sin(radianes) + circulo_y, 0.0)
    
    glEnd()

def dibujar_nube():
    glBegin(GL_TRIANGLE_FAN)
    #Nube
    glColor3f(1.0,1.0,1.0)
    circulo_x= 0.0
    circulo_y= 0.68
    glVertex3f(0.0 + circulo_x, 0.0 + circulo_y, 0.0)

    for grados in range(0,361,10):
        radianes= grados * math.pi/180.0
        glVertex3f(0.24 * math.cos(radianes) + circulo_x, 0.12 * math.sin(radianes) + circulo_y, 0.0)
    
    glEnd()

def dibujar_nube2():
    glBegin(GL_TRIANGLE_FAN)
    #Nube
    glColor3f(1.0,1.0,1.0)
    circulo_x= 0.1
    circulo_y= 0.58
    glVertex3f(0.0 + circulo_x, 0.0 + circulo_y, 0.0)

    for grados in range(0,361,10):
        radianes= grados * math.pi/180.0
        glVertex3f(0.30 * math.cos(radianes) + circulo_x, 0.12 * math.sin(radianes) + circulo_y, 0.0)
    
    glEnd()
    
def dibujar_nube3():
    glBegin(GL_TRIANGLE_FAN)
    #Nube
    glColor3f(1.0,1.0,1.0)
    circulo_x= -0.1
    circulo_y= 0.58
    glVertex3f(0.0 + circulo_x, 0.0 + circulo_y, 0.0)

    for grados in range(0,361,10):
        radianes= grados * math.pi/180.0
        glVertex3f(0.30 * math.cos(radianes) + circulo_x, 0.12 * math.sin(radianes) + circulo_y, 0.0)
    
    glEnd()

def dibujar_cesped():
    glBegin(GL_TRIANGLE_STRIP)
    #Cesped
    glColor3f(0.0,1.0,0.0)
    glVertex3f(-1.0,-0.5,0.0)
    glVertex3f(-1.0,-1.5,0.0)
    glVertex3f(1.0,-0.5,0.0)
    glVertex3f(1.0,-1.5,0.0)
    
    glEnd()

def dibujar_hojas():
    glBegin(GL_TRIANGLE_FAN)
    #Hojas
    glColor3f(0.0,1.0,0.0)
    circulo_x= -0.7
    circulo_y= -0.1
    glVertex3f(0.0 + circulo_x, 0.0 + circulo_y, 0.0)

    for grados in range(0,361,10):
        radianes= grados * math.pi/180.0
        glVertex3f(0.20 * math.cos(radianes) + circulo_x, 0.18 * math.sin(radianes) + circulo_y, 0.0)
    
    glEnd()
    
def dibujar_hojas2():
    glBegin(GL_TRIANGLE_FAN)
    #Hojas
    glColor3f(0.0,1.0,0.0)
    circulo_x= -0.3
    circulo_y= -0.1
    glVertex3f(0.0 + circulo_x, 0.0 + circulo_y, 0.0)

    for grados in range(0,361,10):
        radianes= grados * math.pi/180.0
        glVertex3f(0.20 * math.cos(radianes) + circulo_x, 0.18 * math.sin(radianes) + circulo_y, 0.0)
    
    glEnd()

def dibujar_hojas3():
    glBegin(GL_TRIANGLE_FAN)
    #Hojas
    glColor3f(0.0,1.0,0.0)
    circulo_x= -0.5
    circulo_y= -0.1
    glVertex3f(0.0 + circulo_x, 0.0 + circulo_y, 0.0)

    for grados in range(0,361,10):
        radianes= grados * math.pi/180.0
        glVertex3f(0.20 * math.cos(radianes) + circulo_x, 0.18 * math.sin(radianes) + circulo_y, 0.0)
    
    glEnd()

def dibujar_hojas4():
    glBegin(GL_TRIANGLE_FAN)
    #Hojas
    glColor3f(0.0,1.0,0.0)
    circulo_x= -0.6
    circulo_y= 0.1
    glVertex3f(0.0 + circulo_x, 0.0 + circulo_y, 0.0)

    for grados in range(0,361,10):
        radianes= grados * math.pi/180.0
        glVertex3f(0.20 * math.cos(radianes) + circulo_x, 0.18 * math.sin(radianes) + circulo_y, 0.0)
    
    glEnd()

def dibujar_hojas5():
    glBegin(GL_TRIANGLE_FAN)
    #Hojas
    glColor3f(0.0,1.0,0.0)
    circulo_x= -0.4
    circulo_y= 0.1
    glVertex3f(0.0 + circulo_x, 0.0 + circulo_y, 0.0)

    for grados in range(0,361,10):
        radianes= grados * math.pi/180.0
        glVertex3f(0.20 * math.cos(radianes) + circulo_x, 0.18 * math.sin(radianes) + circulo_y, 0.0)
    
    glEnd()

def dibujar_hojas6():
    glBegin(GL_TRIANGLE_FAN)
    #Hojas
    glColor3f(0.0,1.0,0.0)
    circulo_x= -0.5
    circulo_y= 0.2
    glVertex3f(0.0 + circulo_x, 0.0 + circulo_y, 0.0)

    for grados in range(0,361,10):
        radianes= grados * math.pi/180.0
        glVertex3f(0.20 * math.cos(radianes) + circulo_x, 0.22 * math.sin(radianes) + circulo_y, 0.0)
    
    glEnd()

def dibujar_arbol():
    glBegin(GL_TRIANGLE_FAN)
    #Árbol
    glColor3f(0.0,0.0,1.0)
    #Se ocupan tres vértices para que funcione.
    glVertex3f(-0.6,-0.1,0.0)
    glVertex3f(-0.6,-0.8,0.0)
    glVertex3f(-0.4,-0.8,0.0)
    glVertex3f(-0.4,-0.2,0.0)
    
    glEnd()

def dibujar_casa():
    glBegin(GL_TRIANGLE_FAN)
    #Casa
    glColor3f(1.0,0.0,0.0)
    glVertex3f(0.0,0.0,0.0)
    glVertex3f(0.0,-0.8,0.0)
    glVertex3f(0.8,-0.8,0.0)
    glVertex3f(0.8,0.0,0.0)
    
    #Techo
    glColor3f(1.0,1.0,0.0)
    glVertex3f(0.9,0.0,0.0)
    glVertex3f(0.4,0.6,0.0)
    glVertex3f(-0.1,0.0,0.0)
    
    glEnd()

def dibujar_ventana():
    glBegin(GL_TRIANGLE_FAN)
    #Ventana
    glColor3f(0.0,1.0,1.0)
    glVertex3f(0.4,-0.1,0.0)
    glVertex3f(0.4,-0.4,0.0)
    glVertex3f(0.7,-0.4,0.0)
    glVertex3f(0.7,-0.1,0.0)
    
    glEnd()
    
def dibujar_puerta():
    glBegin(GL_TRIANGLE_FAN)
    #Puerta
    glColor3f(1.0,0.0,1.0)
    glVertex3f(0.1,-0.8,0.0)
    glVertex3f(0.1,-0.4,0.0)
    glVertex3f(0.3,-0.4,0.0)
    glVertex3f(0.3,-0.8,0.0)
    
    glEnd()

def dibujar_point():
    glBegin(GL_POINTS)
    
    glColor3f(1.0,1.0,0.0)
    glVertex3f(-0.2,0.0,0.0)
    
    glEnd()
    
def dibujar_lineas_strip():
    glBegin(GL_LINE_STRIP)
    
    glColor3f(1.0,0.0,0.0)
    glVertex3f(0.0,0.0,0.0)
    glVertex3f(-0.7,0.8,0.0)
    glVertex3f(0.4,-0.1,0.0)
    glVertex3f(0.35,-0.6,0.0)
    
    glEnd()

def dibujar_line_loop():
    glBegin(GL_LINE_LOOP)
    
    glColor3f(1.0,1.0,0.0)
    glVertex3f(0.0,0.0,0.0)
    glVertex3f(-0.7,0.8,0.0)
    glVertex3f(0.4,-0.1,0.0)
    glVertex3f(0.35,-0.6,0.0)
    
    glEnd()

def main():
    width= 700
    height= 700
    
    #Inicializar el GLFW.
    if not glfw.init():
        return
    #Declarar la ventana.
    window= glfw.create_window(width, height, "Mi ventana", None, None)
    #Configuraciones de OpenGL.
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    #Verificación de la creación de la vemtana.
    if not window:
        glfw.terminate()
        return
    #Establcer el contexto.
    glfw.make_context_current(window)
    #Imprimir versión (...Siempre es bueno saberlo...).
    version= glGetString(GL_VERSION)
    print(version)
    #Ciclo de dibujo (Draw Loop= Do while)
    while not glfw.window_should_close(window):
        #Establecer el viewport
        glViewport(0,0,width,height) 
        #Establecer el color de borrado.
        glClearColor(0.5,0.5,0.5,1.0)
        #Borrar contenido del viewport.
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        #Dibujar tipos:
        #Triangules
        #Triangules_strip
        #Triangules_fan
        #Point
        #Lineas
        #Lineas_strip
        #Line_loop
        
        dibujar_cielo()
        dibujar_sol()
        dibujar_nube()
        dibujar_nube2()
        dibujar_nube3()
        dibujar_cesped()
        dibujar_arbol()
        dibujar_hojas()
        dibujar_hojas2()
        dibujar_hojas3()
        dibujar_hojas4()
        dibujar_hojas5()
        dibujar_hojas6()
        dibujar_casa()
        dibujar_puerta()
        dibujar_ventana()
        
        #Polling de inputs
        glfw.poll_events()
        
        #Cambiar los buffers.
        glfw.swap_buffers(window)
    
    #Acabar con los procesos y uso de memoria.
    glfw.destroy_window(window)
    glfw.terminate()
    
    #Ejecutar el main.
if __name__ == "__main__":
    main()