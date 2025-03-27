from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDispositionReviewStage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	reviewersEmailAddresses: Optional[list[str]] = Field(alias="reviewersEmailAddresses", default=None,)
	stageNumber: Optional[str] = Field(alias="stageNumber", default=None,)


