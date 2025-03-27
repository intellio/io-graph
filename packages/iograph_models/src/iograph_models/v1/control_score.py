from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ControlScore(BaseModel):
	controlCategory: Optional[str] = Field(alias="controlCategory", default=None,)
	controlName: Optional[str] = Field(alias="controlName", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	score: float | str | ReferenceNumeric
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .reference_numeric import ReferenceNumeric

