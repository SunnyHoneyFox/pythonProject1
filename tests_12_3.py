import unittest
import suite_12_3


run_tour_test = unittest.TestSuite()
run_tour_test.addTest(unittest.TestLoader().loadTestsFromTestCase(suite_12_3.RunnerTest))
run_tour_test.addTest(unittest.TestLoader().loadTestsFromTestCase(suite_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_tour_test)