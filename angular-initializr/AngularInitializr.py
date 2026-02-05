import os
import sys


def setup_angular_project():
    print("--- 🛠️  Angular Architect Initializr + Feature Generator ---")

    # 1. Caminho do Projeto
    raw_path = input("👉 Cole o caminho absoluto do projeto Angular: ").strip()
    clean_path = raw_path.replace('"', '').replace("'", "")
    base_path = os.path.abspath(clean_path)
    app_path = os.path.join(base_path, "src", "app")

    if not os.path.exists(os.path.join(base_path, "package.json")):
        print(f"\n❌ ERRO: package.json não encontrado em: {base_path}")
        return

    # 2. Nome da Feature Inicial
    feature_name = input("📦 Nome da Feature inicial (ex: manga-catalog): ").strip().lower().replace(" ", "-")

    # Estrutura Global
    global_folders = [
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
        "shared/validators"
    ]

    asset_folders = ["src/assets/data", "src/assets/images/icons"]

    print(f"\n🏗️  Estruturando projeto...")

    # Criar Pastas Globais
    for folder in global_folders:
        path = os.path.join(app_path, folder)
        os.makedirs(path, exist_ok=True)
        open(os.path.join(path, ".gitkeep"), "a").close()
        print(f"✅ [Global] {folder}")

    # Criar Estrutura da Feature (O seu XPTO)
    if feature_name:
        feature_path = os.path.join(app_path, "features", feature_name)
        feature_subs = ["services", "pages", "models"]

        for sub in feature_subs:
            path = os.path.join(feature_path, sub)
            os.makedirs(path, exist_ok=True)

        # Criar o arquivo de routing da feature
        routing_file = f"{feature_name}-routing.module.ts"
        with open(os.path.join(feature_path, routing_file), "w") as f:
            f.write(f"// Routing module for {feature_name}\n")
            f.write("// Configure suas rotas de feature aqui\n")

        print(f"🚀 [Feature] {feature_name} (services, pages, models, routing)")

    # Criar Assets
    for folder in asset_folders:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        print(f"✅ [Assets] {folder}")

    print("\n✨ Estrutura completa aplicada com sucesso!")


if __name__ == "__main__":
    try:
        setup_angular_project()
    except KeyboardInterrupt:
        print("\n\n👋 Operação cancelada.")
        sys.exit()