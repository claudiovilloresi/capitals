import unittest
from mypackages.capitals import check_capital, check_state
import os

#test the repository

class TestGithub(unittest.TestCase):

#open the test
    def setUp(self):
        self.temporary_file = "/tmp/test_empty_datafile"
        f = open(self.temporary_file, 'w')
        f.close()

    def test_non_existing_repo(self):
        res = github.check_capital("X", "Y")
        res = github.check_state("X","Y")
        self.assertFalse(res)

    def test_empty_repo(self):
        res = github.check_capital("", "")
        res = github.check_state("","")
        self.assertFalse(res)

    def test_mismatched_repo(self):
        res = github.check_capital("claudiovilloresi", "capitals")
        res = github.check_state("claudiovilloresi","capitals")
        self.assertFalse(res)

    def test_correct_repo(self):
        res = github.check_capital("swdevel-lab-h-farm-2019", "capitals",
                                verbose=True)
        res = github.check_state ("swdevel-lab-h-farm-2019","capitals",
                                verbose=True)
        self.assertTrue(res)

#close the test
    def tearDown(self):
        os.remove(self.temporary_file)

#test the data
    def setUp(self):
        self.temporary_file = "/tmp/test_empty_datafile"
        f = open(self.temporary_file, 'w')
        f.close()


class TestAnalyser(unittest.TestCase):
#Here we test the valid imput.
    def testValid (self):
        capital_list = [{'Aland Islands':'Mariehamn',
                            'Albania':'Tirana',
                            'Andorra':'Andorra la Vella',
                            'Armenia':'Yerevan',
                            'Austria':'Vienna',
                            'Azerbaijan':'Baku',
                            'Belarus':'Minsk',
                            'Belgium':'Brussels',
                            'Bosnia and Herzegovina':'Sarajevo',
                            'Bulgaria':'Sofia',
                            'Croatia':'Zagreb',
                            'Cyprus':'Nicosia',
                            'Czech Republic':'Prague',
                            'Denmark':'Copenhagen',
                            'Estonia':'Tallinn',
                            'Faroe Islands':'Torshavn',
                            'Finland':'Helsinki',
                            'France':'Paris',
                            'Georgia':'Tbilisi',
                            'Germany':'Berlin',
                            'Gibraltar':'Gibraltar',
                            'Greece':'Athens',
                            'Guernsey':'Saint Peter Port',
                            'Hungary':'Budapest',
                            'Iceland':'Reykjavik',
                            'Ireland':'Dublin',
                            'Isle of Man':'Douglas',
                            'Italy':'Rome',
                            'Jersey':'Saint Helier',
                            'Kosovo':'Pristina',
                            'Latvia':'Riga',
                            'Liechtenstein':'Vaduz',
                            'Lithuania':'Vilnius',
                            'Luxembourg':'Luxembourg',
                            'Macedonia':'Skopje',
                            'Malta':'Valletta',
                            'Moldova':'Chisinau',
                            'Monaco':'Monaco',
                            'Montenegro':'Podgorica',
                            'Netherlands':'Amsterdam',
                            'Northern Cyprus':'North Nicosia',
                            'Norway':'Oslo',
                            'Poland':'Warsaw',
                            'Portugal':'Lisbon',
                            'Romania':'Bucharest',
                            'Russia':'Moscow',
                            'San Marino':'San Marino',
                            'Serbia':'Belgrade',
                            'Slovakia':'Bratislava',
                            'Slovenia':'Ljubljana',
                            'Spain':'Madrid',
                            'Svalbard':'Longyearbyen',
                            'Sweden':'Stockholm',
                            'Switzerland':'Bern',
                            'Turkey':'Ankara',
                            'Ukraine':'Kyiv',
                            'United Kingdom':'London',
                            'Vatican City':'Vatican City'}]
                      oe, lm = github.check_capital(capital_list)
                      oe, lm = github.check_state(capital_list)
                            self.assertEqual(oe, 1)
                            self.assertEqual(lm, 1)

#test 2: Test with an empty list
    def testEmpty(self):
            oe, lm = github.check_capital([])
            oe, lm = github.check_state([])
            self.assertFalse(oe)
            self.assertFalse(lm)

#close the test
    def tearDown(self):
        os.remove(self.temporary_file)
