from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AssignmentFilterValidationResult(BaseModel):
	isValidRule: Optional[bool] = Field(alias="isValidRule", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

