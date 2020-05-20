import unittest
import airML


class TestAirML(unittest.TestCase):
    def test_list(self):
        result = airML.list(False)
        self.assertIsNone(result)

    def test_install(self):
        modelID = "http://github.org/aksw/NSpM/monument_300"
        format = "NSPM/Model"
        version = "0"

        result = airML.install(modelID, format, version)
        self.assertIsNone(result)

    def test_removeKNS(self):
        kns = "https://raw.github.com/AKSW/kbox/master"
        result = airML.removeKNS(kns)
        self.assertIsNone(result)

    def test_getInfo(self):
        modelID = "http://github.org/aksw/NSpM/monument_300"
        format = "NSPM/Model"
        version = "0"

        result = airML.getInfo(modelID, format, version)
        self.assertIsNone(result)

    def test_locate(self):
        modelID = "http://github.org/aksw/NSpM/monument_300"
        format = "NSPM/Model"
        version = "0"

        result = airML.locate(modelID, format, version)
        self.assertEqual(result, '/home/oshara/.kbox/NSPM/Model/0/http/org/github/aksw/NSpM/monument_300')

    # def test_search(self):
    #     pattern = ""
    #     format = ""
    #     version = ""
    #
    #     result = airML.search(pattern, format, version)

    def test_getModelDirPath(self):
        result = airML.getModelDirPath()
        self.assertEqual(result, "/home/oshara/.kbox")

    def test_setModelDirPath(self):
        dir = "/home/oshara/.kbox"
        airML.setModelDirPath(dir)
        result = airML.getModelDirPath()
        self.assertEqual(result, dir)
