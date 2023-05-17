from scripts.helpful_scripts import get_account, SimpleCollectible

sample_token_uri = "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png"
OPENSEA_URL = "http://testnets.opensea.io/assets/{}/{}"


def main():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from":account})
    tx = simple_collectible.createCollectible(sample_token_uri,{"from":account})
    tx.wait(1)
    print(
        f"Awesome, you can view your NFT at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter()-1)}"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button. ")