@startuml herenca composicao

title Diagrama de Classes

class Sala{
    - nrsala:Int 
    - capacidade:Int
    - assento: String
    + construtor(nrsala, capacidade,assento)
}

class Sessao{
    - nrsessao:Int
    - dtsessao:Date
    - hrsessao:String
    + construtor(nrsessao, dtsessao, hrsessao)
    
}

class Filme{
    - nome: String
    - classificacao: String
    - tempoduracao: String
    + construtor(nome, classificacao, tempoduracao)
    
       
}

class Cinema{
    - nome: String
    - cnpj:String
    - end: String
    + construtor(nome, cnpj, end)
    
}

class Ingresso{
    - nringresso:Int
    - valor: Float
    - sala: Sala
    - sessao: Sessao
    - filme: Filme  
    - cinema: Cinema 
    + construtor(nringresso,valor, sala, sessao,filme, cinema)
    
   
}

class Pessoa{
    - nome:String
    - cpf:String
    - email:String
    - ingresso: Ingresso
    - pedido_lanche: PedidoLanche  
    + construtor(nome, cpf, email, ingresso, pedido_lanche)
    + chamar_nome(nome)
    + chamar_valoringresso(valor)
    + chamar_item01_combo01(item01)

}
class PedidoLanche{
    - nrpedido: Int
    - valor: Float 
    - combo01: Combo01
    - combo02: Combo02
    + construtor(nrpedido, valor,combo01,combo02)
    + validarvalor(valor)
}
class Combo01{
    - item01:String
    - item02:String
    + construtor(item01, item02)
    
}
class Combo02{
    - item01:String
    - item02:String   
    + construtor(item01, item02)
    
     
}
Pessoa *-- Ingresso: compra/Composição
Pessoa *-- PedidoLanche: compra/Composição
PedidoLanche o-- Combo01
PedidoLanche o-- Combo02 

Ingresso o-- Sala
Ingresso o-- Sessao 
Ingresso o-- Filme 
Ingresso o-- Cinema 


@enduml 