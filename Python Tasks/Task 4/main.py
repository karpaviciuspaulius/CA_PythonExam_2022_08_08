# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu.
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas:
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.

class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

    def wasExpensive(self):
        if self.budget > 100_000_000:
            print(
                f'{self.title} directed by {self.director} had a budget of ${self.budget}! Which is expensive!')
        else:
            print(
                f'Even though the budget of {self.title} was ${self.budget} bellow 100,000,000 the movie is not regarded as expensive.')


lotr_1 = Movie('LOTR: The Fellowship of the ring', 'Peter Jackson', 93_000_000)
lotr_2 = Movie('LOTR: The Two Towers', 'Peter Jackson', 94_000_000)
lotr_3 = Movie('LOTR: The Return of the King', 'Peter Jackson',
               100_000_001)  # it was actually 94M usd as well :)

lotr_1.wasExpensive()
lotr_2.wasExpensive()
lotr_3.wasExpensive()
