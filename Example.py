# Custom costs and delays for gates that operate on more than 2 qubits
custom_costs = {'ccx': 5, 'cswap': 3}
custom_delays = {'ccx': 5, 'cswap': 3}

# Example QASM string
qasm_str = """
OPENQASM 2.0;
include "qelib1.inc";
qreg q[3];
creg c[3];
h q[0];
cx q[0], q[1];
ccx q[0], q[1], q[2];
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
"""

analyzer = QuantumCostAnalyzer(custom_costs, custom_delays)
analyzer.load_circuit_from_qasm(qasm_str)
cost, delay, num_qubits = analyzer.get_cost_and_delay()
gate_counts = analyzer.get_gate_counts()

print(f"Quantum cost: {cost}")
print(f"Delay: {delay}")
print(f"Number of qubits: {num_qubits}")
print("Quantum gate counter:", gate_counts)
