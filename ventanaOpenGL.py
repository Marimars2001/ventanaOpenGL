from OpenGL.GL import *
import glfw

def main():
    width= 400
    height= 600
    
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
        
        #Polling de inputs
        glfw.poll_events()
        #Cambiar los buffers.
        glfw.swap_buffers(window)
    #Acabar con los procesos y uso de memoria.
    glfw.destroy_window(window)
    glfw.terminate()
    
    #Ejecutar el main.
    if __name__== "__main__":
        main()