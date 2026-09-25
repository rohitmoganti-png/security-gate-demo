import jwt


def issue_token(user_id: int) -> str:
    """Short-lived API token for the mobile app."""
    return jwt.encode({"sub": user_id}, "billing-signing-secret", algorithm="HS256")
