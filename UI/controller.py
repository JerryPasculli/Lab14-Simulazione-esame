import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        output = self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text(output))
        self._view.btn_countedges.disabled=False
        self._view.btn_search.disabled = False
        self._view.update_page()


    def handle_countedges(self, e):
        self._view.txt_result2.controls.clear()
        numero = self._view.txt_name.value
        try:
            int(numero)
        except:
            stringa = "NON HAI INSERITO UN VALORE NUMERICO COME SOGLIA"
            self._view.txt_result2.controls.append(ft.Text(stringa, color="red"))
            self._view.update_page()
            return
        output1 = self._model.soglia(int(numero))
        self._view.txt_result2.controls.append(ft.Text(output1))
        self._view.update_page()


    def handle_search(self, e):
        self._view.txt_result3.controls.clear()
        numero = self._view.txt_name.value
        try:
            int(numero)
        except:
            stringa = "NON HAI INSERITO UN VALORE NUMERICO COME SOGLIA"
            self._view.txt_result3.controls.append(ft.Text(stringa, color="red"))
            self._view.update_page()
            return
        output1 = self._model.cammino(int(numero))
        self._view.txt_result3.controls.append(ft.Text(output1))
        self._view.update_page()