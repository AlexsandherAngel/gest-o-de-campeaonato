import sys
from collections import deque

class Campeonato:
    def __init__(self):
        self.jogadores = {}
        self.times = {}
        self.confrontos = deque()
        self.resultados = []

    def validar_nome(self, texto):
        return all(c.isalpha() or c.isspace() for c in texto) and texto.strip() != ""

    def cadastrar_jogador(self):
        while True:
            nome = input("Nome do jogador: ").strip()
            if self.validar_nome(nome):
                break
            print("Nome inválido. Digite apenas letras e espaços.")

        if nome in self.jogadores:
            print("Jogador já cadastrado.")
            return

        while True:
            idade = input("Idade: ")
            if idade.isdigit():
                idade = int(idade)
                break
            print("Idade inválida. Digite um número.")

        while True:
            posicao = input("Posição: ").strip()
            if self.validar_nome(posicao):
                break
            print("Posição inválida. Digite apenas letras e espaços.")

        self.jogadores[nome] = {"idade": idade, "posicao": posicao, "time": None}
        print(f"Jogador {nome} cadastrado com sucesso.")

    def montar_time(self):
        while True:
            nome_time = input("Nome do time: ").strip()
            if nome_time:
                break
            print("Nome do time não pode ser vazio.")

        if nome_time in self.times:
            print("Time já existe.")
            return

        nomes = input("Nomes dos jogadores (separados por vírgula): ").split(",")
        jogadores_validos = []

        for nome in nomes:
            nome = nome.strip()
            if nome in self.jogadores:
                if self.jogadores[nome]["time"] is None:
                    jogadores_validos.append(nome)
                else:
                    print(f"Jogador {nome} já pertence ao time {self.jogadores[nome]['time']}.")
            else:
                print(f"Jogador {nome} não cadastrado.")

        if not jogadores_validos:
            print("Nenhum jogador válido foi adicionado.")
            return

        self.times[nome_time] = jogadores_validos
        for jogador in jogadores_validos:
            self.jogadores[jogador]["time"] = nome_time

        print(f"Time '{nome_time}' montado com os jogadores: {', '.join(jogadores_validos)}.")

    def realizar_confronto(self):
        if len(self.times) < 2:
            print("É necessário pelo menos dois times para realizar um confronto.")
            return

        time1 = input("Nome do primeiro time: ").strip()
        time2 = input("Nome do segundo time: ").strip()

        if time1 == time2:
            print("Não é possível agendar confronto entre o mesmo time.")
            return

        if time1 not in self.times or time2 not in self.times:
            print("Um ou ambos os times não existem.")
            return

        self.confrontos.append((time1, time2))
        print(f"Confronto entre '{time1}' e '{time2}' agendado.")

    def listar_jogadores(self):
        if not self.jogadores:
            print("Nenhum jogador cadastrado.")
            return
        for nome, dados in self.jogadores.items():
            print(f"{nome} - Idade: {dados['idade']}, Posição: {dados['posicao']}, Time: {dados['time']}")

    def listar_confrontos(self):
        if not self.confrontos:
            print("Nenhum confronto agendado.")
            return
        for i, (t1, t2) in enumerate(self.confrontos, 1):
            print(f"{i}. {t1} vs {t2}")

    def finalizar_confronto(self):
        if not self.confrontos:
            print("Nenhum confronto para finalizar.")
            return

        print("Confrontos agendados:")
        for i, (t1, t2) in enumerate(self.confrontos, 1):
            print(f"{i}. {t1} vs {t2}")

        while True:
            escolha = input("Escolha o número do confronto a ser finalizado: ")
            if escolha.isdigit():
                escolha = int(escolha)
                if 1 <= escolha <= len(self.confrontos):
                    break
            print("Escolha inválida.")

        confronto = self.confrontos[escolha - 1]
        time1, time2 = confronto

        while True:
            placar1 = input(f"Gols do {time1}: ")
            placar2 = input(f"Gols do {time2}: ")
            if placar1.isdigit() and placar2.isdigit():
                placar1, placar2 = int(placar1), int(placar2)
                break
            print("Digite apenas números inteiros para os gols.")

        resultado = {
            "confronto": f"{time1} vs {time2}",
            "placar": f"{time1} {placar1} x {placar2} {time2}"
        }
        self.resultados.append(resultado)
        self.confrontos.remove(confronto)

        print(f"Resultado registrado: {resultado['placar']}")

def menu():
    campeonato = Campeonato()
    while True:
        print("\nMenu:")
        print("1. Cadastrar Jogador")
        print("2. Montar Time")
        print("3. Realizar Confronto")
        print("4. Listar Jogadores")
        print("5. Listar Confrontos")
        print("6. Finalizar Confronto")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            campeonato.cadastrar_jogador()
        elif opcao == "2":
            campeonato.montar_time()
        elif opcao == "3":
            campeonato.realizar_confronto()
        elif opcao == "4":
            campeonato.listar_jogadores()
        elif opcao == "5":
            campeonato.listar_confrontos()
        elif opcao == "6":
            campeonato.finalizar_confronto()
        elif opcao == "7":
            print("Encerrando o programa.")
            sys.exit()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
