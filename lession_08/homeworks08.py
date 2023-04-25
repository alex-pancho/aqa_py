""" Задача 1-10 - оберіть 10 домашніх завдань та покрийте їх тестами.
Код закомітьте в гіт, надайте посилання.
"""
"""First exercise"""
import unittest

def union(set_1, set_2):
    return set_1.union(set_2)

def calculate_perimeter(a, b, c, d):
    return a + b + c + d

def calculate_total_pages(total_photos, quantity_of_photos_in_one_page):
    return (total_photos + quantity_of_photos_in_one_page - 1) // quantity_of_photos_in_one_page

def symmetric_difference(set1, set2):
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    symmetric_difference_set = set1 ^ set2
    return symmetric_difference_set


def calculate_total_sea_area():
    area_of_the_black_sea = 436402
    area_of_the_azov_sea = 37800 
    total_sea_area = area_of_the_black_sea + area_of_the_azov_sea
    return total_sea_area

def calculate_computer_price():
    month_1 = 1179
    total_months = int(12 * 1.5)
    computer_price = total_months * month_1
    return computer_price

def calculate_total_cost_of_products():
    big_pizzas = 4*274
    medium_pizzas = 2*218
    juices = 4*35
    cake = 350
    water = 3*21
    total_cost_of_products = big_pizzas + medium_pizzas + juices + cake + water
    return total_cost_of_products

    


class TestHomework(unittest.TestCase):

    def test_empty_sets(self):
        """Union of set_1 and set_2"""
        self.assertEqual(union(set(), set()), set())

    def test_same_sets(self):
        """Union of set_1 and set_2"""
        set_1 = {1, 2, 3, 4}
        set_2 = {1, 2, 3, 4}
        self.assertEqual(union(set_1, set_2), set_1)

    def test_disjoint_sets(self):
        """Union of set_1 and set_2"""
        set_1 = {1, 2, 3, 4}
        set_2 = {5, 6, 7, 8}
        self.assertEqual(union(set_1, set_2), {1, 2, 3, 4, 5, 6, 7, 8})

    def test_overlapping_sets(self):
        """Union of set_1 and set_2"""
        set_1 = {1, 2, 3, 4}
        set_2 = {3, 4, 5, 6}
        self.assertEqual(union(set_1, set_2), {1, 2, 3, 4, 5, 6})
    
    def test_calculate_perimeter(self):
        """Perimeter of a, b, c and d"""
        self.assertEqual(calculate_perimeter(1, 2, 3, 4), 10)
        self.assertEqual(calculate_perimeter(5, 5, 5, 5), 20)
        self.assertEqual(calculate_perimeter(0, 0, 0, 0), 0)
        self.assertEqual(calculate_perimeter(1, 1, 1, 1), 4)
        self.assertEqual(calculate_perimeter(3, 4, 5, 6), 18)

    def test_calculate_total_pages(self):
        """"Total pages of photos"""
        total_photos = 232
        quantity_of_photos_in_one_page = 8
        expected_total_pages = 29
        actual_total_pages = calculate_total_pages(total_photos, quantity_of_photos_in_one_page)
        self.assertEqual(actual_total_pages, expected_total_pages)

    def test_calculate_total_sea_area(self):
        """Total sea area"""
        area_of_the_black_sea = 436402
        area_of_the_azov_sea = 37800 
        expected_total_sea_area = area_of_the_black_sea + area_of_the_azov_sea
        total_sea_area = calculate_total_sea_area()
        self.assertEqual(total_sea_area, expected_total_sea_area)
    
    def test_symmetric_difference(self):
        """Symetric difference of set1 and set2"""
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        expected_result = {1, 2, 5, 6}
        assert symmetric_difference(set1, set2) == expected_result

    def test_calculate_computer_price(self):
        """Computer price"""
        self.assertEqual(calculate_computer_price(), 21222)

    def test_calculate_total_cost_of_products(self):
        """Total cost of products"""
        total_cost = calculate_total_cost_of_products()
        self.assertEqual(total_cost, 2085)


if __name__ == '__main__':
    unittest.main()






