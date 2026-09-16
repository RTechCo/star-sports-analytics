def implied_probability(american_odds):
    if american_odds < 0:
        probability = abs(american_odds) / (abs(american_odds) + 100)
    else:
        probability = 100 / (american_odds + 100)

    return probability


home_odds = -150
away_odds = 130

home_probability = implied_probability(home_odds)
away_probability = implied_probability(away_odds)

print(f"Home implied probability: {home_probability:.2%}")
print(f"Away implied probability: {away_probability:.2%}")

total_probability = home_probability + away_probability

fair_home_probability = home_probability / total_probability
fair_away_probability = away_probability / total_probability

print("\n--- Noo-Vig Fair Probabilities ---")
print(f"Home fair probability: {fair_home_probability:.2%}")
print(f"Away fair probability: {fair_away_probability:.2%}")


def expected_value(american_odds, your_probability):
    if american_odds > 0:
        profit = american_odds / 100
    else:
        profit = 100 / abs(american_odds)

    loss_probability = 1 - your_probability

    ev = (your_probability * profit) - loss_probability

    return ev

your_home_probability = 0.63

home_ev = expected_value(home_odds, your_home_probability)

print("\n--- Your Analysis ---")
print(f"Your estimated probability: {your_home_probability:.2%}")
print(f"Market fair probability: {fair_home_probability:.2%}")
print(f"Expected value: {home_ev:.2%}")
      