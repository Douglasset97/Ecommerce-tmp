import pytest
from src.validar import validar_voucher

def test_valor_minimo():
    assert validar_voucher(50.00) is True

def test_valor_maximo():
    assert validar_voucher(500.00) is True

def test_valor_abaixo_do_minimo():
    assert validar_voucher(49.99) is False

def test_valor_acima_do_maximo():
    assert validar_voucher(500.01) is False

def test_valor_intermediario():
    assert validar_voucher(100.00) is True

def test_valor_muito_abaixo():
    assert validar_voucher(0.00) is False

def test_valor_muito_acima():
    assert validar_voucher(1000.00) is False
