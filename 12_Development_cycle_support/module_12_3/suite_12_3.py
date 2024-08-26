import unittest
import tests_12_1
import tests_12_2
import tests_12_3

tourST = unittest.TestSuite()
tourST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
tourST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
tourST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tourST)