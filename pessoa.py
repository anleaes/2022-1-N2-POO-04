class Pessoa:
    def __init__(self, nome,cpf, rg, idade):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.idade = idade
    
    def nome_paciente(self):
        return print("o nome do funcionario é: ", self.pessoa.paciente.nome)
    def nome_funcionario(self):
        return print("o nome do funcionario é: ", self.pessoa.funcionario.nome)
    def endereco_casa_pessoa(self):
        return print("endereço da rua da pessoa ", self.pessoa.nome, "é ", self.endereco.rua)
    def endereco_posto_paciente(self):
        return print("o posto fica na rua ",self.posto.endereco.rua)
    def endereco_posto_funcionario(self):
        return print("o posto fica na rua ",self.posto.endereco.rua)
    def nome_do_posto(self):
        return print(self.posto.nome)
    def dia_consulta(self):
        return print(self.agendamento_ficha)
    def numero_carteirinha(self):
        return print(self.carteirinha_de_vacinacao.registro_carteirinha)
    def calendario_nacional(self):
        return print(self.calendario_nacional_vacinacao.calendario)
    def Vacinas(self):
        return print(self.vacinas.nome)
    def Vacinas_fabricante(self):
        return print(self.vacinas.fabricante)

p1 = Pessoa(889, 'alberto', 'joão', 'gerson alegre', 'muttley', '400.289.22', 558893, 18)