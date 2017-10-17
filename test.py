from build import spaces_to_dashes, get_ride_of_disabled_edda, root_path
from shutil import copyfile


import unittest

class TestJSONTransform(unittest.TestCase):

    def test_transform(self):
        tester = root_path("./test/tester.json")
        edda = root_path("./test/edda.json")
        original = root_path("./test/original.json")
        copyfile(original, tester)
        get_ride_of_disabled_edda(tester)
        spaces_to_dashes(tester)
        with open(tester) as f:
            content = f.readlines()
            content = [x.strip().replace(" ","") for x in content]
            with open(edda) as f:
                edda_content = f.read()
                edda_content = [x.strip().replace(" ","") for x in edda_content]
                self.assertEqual("".join(content).strip(), "".join(edda_content).strip())



if __name__ == '__main__':
    unittest.main()
