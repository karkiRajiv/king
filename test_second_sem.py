import unittest
from second_sem import *


class TestDataBase(unittest.TestCase):
    def test_search(self):
        search_entry.insert(0, 'Ankita')
        test_array = [(1, 'Utsav', 'Shahi', 'Bsc(Hons) Computing', 'Golfutar', '9874561230'),
                      (2, 'Rojina', 'Ghimire', 'Bsc(Hons) Ethical Hacking', 'Narayanthan', '9845612073'),
                      (3, 'Bidhan', 'rai', 'Bsc(Hons) Computing', 'Taulung', '9874512630'),
                      (4, 'Ankita', 'Chhetri', 'Bsc(Hons) Computing', 'Bansbari', '014256370')]

        expected_result = [(4, 'Ankita', 'Chhetri', 'Bsc(Hons) Computing', 'Bansbari', '014256370')]
        mylist = SEARCH_info(test_array)
        self.assertEqual(mylist, expected_result)

    def test_sort(self):
        array_test = [(1, 'Utsav', 'Shahi', 'Bsc(Hons) Computing', 'Golfutar', '9874561230'),
                      (2, 'Rojina', 'Ghimire', 'Bsc(Hons) Ethical Hacking', 'Narayanthan', '9845612073'),
                      (3, 'Bidhan', 'rai', 'Bsc(Hons) Computing', 'Taulung', '9874512630'),
                      (4, 'Ankita', 'Chhetri', 'Bsc(Hons) Computing', 'Bansbari', '14256370')]

        expected_result = [(4, 'Ankita', 'Chhetri', 'Bsc(Hons) Computing', 'Bansbari', '14256370'),
                           (3, 'Bidhan', 'rai', 'Bsc(Hons) Computing', 'Taulung', '9874512630'),
                           (2, 'Rojina', 'Ghimire', 'Bsc(Hons) Ethical Hacking', 'Narayanthan', '9845612073'),
                           (1, 'Utsav', 'Shahi', 'Bsc(Hons) Computing', 'Golfutar', '9874561230')]
        combo.set('STUDENT_ID')
        bubble_sort(array_test)
        self.assertEqual(array_test, expected_result)


if __name__ == '__main__':
    unittest.main()
