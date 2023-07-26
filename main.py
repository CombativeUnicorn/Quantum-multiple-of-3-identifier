#!/usr/bin/env python
# coding: utf-8

# In[20]:


from qiskit import QuantumCircuit


# In[21]:


qc = QuantumCircuit(6, 3)
qc.h([0, 1, 2])


# In[22]:


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
qc.h([0, 1, 2])
qc.x([0, 1, 2])
qc.h(2)
qc.ccx(0, 1, 2)
qc.h(2)
qc.x([0, 1, 2])
qc.h([0, 1, 2])


# In[23]:


qc.measure(0, 0)
qc.measure(1, 1)
qc.measure(2, 2)


# In[24]:


from qiskit import Aer, transpile
sim = Aer.get_backend('aer_simulator')
t_qc = transpile(qc, sim)
counts = sim.run(t_qc).result().get_counts()

from qiskit.visualization import plot_histogram
plot_histogram(counts)


# In[ ]:




