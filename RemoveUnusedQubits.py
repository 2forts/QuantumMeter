from qiskit import QuantumCircuit

def remove_unused_qubits(qasm_code):
    # Crear el circuito cuántico a partir del código QASM
    circuit = QuantumCircuit.from_qasm_str(qasm_code)

    # Identificar los cúbits utilizados
    used_qubits = set()
    for instr, qargs, cargs in circuit.data:
        for qarg in qargs:
            used_qubits.add(qarg._index)

    # Crear un mapa de los índices originales a los nuevos índices
    qubit_index_map = {}
    new_index = 0
    for qubit in range(circuit.num_qubits):
        if qubit in used_qubits:
            qubit_index_map[qubit] = new_index
            new_index += 1

    # Crear el nuevo circuito con solo los cúbits utilizados
    new_circuit = QuantumCircuit(len(used_qubits), circuit.num_clbits)

    for instr, qargs, cargs in circuit.data:
        new_qargs = [new_circuit.qubits[qubit_index_map[qarg._index]] for qarg in qargs]
        new_circuit.append(instr, new_qargs, cargs)

    return new_circuit

# Código QASM de ejemplo
qasm_code = """
OPENQASM 2.0;
include "qelib1.inc";
qreg q[3];
creg c[3];
cx q[0],q[2];
x q[0];
measure q[0] -> c[0];
"""

# Procesar el circuito para eliminar cúbits no utilizados
new_circuit = remove_unused_qubits(qasm_code)
print(new_circuit)
