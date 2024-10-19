from thirdweb import ThirdwebSDK


def create_social_score_nft(wallet_address, social_score_result):
    # Initialize the Thirdweb SDK (you'll need to set up your environment variables)
    sdk = ThirdwebSDK.from_private_key(private_key="your-private-key", chain="ethereum")

    # Get your NFT collection contract
    nft_collection = sdk.get_nft_collection("your-nft-collection-address")

    # Create metadata for the NFT
    metadata = {
        "name": f"Social Score: {social_score_result['social_score']}",
        "description": f"Tier: {social_score_result['tier']}",
        "properties": {
            "engagement_score": social_score_result["engagement_score"],
            "content_score": social_score_result["content_score"],
            "trust_score": social_score_result["trust_score"],
            "impact_score": social_score_result["impact_score"],
            "monetization_score": social_score_result["monetization_score"],
            "governance_score": social_score_result["governance_score"],
        },
    }

    # Mint the NFT
    tx = nft_collection.mint_to(wallet_address, metadata)
    receipt = tx.receipt
    token_id = tx.id
    nft = tx.data()

    return nft
