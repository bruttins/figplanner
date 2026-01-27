import unittest
from rotation import create_rotation_table

#3-value boundary checks: valids first 4, 5, 7
class TestRotationStructure(unittest.TestCase):
    def test_rotation_4_names(self):
        names_4 = ["Alice", "Bob", "Charlie", "Diana"]
        result_4 = create_rotation_table(names_4)
        
        self.assertEqual(len(result_4), 4, "Should have 4 rounds")
        
        trainees = [round_data["trainee"] for round_data in result_4]
        self.assertEqual(len(set(trainees)), 4)
        self.assertEqual(set(trainees), set(names_4))
        print(result_4)
 
    def test_rotation_5_names(self):
        names_5 = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
        result_5 = create_rotation_table(names_5)
        
        self.assertEqual(len(result_5), 5)
        
        trainees = [round_data["trainee"] for round_data in result_5]
        self.assertEqual(len(set(trainees)), 5)
        print(result_5)
    
    def test_rotation_7_names(self):
        names_7 = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace"]
        result_7 = create_rotation_table(names_7)
        
        self.assertEqual(len(result_7), 7)
        print(result_7)

#invalid values: 3, 8, duplicates
class TestInvalidInputs(unittest.TestCase):
    def test_too_few_names(self):
        with self.assertRaises(ValueError):
            create_rotation_table(["Alice", "Bob"])
    
    def test_too_many_names(self):
        with self.assertRaises(ValueError):
            create_rotation_table(["A", "B", "C", "D", "E", "F", "G", "H"])
    
    def test_duplicate_names(self):
        with self.assertRaises(ValueError):
            create_rotation_table(["Alice", "Bob", "Alice", "Diana"])	

class TestPositionLimits(unittest.TestCase):
    def test_position_limit_5(self):
        names_5 = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
        result_5 = create_rotation_table(names_5)
        
        role_counts = {name: {"helper": 0, "observer": 0, "trainee": 0} 
                       for name in names_5}
        
        for round_data in result_5:
            role_counts[round_data["fig1"]]["helper"] += 1
            role_counts[round_data["fig2"]]["helper"] += 1
            role_counts[round_data["observer"]]["observer"] += 1
            role_counts[round_data["trainee"]]["trainee"] += 1
        
        for name, counts in role_counts.items():
            self.assertLessEqual(counts["helper"], 3, f"{name} was helper {counts['helper']} times")
            self.assertLessEqual(counts["observer"], 3, f"{name} was observer {counts['observer']} times")
            self.assertEqual(counts["trainee"], 1, f"{name} was trainee {counts['trainee']} times")


    def test_position_limit_6(self):
        names_6 = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Sabi"]
        result_6 = create_rotation_table(names_6)
        
        role_counts = {name: {"helper": 0, "observer": 0, "trainee": 0} 
                       for name in names_6}
        
        for round_data in result_6:
            role_counts[round_data["fig1"]]["helper"] += 1
            role_counts[round_data["fig2"]]["helper"] += 1
            role_counts[round_data["observer"]]["observer"] += 1
            role_counts[round_data["trainee"]]["trainee"] += 1
        
        for name, counts in role_counts.items():
            self.assertLessEqual(counts["helper"], 3, f"{name} was helper {counts['helper']} times")
            self.assertLessEqual(counts["observer"], 3, f"{name} was observer {counts['observer']} times")
            self.assertEqual(counts["trainee"], 1, f"{name} was trainee {counts['trainee']} times")


    def test_position_limit_7(self):
        names_7 = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
        result_7 = create_rotation_table(names_7)
        
        role_counts = {name: {"helper": 0, "observer": 0, "trainee": 0} 
                       for name in names_7}
        
        for round_data in result_7:
            role_counts[round_data["fig1"]]["helper"] += 1
            role_counts[round_data["fig2"]]["helper"] += 1
            role_counts[round_data["observer"]]["observer"] += 1
            role_counts[round_data["trainee"]]["trainee"] += 1
        
        for name, counts in role_counts.items():
            self.assertLessEqual(counts["helper"], 3, f"{name} was helper {counts['helper']} times")
            self.assertLessEqual(counts["observer"], 3, f"{name} was observer {counts['observer']} times")
            self.assertEqual(counts["trainee"], 1, f"{name} was trainee {counts['trainee']} times")