# Projeto-ransomware

🔐 Criptografador & Decrypter em Python

Esses dois scripts formam um par poderoso e educativo 💡 que demonstra como criptografar e descriptografar arquivos usando o algoritmo AES (modo CTR) de forma prática e segura.

🚀 O que cada script faz:

🧱 criptografador.py → Lê um arquivo comum, aplica criptografia AES e gera uma versão protegida com extensão personalizada (.ransomwaretroll).

🔓 decrypter.py → Faz o caminho inverso: usa a mesma chave para recuperar o conteúdo original do arquivo criptografado.

⚙️ Como funciona:

O usuário define uma chave secreta (com 16, 24 ou 32 bytes 🔑).

O script lê o conteúdo do arquivo original (ou criptografado).

Utiliza a biblioteca PyAES para executar a criptografia/descriptografia.

Salva o novo arquivo e remove o anterior com segurança.

🧠 Exemplo rápido:
# Criptografar
python criptografador.py

# Descriptografar
python decrypter.py

🛡️ Importante:

Esses scripts são educacionais, criados para estudos sobre segurança e criptografia.
⚠️ Não devem ser usados para fins maliciosos!
