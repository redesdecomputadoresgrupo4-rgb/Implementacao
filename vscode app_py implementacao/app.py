# program.py
import sys
from recon.passive_recon import passive_recon
from web.check_security_headers import check_security_headers
from sast.run_bandit import run_bandit
from scanning.run_nmap import run_nmap_wrapper

def menu():
    print("=== Security Tests Orchestrator (lab only) ===")
    print("1) Recon passivo (headers, robots.txt)")
    print("2) Checar headers de segurança (HTTP)")
    print("3) Rodar Bandit (SAST) em um diretório, ex: http://localhost:3000")
    print("4) Rodar nmap (wrapper) (colocar .) - requer nmap instalado")
    print("0) Sair")
    choice = input("Escolha: ").strip()
    return choice

def main():
    while True:
        c = menu()
        if c == "1":
            target = input("URL alvo (ex: http://10.0.2.15:8080): ").strip()
            passive_recon(target)
        elif c == "2":
            target = input("URL alvo (ex: http://10.0.2.15:8080): ").strip()
            check_security_headers(target)
        elif c == "3":
            path = input("Caminho para código Python a analisar: ").strip()
            run_bandit(path)
        elif c == "4":
            target = input("IP ou host para nmap: ").strip()
            run_nmap_wrapper(target)
        elif c == "0":
            print("Saindo.")
            sys.exit(0)
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
