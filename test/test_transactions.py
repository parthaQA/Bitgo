import pytest


@pytest.mark.usefixtures("setup")
class TestTransactions:


    def test_Validate_the_section_has_the_heading_25_of_2875_Transactions(self):
        expected_title = "Block #680000: 000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732 · Bitcoin Explorer - Blockstream.info"
        expected_text = "25 of 2875 Transactions"
        assert self.main_page.validate_page_title(expected_title)
        print("actual text : ",self.main_page.validate_text())
        assert self.main_page.validate_text() == expected_text, f"Expected text '{expected_text}' not found on the page."


    def test_parse_through_the_25_transactions_which_are_visible_on_the_page(self):

        assert self.main_page.get_transactions_count() == 25, f"Expected 25 transactions, but found {len(transactions)}."
        print("Transactions on the page:", self.main_page.get_transactions_count())

    def test_print_the_transaction_hash_of_the_transactions_which_has_exactly_1_input_and_2_outputs(self):
        self.main_page.get_transaction_for_one_input_and_two_outputs()


