from brownie import accounts, SimpleStorage

def test_deploy():
    # Given
    account = accounts[0]

    # When
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.get()

    # Then
    assert starting_value == 0

def test_updating_value():
    # Given
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.get()
    value_to_update = starting_value + 15

    # When
    simple_storage.store(value_to_update, {"from": account})

    # Then
    updated_value = simple_storage.get()
    assert updated_value == value_to_update