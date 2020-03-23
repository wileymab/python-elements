import os
import unittest


class BaseTest(unittest.TestCase):   
    """
    This class subclasses from unittest.TestCase, and overloads methods to 
    provide better test failure messaging.
    """
    def __init__(self, methodName):
        super().__init__(methodName)

    @classmethod
    def file_resource(cls, test_file_path: str, resource_sub_path: str):
        test_suite_directory = os.path.dirname(test_file_path)
        test_suite_filename = os.path.basename(test_file_path).replace('.py','')
        return os.path.join(
            test_suite_directory,
            f"resources/{test_suite_filename}", resource_sub_path
        )

    @classmethod
    def _build_failure_message(cls, failure_message: str, expected: any, actual: any):
        """
        Accepts a simple user message, an expected value, and an actual value 
        and use these to build a more readable test failure message.
        """
        return f"\n{failure_message} --> Expected: {str(expected)}, Actual: {str(actual)}\n"

    def assertEqual(self, expected: any, actual: any, failure_message="") -> None:
        """
        Opinionated overload of unittest.TestCase.assertEqual with better test failure messaging.

        Usage:
        ```python
            # Some test logic
            def test_result_is_pi():
                data = {
                    "pi": 9000
                }
                self.assertEqual(
                    expected=3.14159,
                    actual=data.get("pi"), 
                    failure_message="Bad value for data.pi"
                )
        ```
        ```
            # Resulting failure message
            E   AssertionError: 3.14159 != 9000 : 
            E   Bad value for data.pi --> Expected: 3.14159, Actual: 9000
        ```

        :param expected: [Expected test value.]
        :type expected: any
        :param actual: [Actual test value.]
        :type actual: any
        :param failure_message: [Simple message about the failure.], defaults to ""
        :type failure_message: str, optional
        """                   
        super().assertEqual(
            first=expected,
            second=actual,
            msg=BaseTest._build_failure_message(
                failure_message=failure_message,
                expected=expected,
                actual=actual
            )
        )
