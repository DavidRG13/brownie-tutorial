from brownie import accounts, FundMe
from scripts.deploy import deploy_fund_me, get_account

def test_can_fund_and_withdraw():
    # Given
    account = get_account()
    fund_me = deploy_fund_me()
    
    # When
    tx = fund_me.fund({"from": account, "value": (50 * 10 ** 18) + 1})
    tx.wait(1)

    # Then
    assert fund_me.addressToAmountFunded(account.address) == (50 * 10 ** 18) + 1

    # When
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)

    # Then
    assert fund_me.addressToAmountFunded(account.address) == 0
