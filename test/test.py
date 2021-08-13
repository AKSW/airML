from airML import airML
import unittest
import json


class TestAirML(unittest.TestCase):
    def test_list(self):
        output = airML.execute('list -o json')
        output = json.loads(output)
        self.assertTrue(isinstance(output, dict))
        self.assertEqual(output['status_code'], 200)

    def test_list_kns(self):
        output = airML.execute('list kns -o json')
        output = json.loads(output)
        self.assertTrue(isinstance(output, dict))
        self.assertEqual(output['status_code'], 200)

    def test_info(self):
        output = airML.execute("info http://purl.org/pcp-on-web/dbpedia -o json")
        output = json.loads(output)
        self.assertTrue(isinstance(output, dict))
        self.assertEqual(output['status_code'], 200)

    def test_search(self):
        output = airML.execute('search ontology -o json')
        output = json.loads(output)
        self.assertTrue(isinstance(output, dict))
        self.assertEqual(output['status_code'], 200)

    def test_dir(self):
        output = airML.execute('r-dir -o json')
        output = json.loads(output)
        self.assertTrue(isinstance(output, dict))
        self.assertEqual(output['status_code'], 200)

    def test_version(self):
        output = airML.execute('-version -o json')
        output = json.loads(output)
        self.assertTrue(isinstance(output, dict))
        self.assertEqual(output['status_code'], 200)

    def test_invalid_command(self):
        output = airML.execute('lists')
        self.assertTrue("KBox.jar <command> [option]" in output)

    def test_list_function(self):
        output = airML.list(False)
        self.assertTrue('"status_code": 200,' in output)

    def test_install_function(self):
        output = airML.install('http://nspm.org/art', format="nspm")
        self.assertTrue('"message": "http://nspm.org/art KB installed.",' in output)

    def test_getInfo_function(self):
        output = airML.getInfo('http://nspm.org/art')
        self.assertTrue('"Publisher:": "KBox team"' in output)

    def test_locate_function(self):
        output = airML.locate('http://nspm.org/art', format='nspm')
        self.assertTrue('"status_code": 200,' in output)

    def test_search_function(self):
        output = airML.search('art')
        print(output)
        self.assertTrue('"status_code": 200,' in output)


if __name__ == '__main__':
    unittest.main()
