from django.db import models
from decimal import Decimal

class Currency(models.Model):
    """Modelo para almacenar las monedas disponibles como USD, USDT, BTC, etc."""
    symbol = models.CharField(max_length=10)  # Símbolo de la moneda, como 'USD', 'USDT', 'BTC'
    name = models.CharField(max_length=50)    # Nombre de la moneda (Ej. 'Dólar', 'Tether')

    def __str__(self):
        return self.symbol

class Wallet(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)  # Relación con la moneda (USD, USDT)
    balance = models.DecimalField(max_digits=20, decimal_places=8, default=Decimal('0.0'))  # Saldo de la moneda

    def __str__(self):
        return f"Wallet - {self.currency.symbol}: {self.balance} {self.currency.symbol}"

class Transaction(models.Model):
    """Modelo opcional para almacenar las transacciones realizadas (depósitos, conversiones)."""
    
    TRANSACTION_TYPES = (
        ('DEPOSIT', 'Depósito'),
        ('WITHDRAWAL', 'Retiro'),
        ('CONVERSION', 'Conversión'),
    )

    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)  # Tipo de transacción (Depósito, Retiro, Conversión)
    amount = models.DecimalField(max_digits=20, decimal_places=8)  # Monto de la transacción
    total_value = models.DecimalField(max_digits=20, decimal_places=8)  # Valor total de la transacción en la moneda de destino (USDT)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)  # Moneda asociada con la transacción
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)  # Billetera asociada con la transacción
    date = models.DateTimeField(auto_now_add=True)  # Fecha de la transacción

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} {self.currency.symbol} on {self.date}"
