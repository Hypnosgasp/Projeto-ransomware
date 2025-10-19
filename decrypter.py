import os
import pyaes

def decrypt_file(encrypted_file_path, decrypted_file_path, key):
    """
    Descriptografa um arquivo usando AES no modo CTR.
    
    Args:
        encrypted_file_path (str): Caminho para o arquivo criptografado.
        decrypted_file_path (str): Caminho para salvar o arquivo descriptografado.
        key (bytes): Chave de descriptografia (deve ter 16, 24 ou 32 bytes para AES).
    
    Raises:
        FileNotFoundError: Se o arquivo criptografado não existir.
        ValueError: Se a chave for inválida.
        Exception: Para outros erros durante a descriptografia.
    """
    # Verificar se o arquivo criptografado existe
    if not os.path.exists(encrypted_file_path):
        raise FileNotFoundError(f"Arquivo criptografado não encontrado: {encrypted_file_path}")
    
    # Verificar se a chave tem o tamanho correto (AES suporta 128, 192 ou 256 bits)
    if len(key) not in [16, 24, 32]:
        raise ValueError("A chave deve ter 16, 24 ou 32 bytes.")
    
    try:
        # Abrir e ler o arquivo criptografado
        with open(encrypted_file_path, "rb") as file:
            file_data = file.read()
        
        # Configurar AES no modo CTR e descriptografar
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)
        
        # Criar o arquivo descriptografado
        with open(decrypted_file_path, "wb") as new_file:
            new_file.write(decrypt_data)
        
        # Remover o arquivo criptografado apenas após sucesso
        os.remove(encrypted_file_path)
        print(f"Arquivo descriptografado com sucesso: {decrypted_file_path}")
    
    except Exception as e:
        print(f"Erro durante a descriptografia: {e}")
        raise

# Exemplo de uso (pode ser adaptado para argumentos de linha de comando ou inputs)
if __name__ == "__main__":
    encrypted_file = "teste.txt.ransomwaretroll"
    decrypted_file = "teste.txt"
    key = b"testeransomwares"  # A chave deve ser a mesma usada na criptografia
    
    decrypt_file(encrypted_file, decrypted_file, key)
