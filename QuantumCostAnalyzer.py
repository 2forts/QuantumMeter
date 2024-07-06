from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library.standard_gates import *

# Class for calculating the quantum cost and delay of a circuit 
class QuantumCostAnalyzer:
    # Constructor, accepts quantum cost and custom delay for any gate.
    # It is not necessary to specify cost and delay for one or two-cubit gates, 
    # the default being 1 by default (but can also be customised).
    def __init__(self, custom_costs=None, custom_delays=None):
        self.custom_costs = custom_costs if custom_costs else {}
        self.custom_delays = custom_delays if custom_delays else {}

    # By default, the circuit is not transpiled. If transpiling is desired, this 
    # must be indicated by means of the "transpile" attribute. In this case, it 
    # is also necessary to indicate the base gates for this transpilation.
    def load_circuit_from_qasm(self, qasm_str, transpile=False, 
                               transpiled_basis_gates=['u1', 'u2', 'u3', 'cx']):
        self.circuit = QuantumCircuit.from_qasm_str(qasm_str)

        if (transpile==True): 
          self.circuit = transpile(self.circuit, 
                                   basis_gates=transpiled_basis_gates)

    def get_cost_and_delay(self):
        cost = 0
        delay = 0
        depth_layers = {}

        for gate in self.circuit.data: 
            name = gate[0].name
            qubits = gate[1]
            num_qubits = len(qubits)

            # Calculate cost (measurement counts as a cost gate 1)
            if num_qubits <= 2:
                cost += 1
            else:
                cost += self.custom_costs.get(name, 0)

            # Calculate delay
            layer = max(depth_layers.get(qubit._index, 0) for qubit in qubits)
            layer += 1
            delay_layer = 1 if num_qubits <= 2 else self.custom_delays.get(name, 
                                                                           0)
            delay = max(delay, layer + delay_layer - 1)
            for qubit in qubits:
                depth_layers[qubit._index] = layer

        return cost, delay
