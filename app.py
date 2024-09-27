import socket
import threading
import tkinter as tk

# ... (código do servidor e cliente)
# Função para criar a interface gráfica 
def criar_interface(): 
    janela = tk.Tk()
    janela.title("Chatpy")

    #... (criar os elementos da interface)
    # Botão para chamar o encarregando 
    botao_encarregado = tk.button(janela, text="Chamar Encarregado", command=chamar_encarregado)
    botao_encarregado.pack()

    #... (outros elementos)

    janela.mainloop()
# função para ativar/desativar a notificação
def chamar_encarregado():
    #... (lógica para enviar a mensagem e ativar a notificação)
    label_noticacao.config(text="Encarregado Chamado!")
    #... (outras funçoes)
if __name__ == "__main__"
    #iniciar o servidor em uma thread separado
    thread_servidor = threading.Thread(target=iniciar_servidor)
    thread_servidor.start()

    #criar a interface grafica
    criar_interface()
