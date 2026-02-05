import os
import sys


def setup_angular_project():
    print("--- 🛠️  Angular Architect Initializr ---")

    raw_path = input("👉 Cole o caminho absoluto do projeto Angular: ").strip()

    # Limpa aspas que o Windows costuma adicionar (Ex: "C:\Pasta" -> C:\Pasta)
    clean_path = raw_path.replace('"', '').replace("'", "")

    # Normaliza o caminho para o formato do Sistema Operacional
    base_path = os.path.abspath(clean_path)
    app_path = os.path.join(base_path, "src", "app")

    # Verifica se o package.json existe para confirmar que é um projeto Angular
    if not os.path.exists(os.path.join(base_path, "package.json")):
        print(f"\n❌ ERRO: Não encontramos um projeto Angular em: {base_path}")
        print("Certifique-se de que você criou o projeto com 'ng new' antes de rodar este script.")
        return

    # Estrutura de pastas da sua Clean Architecture
    folders = [
        "core/auth",
        "core/models",
        "core/services",
        "core/interceptors",
        "core/guards",
        "core/config",
        "core/layout",

        "shared/components",
        "shared/pipes",
        "shared/directives",
        "shared/utils",
        "shared/validators",

        "features"
    ]

    asset_folders = ["src/assets/data", "src/assets/images/icons"]

    print(f"\n🏗️  Estruturando projeto em: {base_path}\n")

    # Criar pastas do App
    for folder in folders:
        path = os.path.join(app_path, folder)
        os.makedirs(path, exist_ok=True)
        # Cria o .gitkeep
        open(os.path.join(path, ".gitkeep"), "a").close()
        print(f"✅ [App] {folder}")

    # Criar pastas de Assets
    for folder in asset_folders:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        print(f"✅ [Assets] {folder}")

    print("\n✨ Tudo pronto! Sua arquitetura está organizada e pronta para o commit.")


if __name__ == "__main__":
    try:
        setup_angular_project()
    except KeyboardInterrupt:
        print("\n\n👋 Operação cancelada pelo usuário.")
        sys.exit()