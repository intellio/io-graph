from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityDispositionReviewStage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.dispositionReviewStage"] = Field(alias="@odata.type", default="#microsoft.graph.security.dispositionReviewStage")
	name: Optional[str] = Field(alias="name", default=None,)
	reviewersEmailAddresses: Optional[list[str]] = Field(alias="reviewersEmailAddresses", default=None,)
	stageNumber: Optional[str] = Field(alias="stageNumber", default=None,)

