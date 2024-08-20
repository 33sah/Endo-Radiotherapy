import subprocess

def main():
  for i in range(1, 4):
    # Run run.mac with exe
    commandproton = f"cancer.exe -m cancer{i}proton.mac -t 500 -p 2"        
    commandalpha = f"cancer.exe -m cancer{i}.mac -t 500 -p 2"

    subprocess.run(commandalpha, shell=True)
    subprocess.run(commandproton, shell=True)
    # Run command

if __name__ == "__main__":
  main()

