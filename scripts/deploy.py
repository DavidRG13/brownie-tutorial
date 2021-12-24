from brownie import accounts, network, config, SimpleStorage, FundMe, MockV3Aggregator

def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)

def deploy_fund_me():
    account = get_account()

    # if we are on a persistent network like rinkeby, use the associated address
    # otherwise, deploy mocks
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        mock_aggregator = MockV3Aggregator.deploy(18, 2000000000000000000000, {"from": account})
        price_feed_address = mock_aggregator.address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(fund_me)

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_simple_storage()
    deploy_fund_me()