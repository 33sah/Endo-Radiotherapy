import subprocess

def main():
  for i in range(1, 4):
    # Run run.mac with exe
    commandproton = f"cancer.exe -m cancer{i}proton.mac -t 100 -p 2"        
    commandalpha = f"cancer.exe -m cancer{i}.mac -t 100 -p 2"

    mergerootsalpha= f"hadd -O -f cancer{i}.root molecular-dna_t*.root"
    mergerootsproton= f"hadd -O -f cancer{i}proton.root molecular-dna_t*.root"

    cleardata = f"del molecular-dna_t*.root"

    subprocess.run(commandalpha, shell=True)
    subprocess.run(mergerootsalpha, shell=True)
    subprocess.run(cleardata, shell=True)
    subprocess.run(commandproton, shell=True)
    subprocess.run(mergerootsproton, shell=True)
    subprocess.run(cleardata, shell=True)
    # Run command

if __name__ == "__main__":
  main()

