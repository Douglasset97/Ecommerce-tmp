# arquivo: classificador.py

def validar_voucher(valor: float) -> bool:
    """
    Verifica se um valor de compra é elegível para um voucher.
    Válido para valores entre 50.00 e 500.00 (inclusive).
    """
    return 50.00 <= valor <= 500.00

def classificar_nota(valor: float) -> str:
    """
    Classifica um valor numérico entre 0 e 500.
    Usa a função validar_voucher para verificar elegibilidade.
    """
    if valor < 0 or valor > 500:
        return "Nota inválida"

    if validar_voucher(valor):
        return "Aprovado"
    else:
        return "Reprovado"
