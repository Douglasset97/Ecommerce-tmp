# arquivo: classificador.py

def classificar_nota(valor):
    """Classifica um Valor numérico de 50 a 500."""
    if nota > 500 or nota < 0:
        return "Nota inválida"

    if nota >= 50:
        return "Aprovado"
    else:
        return "Reprovado"
