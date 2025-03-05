from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ControlScore(BaseModel):
	controlCategory: Optional[str] = Field(default=None,alias="controlCategory",)
	controlName: Optional[str] = Field(default=None,alias="controlName",)
	description: Optional[str] = Field(default=None,alias="description",)
	score: float | str | ReferenceNumeric
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .reference_numeric import ReferenceNumeric

