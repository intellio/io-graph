from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RecommendedAction(BaseModel):
	actionWebUrl: Optional[str] = Field(default=None,alias="actionWebUrl",)
	potentialScoreImpact: Optional[float] | Optional[str] | ReferenceNumeric
	title: Optional[str] = Field(default=None,alias="title",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric

