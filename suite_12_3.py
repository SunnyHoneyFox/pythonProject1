import unittest
from runner import Runner


def skip_if_frozen(test_func):
    def wrapper(self):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return test_func(self)
    return wrapper

class RunnerTest(unittest.TestCase):

    @skip_if_frozen
    def test_walk(self):
        runner = Runner('runner')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner('runner')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Runner 1")
        runner2 = Runner("Runner 2")

        for i in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()


import unittest
from runner_and_tournament import Runner, Tournament


def skip_if_frozen(test_func):
    def wrapper(self):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return test_func(self)

    return wrapper


class TournamentTest(unittest.TestCase):
    is_frozen = True
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

    @skip_if_frozen
    def test_race_usain_and_nik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results.append({place: str(runner) for place, runner in results.items()})
        self.check_last_runner()

    @skip_if_frozen
    def test_race_andrey_and_nik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.append({place: str(runner) for place, runner in results.items()})
        self.check_last_runner()

    @skip_if_frozen
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
