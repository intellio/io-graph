from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RecommendedAction(BaseModel):
	actionWebUrl: Optional[str] = Field(alias="actionWebUrl",default=None,)
	potentialScoreImpact: float | str | ReferenceNumeric
	title: Optional[str] = Field(alias="title",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .reference_numeric import ReferenceNumeric

