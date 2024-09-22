import os
import pathlib
import sys

import imageio.v3 as iio
import rawpy


def convert_cr3_to_jpg(input_dir, output_dir):
    cr3_files = [f for f in os.listdir(input_dir) if f.lower().endswith(".cr3")]
    total_files = len(cr3_files)

    for index, filename in enumerate(cr3_files, start=1):
        cr3_file_path = os.path.join(input_dir, filename)
        with rawpy.imread(cr3_file_path) as raw:
            rgb = raw.postprocess()

        jpg_filename = os.path.splitext(filename)[0] + ".jpg"
        jpg_file_path = os.path.join(output_dir, jpg_filename)

        iio.imwrite(jpg_file_path, rgb)
        sys.stdout.write(f"\rConverted {filename} to {jpg_filename}.\t\t[{index}/{total_files}]")
        sys.stdout.flush()

    print("\nConversion complete.")

def main():
    script_directory = pathlib.Path(__file__).parent.resolve()
    input_directory = script_directory / "images"
    output_directory = script_directory / "output"
    print(f"Input directory: {input_directory}")
    print(f"Output directory: {output_directory}")
    os.makedirs(output_directory, exist_ok=True)
    convert_cr3_to_jpg(input_directory, output_directory)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nConversion aborted.")

