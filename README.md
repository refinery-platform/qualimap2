# qualimap2 [![Build Status](https://travis-ci.org/refinery-platform/qualimap2.svg?branch=master)](https://travis-ci.org/refinery-platform/qualimap2)
Galaxy Qualimap 2 is a platform-independent application written in Java and R that provides both a Graphical User Inteface (GUI) and a command-line interface to facilitate the quality control of alignment sequencing data and its derivatives like feature counts. 

- [Galaxy Tool Wrapper](https://toolshed.g2.bx.psu.edu/view/refinery-platform/qualimap2_bamqc)
- [Galaxy Workflow]()

### Testing with [planemo](https://planemo.readthedocs.io/en/latest/)

- `pip install -r requirements.txt`
- `planemo test --conda_auto_install --conda_auto_init --conda_ensure_channels bioconda`