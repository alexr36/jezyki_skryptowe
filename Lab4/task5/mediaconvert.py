import os, subprocess, datetime, utils as ut



def convert_file(input_path, target_format, output_dir):
    output_filename = ut.add_ts_and_ext(input_path, target_format)
    output_path = os.path.join(output_dir, output_filename)

    if ut.is_video_or_audio(input_path):
        tool = 'ffmpeg'
        cmd_input = [tool, '-y', '-i', input_path, output_path]
    elif ut.is_image(input_path):
        tool = 'magick'
        cmd_input = [tool, input_path, output_path]
    else:
        print(f"[INFO] Unsupported file type: {input_path}. Skipping...")
        return
    
    print(f"[INFO] Converting {input_path} to {output_filename}...")
    result = subprocess.run(cmd_input, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"[ERROR] Conversion failed: {input_path}")
        print(result.stderr)
        return

    ut.log_history(
        os.path.join(output_dir, 'history.json'),
        {
            'datetime': datetime.datetime.now().isoformat(),
            'input_file': input_path,
            'output_file': output_path,
            'format': target_format,
            'tool': tool 
        }
    )


def main():
    args = ut.read_args()
    input_dir = args[0]
    target_format = args[1]
    output_dir = ut.get_output_dir()
    ut.ensure_dir(output_dir)
    
    for root, _, files in os.walk(input_dir):
        for file in files:
            path = os.path.join(root, file)
            convert_file(path, target_format, output_dir)

    print(f"Converted files saved to {output_dir}")



if __name__ == '__main__':
    main()
