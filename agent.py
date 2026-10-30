"""Rank supplied event listings against explicit user preferences."""
from __future__ import annotations


def recommend_events(request: dict, events: list[dict]) -> list[dict]:
    interests = {str(value).lower() for value in request.get("interests", [])}
    city = str(request.get("city", "")).lower()
    maximum = request.get("max_price")
    ranked = []
    for event in events:
        tags = {str(value).lower() for value in event.get("tags", [])}
        evidence, score = [], 0
        overlap = sorted(interests & tags)
        if overlap: score += 2; evidence.append({"match": "interests", "values": overlap})
        if city and str(event.get("city", "")).lower() == city: score += 1; evidence.append({"match": "city", "value": event.get("city")})
        price = event.get("price")
        if maximum is not None and price is not None and float(price) <= float(maximum): score += 1; evidence.append({"match": "budget", "value": price})
        ranked.append({"event_id": event.get("id"), "name": event.get("name"), "score": score, "evidence": evidence, "source": event.get("source"), "freshness": event.get("updated_at"), "booking_completed": False})
    return sorted(ranked, key=lambda item: (-item["score"], str(item["name"])))
