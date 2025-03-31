from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ConvertIdResult(BaseModel):
	errorDetails: Optional[GenericError] = Field(alias="errorDetails", default=None,)
	sourceId: Optional[str] = Field(alias="sourceId", default=None,)
	targetId: Optional[str] = Field(alias="targetId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .generic_error import GenericError
