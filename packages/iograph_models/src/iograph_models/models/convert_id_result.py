from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConvertIdResult(BaseModel):
	errorDetails: Optional[GenericError] = Field(default=None,alias="errorDetails",)
	sourceId: Optional[str] = Field(default=None,alias="sourceId",)
	targetId: Optional[str] = Field(default=None,alias="targetId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .generic_error import GenericError

