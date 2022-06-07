#arquivo externo com os comandos para testar os métodos.
#criado métodos em classe pessoa e classe funcionário
#Lucas pode criar alguns outros métodos! 
# e usar esse arquivo aqui para comunicação tb
#só comentar com #

from pessoa import *
from endereco import *
from funcionario import *



e1 = Endereco (9879879, 'bento gonçalves', 'vila nova', 'canoas')
p1 = Pessoa(91790248, 'ipiranga 59', 'jardim vila nova', 'poa', 'DIEGO',99999,6546,36)
p1.chamar_nome()
p1.chamar_endereco_rua()






