from dataclasses import dataclass

@dataclass
class Track:
    id : int
    genre_id : int



    def __str__(self):
        return f"{self.id}, {self.genre_id}"
    def __repr__(self):
        return f"{self.id}, {self.genre_id}"

    def __hash__(self):
        return hash(self.id)