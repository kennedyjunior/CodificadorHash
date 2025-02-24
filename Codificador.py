
import hashlib

def Codificador():
    print("Para codificar, escolha entre 1, 2 e 3")
    print("1 para MD5, 2 para SHA1, 3 para SHA256")
    
    options = input("Escolha uma opção (1, 2 ou 3): ")
    if options not in ["1", "2", "3"]:
        print("Opção inválida!")
        return # Finaliza a função 1
    
    msg = input("Digite sua mensagem: ")
    
    # escolher o tipo de hash 1, 2 e 3
    if options == "1":
        hash = hashlib.md5()
    elif options == "2":
        hash = hashlib.sha1()
    elif options == "3":
        hash = hashlib.sha256()
    
    hash.update(msg.encode('utf-8'))  # Atualiza o hash com a mensagem digitada
    print(f"Aqui está sua mensagem codificada: {hash.hexdigest()}")  # Exibe o hash gerado

if __name__ == "__main__":  
    Codificador()