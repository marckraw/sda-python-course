import pytest

from sample_2_wallet.wallet import Wallet, InsufficientAmount


class TestWallet:
    amount = 100

    def setup_method(self):
        self.empty_wallet = Wallet()
        self.wallet = Wallet(amount=self.amount)

    def test_default_initial_amount(self):
        expected = 0

        balance = self.empty_wallet.get_balance()

        assert balance == expected, "Should be empty"

    def test_setting_initial_amount(self):
        expected = 100

        balance = self.wallet.get_balance()

        assert balance == expected, "Should be 100"

    def test_spend_cash(self):
        spending = 30
        expected = 70

        self.wallet.spend_cash(spending)
        balance = self.wallet.get_balance()

        assert balance == expected

    def test_add_cash(self):
        cash = 50
        expected = 150

        self.wallet.add_cash(cash)
        balance = self.wallet.get_balance()

        assert balance == expected

    def test_spend_cash_raises_exception_on_insufficient_amount(self):
        with pytest.raises(InsufficientAmount):
            self.empty_wallet.spend_cash(150)

    @pytest.mark.parametrize('cash,spending,expected', (
            (100, 50, 50),
            (30, 20, 10),
            (1100, 1100, 0)
    ))
    def test_transaction(self, cash, spending, expected):
        self.empty_wallet.add_cash(cash)
        self.empty_wallet.spend_cash(spending)

        assert self.empty_wallet.get_balance() == expected
