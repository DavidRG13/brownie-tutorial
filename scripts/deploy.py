from brownie import accounts, network, config, SimpleStorage, FundMe, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["develoment", "ganache-local"]

def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)

def deploy_fund_me():
    account = get_account()

    # if we are on a persistent network like rinkeby, use the associated address
    # otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        if len(MockV3Aggregator) <= 0:
            MockV3Aggregator.deploy(18, Web3.toWei(2000, "ether"), {"from": account})
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_simple_storage()
    deploy_fund_me()