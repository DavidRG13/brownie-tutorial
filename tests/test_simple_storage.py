from brownie import accounts, SimpleStorage

def test_deploy():
    # Given
    account = accounts[0]

    # When
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.get()

    # Then
    assert starting_value == 0