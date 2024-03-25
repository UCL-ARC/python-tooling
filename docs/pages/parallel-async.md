---
title: Parallel and asynchronous processing
layout: default
---

# Parallel and asynchronous processing

Python has a good ecosystem of libraries for multiprocessing (threads and GPU
parallelisation), as well as asynchronous processing.

🟠 tools in the following may be preferred over 🟢, if there are external
reasons to use a specific interface or parallelisation scheme. Possibly due to
the nature of the research problem, the high-performance computing resources
available or simply due to pre-existing code using a library like [pandas].

## Thread- and process-based parallelism

| Name              | Short description                                                                                                                                                                                            | 🚦  |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-: |
| [multiprocess]    | A fork of [multiprocessing] which uses `dill` instead of `pickle` to allow serializing wider range of object types including nested / anonymous functions. We've found this rather more simple to work with. | 🟢  |
| [dask]            | Aims to make scaling existing code in familiar libraries (`numpy`, [pandas], `scikit-learn`, ...) easy.                                                                                                      | 🟠  |
| [multiprocessing] | The standard library module for distributing tasks across multiple processes                                                                                                                                 | 🟠  |
| [mpi4py]          | support for MPI based parallelism                                                                                                                                                                            | 🟠  |

## Compiler-based parallelism

| Name     | Short description                                                                                                                                                       | 🚦  |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: |
| [Cython] | Has [support for OpenMP based parallelism](https://cython.readthedocs.io/en/latest/src/userguide/parallelism.html)                                                      | 🟠  |
| [numba]  | [Support for parallelism via `jit(parallel=True)`](https://numba.pydata.org/numba-doc/latest/user/parallel.html).                                                       | 🟠  |
| [jax]    | [Support for parallelising NumPy / scientific computing like operations using functional transforms](https://jax.readthedocs.io/en/latest/jax-101/06-parallelism.html). | 🟠  |

<!-- URLs for more a readable table and text above 👆 -->

[multiprocess]: https://multiprocess.readthedocs.io/en/latest/
[multiprocessing]: https://docs.python.org/3/library/multiprocessing.html
[Cython]: https://cython.readthedocs.io/
[mpi4py]: https://mpi4py.readthedocs.io/
[pandas]: https://pandas.pydata.org/
[dask]: https://docs.dask.org/
[numba]: https://numba.pydata.org/
[jax]: https://jax.readthedocs.io/
