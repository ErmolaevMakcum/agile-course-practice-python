import unittest

from statistics.viewmodel.viewmodel import StatisticsViewModel


class TestStatisticsViewModel(unittest.TestCase):

    def setUp(self):
        self.view_model = StatisticsViewModel()

    def test_by_default_button_disabled(self):
        self.assertEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_valid_string_button_enabled(self):
        self.view_model.set_instr("5 5", "5 5", "5 5")
        self.assertNotEqual('disabled', self.view_model.get_button_convert_state())

    def test_when_entered_invalid_string_button_disabled(self):
        self.view_model.set_instr("5+5", "5 5", "5 5")
        self.assertNotEqual('normal', self.view_model.get_button_convert_state())

    def test_can_get_input_string(self):
        self.view_model.set_instr("5 5", "5 5", "5 5")
        instr = self.view_model.get_stud1_txt()
        self.assertEqual("5 5", instr)

    def test_can_get_answer(self):
        self.view_model.set_instr("5 5", "5 5", "5 5")
        self.view_model.click_button()
        self.assertEqual(0, self.view_model.get_answer1())

    def test_add_empty_string_is_0(self):
        self.view_model.set_instr("", "", "")
        self.assertNotEqual('normal', self.view_model.get_button_convert_state())

    def test_add_negative_marks(self):
        self.view_model.set_instr("5 5", "-5 -5", "5 5")
        self.assertNotEqual('normal', self.view_model.get_button_convert_state())

    def test_add_marks_over_5(self):
        self.view_model.set_instr("5 7", "5 5", "5 5")
        self.assertNotEqual('normal', self.view_model.get_button_convert_state())
