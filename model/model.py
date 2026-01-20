import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self.load_all_artists()
        self.lista_artisti_filtrati= []
        self.dict_artisti_album = {}

    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        print(f"Artisti: {self._artists_list}")

    def load_artists_with_min_albums(self, min_albums):
        self.lista_artisti_filtrati = DAO.get_artisti_filtrati(min_albums)
        #print(self.lista_artisti_filtrati[0].name) # per verificare correttezza con database



    def build_graph(self):
        self.dict_artisti_album =DAO.ottieni_albums(self.lista_artisti_filtrati) #mappa artisti ad album corrispondente
        #print(self.dict_artisti_album)
        self._tracks = DAO.get_track(self.lista_artisti_filtrati)#otteniamo diionario oggetti tracks che usiamo per collegare genre e artists
                                                        #per poi costruire il graph



