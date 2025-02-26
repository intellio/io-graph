from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecureScoreControlStateUpdateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SecureScoreControlStateUpdate] = Field(alias="value",)

from .secure_score_control_state_update import SecureScoreControlStateUpdate

