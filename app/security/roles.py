from fastapi import Depends, HTTPException, status
from app.security.dependencies import get_current_user

def admin_only(user=Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return user


def staff_or_admin(user=Depends(get_current_user)):
    if user["role"] not in ["admin", "staff"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Staff or Admin access required"
        )
    return user
