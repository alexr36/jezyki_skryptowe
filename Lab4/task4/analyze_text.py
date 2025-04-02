import sys, subprocess, os



def read_args():
    if len(sys.argv) < 2:
        sys.stderr.write(f"[ERROR] Please provide an argument")
        exit(1)
        
    return sys.argv[1:]



def compile_analyzer():
    compile = subprocess.run([
        'g++', 
        '-std=c++20', 
        'text_analyzer.cpp', 
        '-o', 
        'text_analyzer.exe'
    ])

    if compile.returncode != 0:
        sys.stderr.write("[ERROR] Compilation failed")
        sys.exit(1)



def analyze(filepath):
    return subprocess.run(
        f"echo {filepath} | ./text_analyzer.exe", 
        shell=True, text=True, capture_output=True
    )



def run_analyzis():
    compile_analyzer()
    analyzed_text_files = {}

    for arg in read_args():
        analyzed_text_files[arg] = analyze(arg)

    return analyzed_text_files    



def show_results():
    for file, result in run_analyzis().items():
        print(f"STATS FOR FILE '{file}':")
        print(result.stdout)



if __name__ == '__main__':
   show_results()
