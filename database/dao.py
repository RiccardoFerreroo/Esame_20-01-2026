from database.DB_connect import DBConnect
from model.artist import Artist
from model.track import Track


class DAO:

    @staticmethod
    def get_all_artists():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT *
                FROM artist a
                """
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'], num_album= 0,genre_id='')#assegno 0 a num_album e genre'' per comodità
            result.append(artist)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_artisti_filtrati(min_albums):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                select a.id, a.name, count(al.id) as num_album
                from artist a, album al
                where a.id = al.artist_id 
                group by a.id,a.name
                having COUNT(al.id)>1
                """
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'], num_album=row['num_album'], genre_id='')
            result.append(artist)
        cursor.close()
        conn.close()
        return result
    @staticmethod
    def ottieni_albums(lista_artisti):
        conn = DBConnect.get_connection()
        result = {a: set() for a in lista_artisti}
        cursor = conn.cursor(dictionary=True)
        artists_id = tuple(a.id for a in lista_artisti)
        query = f"""select a.id as album_id
                    from album a 
                    where a.artist_id IN {artists_id}
            
                """
        cursor.execute(query)
        for row in cursor:
            artists_id = next((a for a in lista_artisti if a.id == row['album_id']), None)
            if artists_id:
                result[artists_id].add(row['album_id'])
        cursor.close()
        conn.close()
        return result
    @staticmethod
    def get_track(lista_artisti):
        conn = DBConnect.get_connection()
        result = {}
        cursor = conn.cursor(dictionary=True)
        query = """
                 SELECT album_id , genre_id
                FROM track
                group by album_id , genre_id 
                """
        cursor.execute(query)
        for row in cursor:
            track = Track(id=row['album_id'], genre_id=row['genre_id'])
            result[track.id].add(row['genre_id'])

        cursor.close()

        conn.close()
        return result











    #def ottieni_artisti(artist_filtrati):
    #    conn = DBConnect.get_connection()
    #    result = []
    #    lista_a_query = []
    #    for i, artist_1 in enumerate(artist_filtrati):
    #        for artist_2 in artist_filtrati[i + 1:]:
    #            lista_a_query.append((artist_1,artist_2))
    #    for a1, a2 in lista_a_query:
    #        artists_ids = tuple(a1,a2 )
#
    #        cursor = conn.cursor(dictionary=True)
    #        query = """select least(a1.artist_id) as artista_1, greatest(a2.artist_id)as artista_2, count(t1.genre_id)as somma
    #                    from track t1, track t2, album a1, album a2
    #                    where a1.artist_id = a2.artist_id and t1.genre_id  = t2.genre_id and (a1.artist_id, a2.artist_id)in  {artists_id}
    #                    group by somma
    #             """
    #        cursor.execute(query,())
    #        for row in cursor:
    #            artist = Artist(id=row['id'], name=row['name'], num_album=row['num_album'], genre_id='')
    #            result.append(artist)
    #        cursor.close()
    #    conn.close()
    #    return result
#