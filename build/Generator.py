import subprocess
import itertools

# Indexing Magic
def seq(start, end, step):
    if step == 0:
        raise ValueError("step must not be 0")
    sample_count = int(abs(end - start) / step)
    return itertools.islice(itertools.count(start, step), sample_count)

# Changing run.mac file for correct shape / energy
def texteditor(file, Energy, linenumbers):
    if all(type(x) in [int] for x in linenumbers):
    # Checking if integers passed in argument

        with open("file", "r") as file:
            text = file.read()
    
        lines = text.split("\n")
        lines[linenumbers[0]] = f"/gps/energy {Energy} MeV"
        FileEnergy = str(Energy).replace(".","_")
        lines[linenumbers[1]] = f"/analysisDNA/fileName cancer{FileEnergy}.root"
        final_text = "\n".join(lines)
    
        with open("file", "w") as file:
            file.write(final_text)

def main():
  # Run run.mac with gears
  file = "cancer1.mac"
  command = f"cancer.exe -m {file} -t 2 -p 2"

  # Line Numbers to change - Geometry, Energy Range + Distribution and Data - Remember these will be 1 smaller than actuality due to Python list starting at index = 0
  Numbers = [53, 61]
  
  for x in seq(5.0,9.1,0.1):
        # Python rounding error
        texteditor(file, round(x,2), Numbers)
        subprocess.run(command, shell=True)
        # Run command

if __name__ == "__main__":
  main()
