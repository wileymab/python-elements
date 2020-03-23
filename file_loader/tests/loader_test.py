
from test_utils.base_test import BaseTest

from file_loader.loader import FileLoader

class FileLoaderTests(BaseTest):

    def test_can_load_json(self):
        data = FileLoader.load_json_file(
            file_name=FileLoaderTests.file_resource(__file__, 'json/valid.json')
        )
        self._valid_file_load_assertions(data=data)

    def test_can_load_yaml(self):
        data = FileLoader.load_yaml_file(
            file_name=FileLoaderTests.file_resource(__file__, 'yaml/valid.yaml')
        )
        self._valid_file_load_assertions(data=data)


    def _valid_file_load_assertions(self, data: dict):
        self.assertIsInstance(data, dict)
        self.assertEqual(expected="matt", actual=data.get("name"), failure_message="Error on 'name' definition.")
        self.assertEqual(expected=38, actual=data.get("age"), failure_message="Error on 'age' definition.")
        self.assertEqual(expected=0.67, actual=data.get("pocket_cash"), failure_message="Error on 'pocket_cash' definition.")

        self.assertIsInstance(data.get("hobbies"), list)
        self.assertEqual(expected=2, actual=len(data.get("hobbies")), failure_message="Error on 'hobbies' definition.")
        self.assertEqual(expected="sleeping", actual=data.get("hobbies")[0], failure_message="Error on 'hobbies[0]' definition.")
        self.assertEqual(expected="drinking beer", actual=data.get("hobbies")[1], failure_message="Error on 'hobbies[1]' definition.")

        self.assertIsInstance(data.get("stats"), dict)
        self.assertEqual(expected=18.038, actual=data.get("stats").get("powerlevel"), failure_message="Error on 'stats.powerlevel' definition.")
        self.assertEqual(expected=0.017, actual=data.get("stats").get("restlevel"), failure_message="Error on 'stats.restlevel' definition.")
        self.assertEqual(expected=9000, actual=data.get("stats").get("unused_journal_count"), failure_message="Error on 'stats.unused_journal_count' definition.")
        self.assertEqual(expected="disestablishmentarianism", actual=data.get("stats").get("word"), failure_message="Error on 'stats.word' definition.")