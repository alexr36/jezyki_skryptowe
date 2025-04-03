import sys, subprocess, json
from collections import Counter



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
    #TODO: ogarnij to 
    results = run_analyzis()

    total_chars = 0
    total_words = 0
    total_lines = 0
    char_counter = Counter()
    word_counter = Counter()

    for file, result in results.items():
        print(f"STATS FOR FILE '{file}':")
        print(result.stdout)

        try:
            stats = json.loads(result.stdout)
            total_chars += stats['chars_count']
            total_words += stats['words_count']
            total_lines += stats['lines_count']
            char_counter[stats['most_common_char']] += 1
            word_counter[stats['most_common_word']] += 1
        except Exception:
            print(f"[WARNING] Could not parse stats for file '{file}")

    print("\nGLOBAL SUMMARY:")
    print(f"\nRead files: {len(results.items())}")
    print(f"Total characters: {total_chars}")
    print(f"Total words: {total_words}")
    print(f"Total lines: {total_lines}")

    most_common_char = char_counter.most_common(1)[0][0] if char_counter else 'N/A'
    print(f"Most common character: {most_common_char}")

    most_common_word = word_counter.most_common(1)[0][0] if word_counter else 'N/A'
    print(f"Most common word: {most_common_word}")



if __name__ == '__main__':
   show_results()
