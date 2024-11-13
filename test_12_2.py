class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        time = 0

        while self.participants:
            time += 1
            for participant in self.participants:

                participant.run()

                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1

                    self.participants.remove(participant)
                    break

        return finishers


import unittest


class TournamentTest(unittest.TestCase):
    all_results = []

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = Runner('Усейн', speed=10)
        self.runner2 = Runner('Андрей', speed=9)
        self.runner3 = Runner('Ник', speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            print(result)

    def test_race_usain_and_nik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results.append({place: str(runner) for place, runner in results.items()})
        self.check_last_runner()

    def test_race_andrey_and_nik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.append({place: str(runner) for place, runner in results.items()})
        self.check_last_runner()

    def test_race_usain_andrey_and_nik(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.append({place: str(runner) for place, runner in results.items()})
        self.check_last_runner()

    def check_last_runner(self):
        if self.all_results:
            last_result = self.all_results[-1]
            last_place = max(last_result.keys())
            last_runner_name = last_result[last_place]

            expected_last_runner_name = 'Ник'
            self.assertTrue(last_runner_name == expected_last_runner_name)


if __name__ == '__main__':
    unittest.main()
