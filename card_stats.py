import pickle

class CardStats:
    def __init__(self, stats_dict=None):
        if stats_dict is None:
            stats_dict = {}
        self.stats_dict = stats_dict

    @staticmethod
    def load(data):
        return CardStats(pickle.loads(data))

    def save(self):
        return pickle.dumps(self.stats_dict)

    def __eq__(self, other):
        return self.stats_dict == other.stats_dict

    def __repr__(self):
        return repr(self.stats_dict)

    def answer(self, card_sides, result):
        pass #STUB
