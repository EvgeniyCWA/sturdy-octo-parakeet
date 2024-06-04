gas_price = 1
eth_price = 30
print(f"Стоимость газа {gas_price} gwei")
transaction_price = 22000 * gas_price / 10 ** 1
print(f"Стоимость транзакции 22000 gas * {gas_price} gwei = {transaction_price} ETH или {transaction_price * eth_price} $")
print("Для получения дропа нужно сделать 100 транзакций")
print(f"Расход для получения дропа составит {gas_price} gwei = {transaction_price * 100} ETH")
