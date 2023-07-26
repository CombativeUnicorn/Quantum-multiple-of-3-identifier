from qiskit import QuantumCircuit
from qiskit import Aer, transpile
from qiskit.visualization import plot_histogram


qc = QuantumCircuit(6, 3)


# here you have to initialize a superposition of states, in this case it is a superposition of all numbers from 0 to 7
# please note tath this code will not work with some initial superpositions, specificly those where exactly half the numbers are multiples of 3
qc.h([0, 1, 2])


qc.x(3)
qc.cx(0, 1)
qc.x(1)
qc.cx(2, 1)
qc.ccx(0, 2, 3)
qc.cz(1, 3)
qc.ccx(0, 2, 3)
qc.cx(2, 1)
qc.x(1)
qc.cx(0, 1)


# here you have to apply the tranformation from the initial superposition to the state of |1>
qc.h([0, 1, 2])
qc.x([0, 1, 2])


qc.h(2)
qc.ccx(0, 1, 2)
qc.h(2)


# here you have to apply the tranformation from the state of |1> to the initial superposition 
qc.x([0, 1, 2])
qc.h([0, 1, 2])


qc.measure(0, 0)
qc.measure(1, 1)
qc.measure(2, 2)


sim = Aer.get_backend('aer_simulator')
t_qc = transpile(qc, sim)
counts = sim.run(t_qc).result().get_counts()


plot_histogram(counts)
