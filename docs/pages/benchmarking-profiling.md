---
title: Benchmarking and profiling
layout: default
---

# Benchmarking

| Name                                         | Short description                                                                                                                                                                                                                                                                                                                                                                         | 🚦  |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: |
| [asv](https://asv.readthedocs.io/en/stable/) | A tool for benchmarking Python packages over their lifetime. Allows you to write benchmarks and then run them against every commit in the repository, to identify where performance increased or decreased. Comparative benchmarks can also be run, which can be useful for [running them in CI using GitHub runners](https://labs.quansight.org/blog/2021/08/github-actions-benchmarks). | 🟢  |

# Profiling

## Time

| Name                                                          | Short description                                                                                                                              | 🚦  |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | :-: |
| [pyinstrument](https://pyinstrument.readthedocs.io/en/stable) | Python profiler. Tells you how long individual lines of code take to run, so you can focus on the slowest part of your program to speed it up. | 🟢  |
| [line_profiler](https://pypi.org/project/line-profiler/)      | A tool for line-by-line profiling of functions.                                                                                                | 🟠  |

## Memory

| Name                                                         | Short description                                                                                                                                                                                                                           | 🚦  |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: |
| [memray](https://bloomberg.github.io/memray/)                | Tracks and reports memory allocations, both in Python code and in compiled extension modules. It also has a [plugin](https://pytest-memray.readthedocs.io/en/latest/) for easy integration with pytest. Only works on Linux and macOS.      | 🟠  |
| [memory_profiler](https://pypi.org/project/memory-profiler/) | No longer actively maintained. A Python module for monitoring memory consumption of a process alongside line-by-line analysis of memory consumption. Might be a useful alternative to memray if you need to do memory profiling on Windows. | 🟠  |

## General/other tools

| Name                                               | Short description                                                                                 | 🚦  |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------- | :-: |
| [psutil](https://psutil.readthedocs.io/en/latest/) | System monitoring, profiling, limiting process resources and the management of running processes. | 🟢  |
| [snakeviz](https://jiffyclub.github.io/snakeviz/)  | Browser based graphical viewer for the output of Python’s cProfile module.                        | 🟢  |
