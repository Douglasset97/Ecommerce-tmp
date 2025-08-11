from classificador import classificar_nota


def test_deve_retornar_aprovado_para_nota_alta():
    assert classificar_nota(85) == "Aprovado"


def test_deve_retornar_reprovado_para_nota_baixa():
    assert classificar_nota(40) == "Reprovado"


def test_deve_retornar_nota_invalida_para_nota_negativa():
    assert classificar_nota(-5) == "Nota inválida"


# Adicao de novos testes para matar os mutantes sobreviventes

# def test_deve_retornar_reprovado_para_nota_0():
#     """Testa o limite inferior válido (0)"""
#     assert classificar_nota(0) == "Reprovado"


# def test_deve_retornar_aprovado_para_nota_limite_50():
#     """Testa exatamente o limite de aprovação (50)"""
#     assert classificar_nota(50) == "Aprovado"


# def test_deve_retornar_reprovado_para_nota_limite_49():
#     """Testa logo abaixo do limite de aprovação (49)"""
#     assert classificar_nota(59) == "Reprovado"


# def test_deve_retornar_aprovado_para_nota_500():
#     assert classificar_nota(500) == "Aprovado"


# def test_deve_retornar_nota_invalida_para_nota_501():
#     """Testa exatamente uma nota acima do limite válido"""
#     assert classificar_nota(501) == "Nota inválida"


# def test_deve_retornar_nota_invalida_para_nota_acima_de_500():
#     assert classificar_nota(500) == "Nota inválida"
