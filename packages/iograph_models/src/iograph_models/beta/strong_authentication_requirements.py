from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class StrongAuthenticationRequirements(BaseModel):
	perUserMfaState: Optional[PerUserMfaState | str] = Field(alias="perUserMfaState", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .per_user_mfa_state import PerUserMfaState
