# Code for [A framework for quantum circuit optimization: comparators as a case study](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=92)

**Francisco Orts and Rodrigo Gil-Merino**

This repository contains all the written code for the paper "A framework for quantum circuit optimization: comparators as a case study", written by Francisco Orts and Rodrigo Gil-Merino. It allows simplifying quantum arithmetic circuits and, in general, any quantum circuit that computes an operation between two bit strings $A$ and $B$ whose operation is based on Boolean algebra.

The code is written in Python. These libraries are necessary:
* qiskit
* collections 

**Files included:**
* [OptimizeConcatenatedCNOT.py](https://github.com/2forts/QuantumMeter/blob/main/OptimizeConcatenatedCNOT.py): Replaces, as specified in the paper, controlled operations that can be simplified.
* [QuantumCostAnalyzer.py](https://github.com/2forts/QuantumMeter/blob/main/QuantumCostAnalyzer.py): Quantum circuit metric calculator.
* [RemoveCNOT.py](https://github.com/2forts/QuantumMeter/blob/main/RemoveCNOT.py): Replaces CNOT operations with unit operations.
* [RemoveUnusedQubits.py](https://github.com/2forts/QuantumMeter/blob/main/RemoveUnusedQubits.py): Eliminates all unused qubits from a circuit, obtaining an equivalent and ordered one.
* [Example.py](https://github.com/2forts/QuantumMeter/blob/main/Example.py): Example of how to use the framework operations.
* [comparator.qasm](https://github.com/2forts/QuantumMeter/blob/main/comparator.qasm): Comparator obtained using the framework, as described in the paper.
* [LiCENSE](https://github.com/2forts/QuantumMeter/blob/main/LICENSE): Apache License 2.0.

**How to cite:**

IMPORTANT: This work is currently under review.

If you are going to use all or part of this code in your own work, please quote it as follows

F. Orts & R. Gil-Merino. (2024). A framework for quantum circuit optimization: comparators as a case study. IEEE transactions on very large scale integration (vlsi) systems.

BibTex:
```{bibtex}
@article{orts2024,
  title={A framework for quantum circuit optimization: comparators as a case study},
  author={Orts, F and Gil-Merino, R},
  journal={IEEE transactions on very large scale integration (vlsi) systems},
  volume={?},
  number={?},
  pages={?},
  year={2024},
  publisher={IEEE}
}
```
