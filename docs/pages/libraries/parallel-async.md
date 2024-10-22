---
title: Parallel and asynchronous processing
layout: default
parent: Recommended libraries
---

## Parallel and asynchronous processing

Python has a good ecosystem of libraries for parallelising the processing of
tasks, as well as asynchronous processing.

Parallelisation in Python is typically _process-based_ with code parallelised
across multiple Python processes each with their own interpreter or makes use of
tools which run the tasks to be parallelised outside of the Python interpreter,
using for example Python wrappers around external code which uses thread-based
parallelism.

🟠 tools in the following should be chosen, if there are external reasons to use
a specific interface or parallelisation scheme. Possibly due to the nature of
the research problem, the high-performance computing resources available or
simply due to pre-existing code using a library like [pandas].

### Process-based (and thread-based) parallelism

| Name                 | Short description                                                                                                                                                                                                 | 🚦  |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: |
| [multiprocess]       | A fork of [multiprocessing] which uses `dill` instead of `pickle` to allow serializing wider range of object types including nested / anonymous functions. We've found this easier to use than `multiprocessing`. | 🟢  |
| [concurrent.futures] | [See the table below](#asynchronous-processing).                                                                                                                                                                  | 🟠  |
| [dask]               | Aims to make scaling existing code in familiar libraries (`numpy`, [pandas], `scikit-learn`, ...) easy.                                                                                                           | 🟠  |
| [multiprocessing]    | The standard library module for distributing tasks across multiple processes.                                                                                                                                     | 🟠  |
| [mpi4py]             | Support for MPI based parallelism.                                                                                                                                                                                | 🟠  |
| [threading]          | The standard library module for multi-threading. Due to the _global interpreter lock_ [currently][PEP703] only one thread can execute Python code at a time.                                                      | 🔴  |

### Compiler-based parallelism

| Name     | Short description                                                                                                                                                       | 🚦  |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: |
| [Cython] | Has [support for OpenMP based parallelism](https://cython.readthedocs.io/en/latest/src/userguide/parallelism.html)                                                      | 🟠  |
| [numba]  | [Support for parallelism via `jit(parallel=True)`](https://numba.readthedocs.io/en/stable/user/parallel.html).                                                          | 🟠  |
| [jax]    | [Support for parallelising NumPy / scientific computing like operations using functional transforms](https://jax.readthedocs.io/en/latest/jax-101/06-parallelism.html). | 🟠  |

### Asynchronous processing

| Name                 | Short description                                                                                                                                                                                         | 🚦  |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: |
| [asyncio]            | Python standard library for asynchronous programming with tasks run in a single-threaded event loop. Used for [cooperative multitasking](https://en.wikipedia.org/wiki/Cooperative_multitasking).         | 🟠  |
| [concurrent.futures] | Another Python standard library for asynchronous processing. Provides a common interface for thread and process based concurrency as an alternative to using `multiprocess(ing)` or `threading` directly. | 🟠  |

### See also

- This [Stack Overflow post](https://stackoverflow.com/a/61360215) is a nice
  summary of what each of [threading], [multiprocessing], [asyncio] and
  [concurrent.futures] do.

<!-- URLs for more a readable tables and text above 👆 -->

[multiprocess]: https://multiprocess.readthedocs.io/en/stable/
[multiprocessing]: https://docs.python.org/3/library/multiprocessing.html
[threading]: https://docs.python.org/3/library/threading.html
[PEP703]: https://peps.python.org/pep-0703/
[Cython]: https://cython.readthedocs.io/
[mpi4py]: https://mpi4py.readthedocs.io/
[pandas]: https://pandas.pydata.org/
[dask]: https://docs.dask.org/
[numba]: https://numba.readthedocs.io/
[jax]: https://jax.readthedocs.io/
[asyncio]: https://docs.python.org/3/library/asyncio.html
[concurrent.futures]: https://docs.python.org/3/library/concurrent.futures.html
