import json

from .socialScore import (
    SocialScoreCalculator,
    EngagementMetrics,
    ContentQuality,
    Trustworthiness,
    SocialImpact,
    MonetizationPotential,
    GovernanceParticipation,
)


def calculate_social_score(request):
    # Assuming you're getting the metrics data from the request
    # You'll need to implement the logic to extract these values from your data source

    calculator = SocialScoreCalculator()

    result = calculator.calculate_social_score(
        engagement=EngagementMetrics(
            engagement_rate=float(request.data["engagement_rate"]),
            interaction_quality=float(request.data["interaction_quality"]),
            growth_rate=float(request.data["growth_rate"]),
        ),
        content=ContentQuality(
            frequency=float(request.data["content_frequency"]),
            originality=float(request.data["content_originality"]),
            diversity=float(request.data["content_diversity"]),
        ),
        trust=Trustworthiness(
            trust_score=float(request.data["trust_score"]),
            verified_followers=float(request.data["verified_followers"]),
            reputation_index=float(request.data["reputation_index"]),
        ),
        impact=SocialImpact(
            network_influence=float(request.data["network_influence"]),
            trend_setting=float(request.data["trend_setting"]),
            mentions_reposts=float(request.data["mentions_reposts"]),
        ),
        monetization=MonetizationPotential(
            token_transactions=float(request.data["token_transactions"]),
            crowdfunding=float(request.data["crowdfunding"]),
            endorsement_success=float(request.data["endorsement_success"]),
        ),
        governance=GovernanceParticipation(
            voting_activity=float(request.data["voting_activity"]),
            proposal_contribution=float(request.data["proposal_contribution"]),
        ),
    )

    return JsonResponse(result)
