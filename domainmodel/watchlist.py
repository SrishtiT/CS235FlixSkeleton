from typing import List
from domainmodel.movie import Movie

class WatchList:
    def __init__(self):
        self._watch_list: List[Movie] = list()

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self._watch_list):
            movie = self._watch_list[self.i]
            self.i += 1
            return movie
        else:
            raise StopIteration

    @property
    def watchlist(self):
        return self._watch_list

    def add_movie(self, movie: Movie):
        if movie not in self._watch_list:
            self._watch_list.append(movie)

    def remove_movie(self, movie: Movie):
        if movie in self._watch_list:
            self._watch_list.remove(movie)

    def select_movie_to_watch(self, index):
        if index >= len(self._watch_list) or index < 0:
            return None
        return self._watch_list[index]

    def size(self):
        return len(self._watch_list)

    def first_movie_in_watchlist(self):
        if self.size() == 0:
            return None
        return self._watch_list[0]
