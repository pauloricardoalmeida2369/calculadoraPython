class Calculadora:
    def soma(self, primeiro, segundo):
        return primeiro + segundo

    def subtracao(self, primeiro, segundo):
        return primeiro - segundo

    def multiplicacao(self, primeiro, segundo):
        return primeiro * segundo

    def divisao(self, primeiro, segundo):
        if segundo == 0:
            return "Não é possível dividir por zero."
        return primeiro / segundo


class View:
    def start(self):
        print("Bem-vindo à Calculadora Python\n")
        return self.menu()

    def menu(self):
        print("1 - Para somar dois números")
        print("2 - Para subtrair dois números")
        print("3 - Para multiplicar dois números")
        print("4 - Para dividir dois números")
        print("0 - Sair")

        return int(input("\nDigite a opção: "))

    def get_operando(self):
        print("\nDigite os valores a serem calculados")

        primeiro = int(input("O primeiro valor: "))
        segundo = int(input("O segundo valor: "))

        return primeiro, segundo

    def mostrar_resultado(self, resultado):
        print(f"O resultado calculado foi: {resultado}\n")

    def finalizar(self):
        print("Programa finalizado!")


def main():
    calculadora = Calculadora()
    view = View()

    while True:
        opcao = view.start()

        if opcao == 0:
            view.finalizar()
            break

        if opcao in (1, 2, 3, 4):
            primeiro, segundo = view.get_operando()

            if opcao == 1:
                resultado = calculadora.soma(primeiro, segundo)
            elif opcao == 2:
                resultado = calculadora.subtracao(primeiro, segundo)
            elif opcao == 3:
                resultado = calculadora.multiplicacao(primeiro, segundo)
            elif opcao == 4:
                resultado = calculadora.divisao(primeiro, segundo)

            view.mostrar_resultado(resultado)
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()