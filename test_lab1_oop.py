import unittest
from unittest.mock import patch
from io import StringIO
from lab1_oop import OperationsWithMatrix


class TestSum(unittest.TestCase):

    def setUp(self):
        self.ops = OperationsWithMatrix()

    def test_sum_basic(self):
        A = [[1.0, 2.0], [3.0, 4.0]]
        B = [[1.0, 1.0], [1.0, 1.0]]
        self.assertEqual(self.ops.sum(A, B), [[2.0, 3.0], [4.0, 5.0]])

    def test_sum_zeros(self):
        A = [[0.0, 0.0], [0.0, 0.0]]
        B = [[0.0, 0.0], [0.0, 0.0]]
        self.assertEqual(self.ops.sum(A, B), [[0.0, 0.0], [0.0, 0.0]])

    def test_sum_negative_values(self):
        A = [[-1.0, -2.0], [-3.0, -4.0]]
        B = [[1.0, 2.0], [3.0, 4.0]]
        self.assertEqual(self.ops.sum(A, B), [[0.0, 0.0], [0.0, 0.0]])

    def test_sum_float_precision(self):
        A = [[1.5, 2.5], [3.5, 4.5]]
        B = [[0.5, 0.5], [0.5, 0.5]]
        self.assertEqual(self.ops.sum(A, B), [[2.0, 3.0], [4.0, 5.0]])

    def test_sum_single_element(self):
        A = [[5.0]]
        B = [[3.0]]
        self.assertEqual(self.ops.sum(A, B), [[8.0]])

    def test_sum_1x3_matrix(self):
        A = [[1.0, 2.0, 3.0]]
        B = [[4.0, 5.0, 6.0]]
        self.assertEqual(self.ops.sum(A, B), [[5.0, 7.0, 9.0]])

    def test_sum_3x1_matrix(self):
        A = [[1.0], [2.0], [3.0]]
        B = [[4.0], [5.0], [6.0]]
        self.assertEqual(self.ops.sum(A, B), [[5.0], [7.0], [9.0]])

    def test_sum_large_values(self):
        A = [[1000.5, 2000.5]]
        B = [[3000.5, 4000.5]]
        self.assertEqual(self.ops.sum(A, B), [[4001.0, 6001.0]])

    def test_sum_result_type(self):
        A = [[1.0, 2.0], [3.0, 4.0]]
        B = [[1.0, 1.0], [1.0, 1.0]]
        result = self.ops.sum(A, B)
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], list)

    def test_sum_converts_int_to_float(self):
        A = [[1, 2], [3, 4]]
        B = [[1, 1], [1, 1]]
        result = self.ops.sum(A, B)
        self.assertEqual(result, [[2.0, 3.0], [4.0, 5.0]])


class TestSpacialCalculation(unittest.TestCase):

    def setUp(self):
        self.ops = OperationsWithMatrix()

    def test_spacial_basic(self):
        C = [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0]
        ]
        self.assertEqual(self.ops.spacial_calculation(C), 14.0)

    def test_spacial_single_row_even(self):
        C = [[3.0, 1.0, 2.0]]
        self.assertEqual(self.ops.spacial_calculation(C), 1.0)

    def test_spacial_two_rows(self):
        C = [
            [5.0, 1.0, 3.0],
            [2.0, 8.0, 4.0],
        ]
        self.assertEqual(self.ops.spacial_calculation(C), 9.0)

    def test_spacial_all_equal_elements(self):
        C = [
            [5.0, 5.0, 5.0],
            [3.0, 3.0, 3.0],
        ]
        self.assertEqual(self.ops.spacial_calculation(C), 8.0)

    def test_spacial_negative_values(self):
        C = [
            [-1.0, -5.0, -3.0],
            [-1.0, -5.0, -3.0],
        ]
        self.assertEqual(self.ops.spacial_calculation(C), -6.0)

    def test_spacial_four_rows(self):
        C = [
            [1.0, 2.0],
            [3.0, 4.0],
            [5.0, 6.0],
            [7.0, 8.0],
        ]
        self.assertEqual(self.ops.spacial_calculation(C), 18.0)

    def test_spacial_result_type(self):
        C = [[1.0, 2.0], [3.0, 4.0]]
        result = self.ops.spacial_calculation(C)
        self.assertIsInstance(result, float)


class TestPrintResults(unittest.TestCase):

    def setUp(self):
        self.ops = OperationsWithMatrix()

    def test_print_contains_matrix_label(self):
        C = [[2.0, 3.0], [4.0, 5.0]]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.ops.print_results(C, 7.0)
            output = fake_out.getvalue()
        self.assertIn("C = A + B", output)

    def test_print_contains_result_value(self):
        C = [[2.0, 3.0], [4.0, 5.0]]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.ops.print_results(C, 7.0)
            output = fake_out.getvalue()
        self.assertIn("7.0", output)

    def test_print_float_format(self):
        C = [[2.123, 3.456]]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.ops.print_results(C, 0.0)
            output = fake_out.getvalue()
        self.assertIn("2.1", output)
        self.assertIn("3.5", output)


class TestMatrix(unittest.TestCase):

    def setUp(self):
        self.ops = OperationsWithMatrix()

    def test_matrix_runs_without_error(self):
        try:
            with patch('sys.stdout', new=StringIO()):
                self.ops.matrix()
        except Exception as e:
            self.fail(f"matrix() викинув виняток: {e}")

    def test_matrix_output_has_result(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.ops.matrix()
            output = fake_out.getvalue()
        self.assertIn("C = A + B", output)

    def test_matrix_correct_sum_output(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.ops.matrix()
            output = fake_out.getvalue()
        self.assertIn("2.0", output)


class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.ops = OperationsWithMatrix()

    def test_sum_then_spacial(self):
        A = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
        B = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
        C = self.ops.sum(A, B)
        result = self.ops.spacial_calculation(C)
        self.assertEqual(result, 14.0)

    def test_sum_then_print(self):
        A = [[1.0, 2.0], [3.0, 4.0]]
        B = [[1.0, 1.0], [1.0, 1.0]]
        C = self.ops.sum(A, B)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.ops.print_results(C, 99.0)
            output = fake_out.getvalue()
        self.assertIn("99.0", output)
        self.assertIn("C = A + B", output)


if __name__ == '__main__':
    unittest.main()