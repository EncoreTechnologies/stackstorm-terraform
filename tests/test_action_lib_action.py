from terraform_base_action_test_case import TerraformBaseActionTestCase
from lib.action import Action
# Using this to run tests. Otherwise get an error for no run method.
from init import Init
import mock


class ActionTestCase(TerraformBaseActionTestCase):
    __test__ = True
    action_cls = Init

    @mock.patch("lib.action.Terraform")
    def test_init(self, mock_trfm):
        action = self.get_action_instance({})
        self.assertIsInstance(action, Action)
        self.assertEqual(action.terraform, mock_trfm())

    def test_check_result_success(self):
        action = self.get_action_instance({})
        # Declare test input values
        test_return_code = 0
        test_stdout = "Terraform has been successfully initialized!"
        test_stderr = ""

        test_output = test_stdout + "\n" + test_stderr
        expected_result = (True, test_output)

        # Execute the run function
        result = action.check_result(test_return_code, test_stdout, test_stderr)

        # Verify the results
        self.assertEqual(result, expected_result)

    def test_check_result_fail(self):
        action = self.get_action_instance({})
        # Declare test input values
        test_return_code = 1
        test_stdout = "Initialization failed!"
        test_stderr = "Error details..."

        test_output = test_stdout + "\n" + test_stderr
        expected_result = (False, test_output)

        # Execute the run function
        result = action.check_result(test_return_code, test_stdout, test_stderr)

        # Verify the results
        self.assertEqual(result, expected_result)
