import sys

tarefas = []
contador_id = 1


def validar_titulo():
    """Valida o título garantindo que não seja vazio nem composto apenas por espaços."""
    while True:
        titulo = input("Digite o Título da tarefa (Obrigatório): ").strip()
        if titulo:
            return titulo
        print("❌ Erro: O título é obrigatório e não pode ficar em branco. Tente novamente.\n")


def validar_prioridade():
    """Garante o domínio fechado de prioridades: Alta, Média ou Baixa."""
    opcoes_validas = {
        "alta": "Alta",
        "média": "Média",
        "media": "Média",
        "baixa": "Baixa"
    }
    while True:
        prioridade_input = input("Digite a Prioridade (Alta, Média ou Baixa): ").strip().lower()
        if prioridade_input in opcoes_validas:
            return opcoes_validas[prioridade_input]
        print("❌ Erro: Opção inválida! Escolha apenas entre Alta, Média ou Baixa.\n")


def cadastrar_tarefa():
    """Cadastra a tarefa com ID sequencial e Status inicial 'Pendente'."""
    global contador_id
    print("\n------------------------------------")
    print("      CADASTRO DE NOVA TAREFA       ")
    print("------------------------------------")
    
    titulo = validar_titulo()
    descricao = input("Digite a Descrição (Opcional): ").strip()
    prioridade = validar_prioridade()
    data_limite = input("Digite a Data Limite (ex: DD/MM/AAAA): ").strip()
    
    nova_tarefa = {
        "id": contador_id,
        "titulo": titulo,
        "descricao": descricao if descricao else "Sem descrição",
        "prioridade": prioridade,
        "data_limite": data_limite if data_limite else "Não informada",
        "status": "Pendente"
    }
    
    tarefas.append(nova_tarefa)
    contador_id += 1
    print(f"\n✅ Tarefa '{titulo}' cadastrada com sucesso! [ID: {nova_tarefa['id']}]")


def visualizar_tarefas():
    """Exibe as tarefas cadastradas ou informa se a lista estiver vazia."""
    print("\n------------------------------------")
    print("    LISTA DE TAREFAS CADASTRADAS    ")
    print("------------------------------------")
    
    if not tarefas:
        print("ℹ️ Nenhuma tarefa cadastrada até o momento.")
        return

    pendentes = 0
    concluidas = 0

    for t in tarefas:
        print(f"\n[ID #{t['id']}] {t['titulo']}")
        print(f"  • Descrição:  {t['descricao']}")
        print(f"  • Prioridade: {t['prioridade']}")
        print(f"  • Data Limite: {t['data_limite']}")
        print(f"  • Status:     {t['status']}")
        
        if t['status'] == "Pendente":
            pendentes += 1
        else:
            concluidas += 1

    print("\n------------------------------------")
    print(f"Resumo: Total: {len(tarefas)} | Pendentes: {pendentes} | Concluídas: {concluidas}")


def menu_principal():
    """Loop contínuo da Interface de Linha de Comando (CLI)."""
    while True:
        print("\n====================================")
        print("        TASKTRACKER - MENU          ")
        print("====================================")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")
        
        opcao = input("\nEscolha uma opção (1-3): ").strip()
        
        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            print("\nSaindo do TaskTracker... Até logo!")
            sys.exit(0)
        else:
            print("❌ Opção inválida! Digite 1, 2 ou 3.")


if __name__ == "__main__":
    menu_principal()
