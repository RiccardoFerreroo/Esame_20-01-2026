import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):
        try:
            min_albums = int(self._view.txtNumAlbumMin.value)
            #print('num convertito')
            if min_albums<1:
                raise Exception
        except Exception:
            self._view.show_alert('inserire valore valido')
            return
        #print('numero album minimo')
        self._model.load_all_artists()
        self._model.load_artists_with_min_albums(min_albums)

        self._model.build_graph()



    def handle_connected_artists(self, e):
        pass


