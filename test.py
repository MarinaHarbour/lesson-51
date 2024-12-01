from tests_12_1 import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        name = Runner('Anna')
        for i in range(1, 11):
            name.walk()
        self.assertEqual(name.distance, 50)

    def test_run(self):
        name = Runner('Igor')
        for i in range(1, 11):
            name.run()
        self.assertEqual(name.distance, 100)

    def test_challenge(self):
        name1 = Runner('Vanya')
        name2 = Runner('Sasha')
        for i in range(1, 11):
            name1.run()
            name2.walk()
        self.assertNotEqual(name1.distance, name2.distance)


if __name__ == "__main__":
    unittest.main()
