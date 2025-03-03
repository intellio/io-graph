from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecureScoreControlProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[SecureScoreControlProfile]] = Field(default=None,alias="value",)

from .secure_score_control_profile import SecureScoreControlProfile

