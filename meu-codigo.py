# projeto_interface
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Dicionário para login
usuarios = {
    "chuudoloona": "senha1",
    "haerindonewjeans": "senha2"
}

# Funções
def fazer_login():  # Login por usuário e senha
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Usuário autenticado:", usuario)
        abrir_proxima_tela()
    else:
        messagebox.showerror("Erro de Login", "Usuário ou senha incorretos")

def abrir_proxima_tela():  # Próxima tela
    janela.withdraw()
    proxima_tela = tk.Toplevel(janela)
    proxima_tela.title("Segunda Tela")

    label = tk.Label(proxima_tela, text="Bem-vindo ao fretinho!", font=("Arial", 30))
    label.pack(expand=True, fill="both")

def abrir_tela_novo_usuario():
    global entry_novo_usuario, entry_nova_senha
    janela_novo_usuario = tk.Toplevel(janela)
    janela_novo_usuario.title("Cadastro de Novo Usuário")

    label_novo_usuario = tk.Label(janela_novo_usuario, text="Novo Usuário:", font=("Arial", 16))
    label_novo_usuario.pack(pady=10)

    entry_novo_usuario = tk.Entry(janela_novo_usuario, font=("Arial", 16))
    entry_novo_usuario.pack(pady=10)

    label_nova_senha = tk.Label(janela_novo_usuario, text="Nova Senha:", font=("Arial", 16))
    label_nova_senha.pack(pady=10)

    entry_nova_senha = tk.Entry(janela_novo_usuario, show="*", font=("Arial", 16))
    entry_nova_senha.pack(pady=10)

    botao_criar_usuario = tk.Button(janela_novo_usuario, text="Criar Usuário", command=criar_novo_usuario, font=("Arial", 16))
    botao_criar_usuario.pack(pady=10)

def criar_novo_usuario():
    novo_usuario = entry_novo_usuario.get()
    nova_senha = entry_nova_senha.get()
    if novo_usuario and nova_senha:
        if novo_usuario not in usuarios:
            usuarios[novo_usuario] = nova_senha
            messagebox.showinfo("Sucesso", "Novo usuário cadastrado com sucesso.")
        else:
            messagebox.showerror("Erro", "Usuário já existe.")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("600x400")  # Tamanho inicial da janela

# Imagem de fundo
caminho_para_imagem = "C:/Users/bryan/Downloads/fretinhoproject.jpeg"
imagem_fundo = Image.open(caminho_para_imagem)
imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

fundo_label = tk.Label(janela, image=imagem_fundo)
fundo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Container para login
container_login = tk.Frame(janela, bg="white", width=300, height=200)
container_login.place(relx=0.5, rely=0.5, anchor="center")

# entrada para o nome de usuário
label_usuario = tk.Label(container_login, text="Usuário:", font=("Arial", 16))
label_usuario.pack(pady=10)

entry_usuario = tk.Entry(container_login, font=("Arial", 16))
entry_usuario.pack(pady=10)

# entrada para a senha
label_senha = tk.Label(container_login, text="Senha:", font=("Arial", 16))
label_senha.pack(pady=10)

entry_senha = tk.Entry(container_login, show="*", font=("Arial", 16))
entry_senha.pack(pady=10)

# botão de login
botao_login = tk.Button(container_login, text="Login", command=fazer_login, font=("Arial", 16))
botao_login.pack(pady=10)

# botão de novo usuário
botao_novo_usuario = tk.Button(container_login, text="Novo Usuário", command=abrir_tela_novo_usuario, font=("Arial", 16))
botao_novo_usuario.pack(pady=10)

janela.mainloop()
