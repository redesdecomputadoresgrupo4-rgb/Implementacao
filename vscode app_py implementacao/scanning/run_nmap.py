# scanning/run_nmap.py
import nmap
import json
import os

def run_nmap_wrapper(target, outdir="reports"):
    """
    Wrapper simples para nmap usando python-nmap.
    Use somente em ambiente autorizado.
    """
    os.makedirs(outdir, exist_ok=True)
    nm = nmap.PortScanner()
    # Exemplo de varredura não-agressiva: -sV (service/version) e -p- is more aggressive; modifique com cuidado.
    print(f"Rodando nmap em {target} (sV, top-1000 ports)...")
    try:
        nm.scan(targets=target, arguments='-sV --top-ports 1000')
    except Exception as e:
        print("Erro ao rodar nmap:", e)
        return
    fname = os.path.join(outdir, f"nmap_{target.replace(':','_')}.json")
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(nm.analyse_nmap_xml_scan(), f, indent=2)
    print(f"[+] Resultado salvo em {fname}")
