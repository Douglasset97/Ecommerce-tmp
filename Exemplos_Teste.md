Exemplo: Como Matar os Mutantes Sobreviventes.

Baseado nos resultados do mutation testing, assim são exemplos de como adicionar testes para matar os mutantes que sobreviveram.

Mutante 1: nota > 100 → nota >= 100

Problema: Não há teste para nota = 100
Solução: Adicionar teste para verificar que 100 é uma nota válida

def test_deve_retornar_aprovado_para_nota_100():
    assert classificar_nota(100) == "Aprovado"

Mutante 2: nota < 0 → nota <= 0

Problema: Não há teste para nota = 0
Solução: Adicionar teste para verificar que 0 é uma nota válida

def test_deve_retornar_reprovado_para_nota_0():
    assert classificar_nota(0) == "Reprovado"


Mutante 3: nota >= 60 → nota > 60
Problema: Não há teste específico para nota = 60
Solução: Você já tem, mas pode reforçar:

from classificador import classificar_nota

def test_deve_retornar_aprovado_para_nota_alta():
    assert classificar_nota(85) == "Aprovado"

def test_deve_retornar_reprovado_para_nota_baixa():
    assert classificar_nota(40) == "Reprovado"

def test_deve_retornar_nota_invalida_para_nota_negativa():
    assert classificar_nota(-5) == "Nota inválida"

def test_deve_retornar_reprovado_para_nota_0():
    assert classificar_nota(0) == "Reprovado"

def test_deve_retornar_aprovado_para_nota_limite_50():
    assert classificar_nota(50) == "Aprovado"

def test_deve_retornar_reprovado_para_nota_limite_49():
    assert classificar_nota(49) == "Reprovado"

def test_deve_retornar_aprovado_para_nota_500():
    assert classificar_nota(500) == "Aprovado"

def test_deve_retornar_nota_invalida_para_nota_501():
    assert classificar_nota(501) == "Nota inválida"

def test_deve_retornar_nota_invalida_para_nota_acima_de_500():
    assert classificar_nota(1000) == "Nota inválida"

// Se você utilizar o pytest, basta rodar //

pytest test_classificador.py

def test_deve_retornar_aprovado_para_nota_limite_60():
    assert classificar_nota(60) == "Aprovado"

Teste Completo Recomendado
Adicione estes testes ao seu test_classificador.py:


Após Adicionar os Testes
Execute os testes para verificar se passam:

python -m pytest test_classificador.py -v

Execute mutation testing novamente:

mutmut run

Verifique se os mutantes foram mortos:

mutmut results
