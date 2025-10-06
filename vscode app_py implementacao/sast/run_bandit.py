# sast/run_bandit.py
import subprocess
import os

def run_bandit(path_to_code, outdir="reports"):
    os.makedirs(outdir, exist_ok=True)
    out_file = os.path.join(outdir, "bandit_report.txt")
    print(f"Rodando Bandit em {path_to_code} ...")
    try:
        subprocess.run(["bandit", "-r", path_to_code, "-f", "txt", "-o", out_file], check=True)
        print(f"[+] Bandit finalizado. Relatório em: {out_file}")
    except subprocess.CalledProcessError as e:
        print("Erro ao rodar Bandit:", e)
