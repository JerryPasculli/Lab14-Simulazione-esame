class Arco:
    def __init__(self, primo, secondo, peso):
        self._primo = primo
        self._secondo = secondo
        self._peso = peso

    def __lt__(self, other):
        return self._peso < other._peso
    def __hash__(self):
        stringhetta = str(self._primo) + "_" + str(self._secondo)
        return hash(stringhetta)
    def __eq__(self, other):
        if other is None:
            return False
        stringhetta1 = str(self._primo) + "_" + str(self._secondo)
        stringhetta2 = str(other._primo) + "_" + str(other._secondo)
        return stringhetta1 == stringhetta2