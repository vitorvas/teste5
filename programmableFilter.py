# Filtro para pegar os valores absolutos entre dois conjuntos de Q
# Funciona carregando testeA e testeB
# QW é a variável.
# Pode ser Q. Neste caso é usada a Calculator para criar Q/volume
# Com isso temos o Q em Watts
# O valor absoluto permite exibir as diferenças entre Q's

import vtk
import vtk.numpy_interface.dataset_adapter as dsa
import vtk.numpy_interface.algorithms as algs
Q1=inputs[0].CellData['QW']
Q2=inputs[1].CellData['QW']
K=algs.abs(Q1-Q2)
output.CellData.append(K,'QWdiff')
#T1=inputs[0].CellData['T']
#T2=inputs[1].CellData['T']
#output.CellData.append(T2-T1,'Tdiff')
