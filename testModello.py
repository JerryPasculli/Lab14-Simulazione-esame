from model.model import Model

self_model = Model()
output = self_model.creaGrafo()
print(output)
output1 = self_model.soglia(3)
print(output1)
output2 = self_model.cammino(3)
print(output2)
