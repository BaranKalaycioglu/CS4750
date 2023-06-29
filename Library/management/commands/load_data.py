import csv
from django.core.management import BaseCommand
from Library.models import Game

class Command(BaseCommand):
    help = 'Load a games csv file into the database'

    def handle(self, *args, **kwargs):
        with open('Library/game_data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            for row in reader:
                try:
                    game = Game()
                    game.name = row[0]
                    game.genre = row[1]
                    game.developer = row[2]
                    game.platform = row[3]
                    game.price = row[4]
                    game.save()
                    print(f"Game {game.name} saved successfully.")
                except Exception as e:
                    print(f"Failed to save Game {row[0]} due to error: {e}")
