from qiskit import QuantumCircuit

def get_qubit_states(circuit):
    # Utilizar el simulador de estado vectorial para obtener los estados de los cúbits
    circuit.remove_final_measurements()  # no measurements allowed
    from qiskit.quantum_info import Statevector
    statevector = Statevector(circuit)
    
    # Determinar el estado de cada cúbit
    qubit_states = {}
    for i in range(circuit.num_qubits):
        # Calculamos la probabilidad de que el cúbit esté en el estado |1>
        prob_one = sum(abs(statevector[j])**2 for j in range(len(statevector)) if (j >> i) & 1)
        qubit_states[i] = 1 if prob_one > 0.5 else 0

    return qubit_states

def process_cnot_in_circuit(qasm_code, initial_states):
    # Crear el circuito cuántico a partir del código QASM
    circuit = QuantumCircuit.from_qasm_str(qasm_code)

    # Crear un registro para las operaciones realizadas en cada cúbit
    qubit_operations = {qubit: False for qubit in range(circuit.num_qubits)}

    # Nuevo circuito donde añadiremos las puertas transformadas
    new_circuit = QuantumCircuit(circuit.num_qubits, circuit.num_clbits)
    
    for instr, qargs, cargs in circuit.data:
        controlled = False
        target_qubit = 0
        if instr.name == "cx":
            control_qubit = qargs[0]._index
            target_qubit = qargs[1]._index

            # Obtener el estado actual de los cúbits antes de la puerta CNOT
            qubit_states = get_qubit_states(new_circuit)

            # Si no se ha hecho operación alguna en el cúbit de control
            if not qubit_operations[control_qubit]:
                controlled = True
                control_state = qubit_states[control_qubit]

                if control_state == 1:
                    new_circuit.x(target_qubit)
                else:
                    new_circuit.id(target_qubit)
            else:
                new_circuit.cx(control_qubit, target_qubit)
        else:
            new_circuit.append(instr, qargs, cargs)

        # Registrar que se ha hecho una operación en los cúbits correspondientes
        # pero solo si no es una de las simplificaciones
        if (controlled==False):
          for qubit in qargs:
            qubit_operations[qubit._index] = True

    return new_circuit

# Código QASM de ejemplo
qasm_code = """
OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
creg c[2];
cx q[0],q[1];
cx q[0],q[1];
cx q[0],q[1];
x q[0];
cx q[0],q[1];
cx q[0],q[1];
"""

# Estados iniciales de los cúbits (indexado por el número del cúbit)
initial_states = {
    0: 1,  # El cúbit 0 está en estado |0>
    1: 0   # El cúbit 1 está en estado |0>
}

# Procesar el circuito
new_circuit = process_cnot_in_circuit(qasm_code, initial_states)
print(new_circuit)
