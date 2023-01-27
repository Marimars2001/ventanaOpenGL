from OpenGL.GL import *
import glfw

def dibujar_triangulos():
    glBegin(GL_TRIANGLES)
    
    glColor3f(1.0,0.0,0.0)
    glVertex3f(-1.0,0.0,0.0)
    glColor3f(0.0,0.0,1.0)
    glVertex3f(0.0,1.0,0.0)
    glColor3f(0.0,1.0,0.0)
    glVertex3f(1.0,0.0,0.0)
    
    glColor3f(1.0,0.0,1.0)
    glVertex3f(0.0,-0.3,0.0)
    glVertex3f(-0.7,-0.9,0.0)
    glVertex3f(0.6,-0.7,0.0)
    
    glEnd()

def Dibujar_point():
    glBegin(GL_POINTS)
    
    glColor3f(1.0,1.0,0.0)
    glVertex3f(-0.2,0.0,0.0)
    
    glEnd()

def Dibujar_lineas():
    glBegin(GL_LINES)
    
    glColor3f(1.0,1.0,0.0)
    #Se ocupan dos vértices para que funcione.
    glVertex3f(-0.7,0.8,0.0)
    glVertex3f(0.0,0.0,0.0)
    
    glEnd()
    
def Dibujar_lineas_strip():
    glBegin(GL_LINE_STRIP)
    
    glColor3f(1.0,0.0,0.0)
    glVertex3f(0.0,0.0,0.0)
    glVertex3f(-0.7,0.8,0.0)
    glVertex3f(0.4,-0.1,0.0)
    glVertex3f(0.35,-0.6,0.0)
    
    glEnd()

def Dibujar_line_loop():
    glBegin(GL_LINE_LOOP)
    
    glColor3f(1.0,1.0,0.0)
    glVertex3f(0.0,0.0,0.0)
    glVertex3f(-0.7,0.8,0.0)
    glVertex3f(0.4,-0.1,0.0)
    glVertex3f(0.35,-0.6,0.0)
    
    glEnd()

def main():
    width= 400
    height= 400
    
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
        
        #Dibujar
        #dibujar_triangulos()
        #Dibujar_point()
        #Dibujar_lineas()
        #Dibujar_lineas_strip()
        Dibujar_line_loop()
        
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