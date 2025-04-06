# from qiskit import QuantumCircuit, Aer, transpile
# from qiskit.providers.aer import AerSimulator
#
# # 간단한 테스트 회로 생성
# qc = QuantumCircuit(2)
# qc.h(0)
# qc.cx(0, 1)
# qc.measure_all()
#
# # AerSimulator에서 시뮬레이션 실행
# simulator = AerSimulator()
# compiled_circuit = transpile(qc, simulator)
# result = simulator.run(compiled_circuit).result()
# print(result.get_counts())

# 간단한 Qiskit 상태 벡터 시각화 코드
from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# 1. 양자 회로 생성
qc = QuantumCircuit(1)  # 1 큐비트 생성
qc.h(0)  # 아다마르 게이트를 적용하여 중첩 상태 생성
qc.draw('mpl')  # 회로 시각화

# 2. 상태 벡터 계산
state = Statevector.from_instruction(qc)  # 회로에서 상태 벡터 계산

# 3. 상태 시각화 (블로흐 구면)
fig = plot_bloch_multivector(state)  # 블로흐 구에 상태 벡터 표시
plt.show()
