# SUI Wallet Generator (Python)

Простой и полностью рабочий генератор SUI-кошельков (Ed25519 + правильный bech32 адрес Sui)

## Установка и запуск 

```bash
# 1. Клонируем репозиторий
git clone https://github.com/hudsoonme/sui-wallet-generator.git
cd sui-wallet-generator

# 2. Создаём виртуальное окружение (рекомендуется)
python -m venv venv
source venv/bin/activate    # Linux / macOS
# или
venv\Scripts\activate       # Windows

# 3. Устанавливаем зависимости
pip install ed25519 bech32

# 4. Запускаем генератор (создаст 10 кошельков)
python sui_generator.py

## Пример вывода


Кошелёк 1
Адрес:         sui1qrp4w7gq34k3g3j7l5v9mzf5q2v8n0x3v5zq2v8n0x3v5zq2v8n0x3v
Приватный ключ: 3f4a9b8c2d1e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a
Публичный ключ: 8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b
--------------------------------------------------------------------
