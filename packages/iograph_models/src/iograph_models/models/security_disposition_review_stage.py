from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityDispositionReviewStage(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	name: Optional[str] = Field(default=None,alias="name",)
	reviewersEmailAddresses: Optional[list[str]] = Field(default=None,alias="reviewersEmailAddresses",)
	stageNumber: Optional[str] = Field(default=None,alias="stageNumber",)


