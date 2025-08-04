from pywinauto.application import Application
import time

# Usa backend "uia" que é compatível com UWP/XAML
app = Application(backend="uia").start("notepad.exe")
time.sleep(2)  # Dá tempo para a janela abrir

# Descobre o nome real da janela
for w in app.windows():
    print("Janela encontrada:", w.window_text())

# Ajuste aqui conforme o nome impresso acima
janela = app.window(title_re=".*Bloco de Notas")

# Espera a janela estar pronta
janela.wait('visible', timeout=10)

# Escreve no campo de texto (Notepad moderno usa Edit control)
editor = janela.child_window(control_type="Edit")
editor.wait('ready', timeout=5)
editor.type_keys("Olá Mundo!", with_spaces=True)
