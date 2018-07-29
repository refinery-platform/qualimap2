#!/usr/bin/env python
from __future__ import print_function
import argparse
import os
from subprocess import check_call, CalledProcessError
import shutil
import sys

QUALIMAP_OUPUT_DIR = "qualimap_results"


def qualimap_bamqc(bam_filename, jv_mem_size):
    qualimap_command = [
        "qualimap", "bamqc",
        "-bam " + bam_filename,
        "-outdir " + QUALIMAP_OUPUT_DIR,
        "--java-mem-size=" + jv_mem_size
    ]

    try:
        check_call(qualimap_command)
    except CalledProcessError:
        print("Error running the qualimap bamqc", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Generate Bam Quality Statistics"
    )
    parser.add_argument('--input_file')
    parser.add_argument('--out_dir')
    parser.add_argument('--out_results')
    parser.add_argument('--out_zip')
    parser.add_argument('--java_mem_size')

    args = parser.parse_args()

    qualimap_bamqc(args.input_file, args.java_mem_size)

    shutil.make_archive(
        'raw_data_qualimapReport',
        'zip',
        os.path.join(QUALIMAP_OUPUT_DIR, 'raw_data_qualimapReport')
    )

    shutil.move("raw_data_qualimapReport.zip", args.out_zip)
    shutil.move(
        os.path.join(QUALIMAP_OUPUT_DIR, "genome_results.txt"),
        args.out_results
    )

if __name__ == "__main__":
    main()
