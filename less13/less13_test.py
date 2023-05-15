import unittest 
from less13_hw import LifeActions 

class TestLifeActions(unittest.TestCase):

    def test_initial_energy(self):
        """Test if all people has initial energy of 100"""
        self.assertEqual(LifeActions.energy, 100)


    def test_eat(self):
        """Test energy change for eat action"""
        action = LifeActions()
        actual_result = action.eat()
        expected_result = 105
        self.assertEqual(actual_result, expected_result)

    def test_sleep(self):
        """Test energy change for sleep action"""
        action = LifeActions()
        actual_result = action.sleep()
        expected_result = 110
        self.assertEqual(actual_result, expected_result)

    def test_speak(self):
        """Test energy change for speak action"""
        action = LifeActions()
        actual_result = action.speak()
        expected_result = 95
        self.assertEqual(actual_result, expected_result)


    def test_walk(self):
        """Test energy change for walk action"""
        action = LifeActions()
        actual_result = action.walk()
        expected_result = 90
        self.assertEqual(actual_result, expected_result)

    def test_homework(self):
        """Test energy change for homework action"""
        action = LifeActions()
        actual_result = action.homework()
        expected_result = 10
        self.assertEqual(actual_result, expected_result)






if __name__ == '__main__':
    unittest.main(verbosity=2)

