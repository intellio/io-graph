from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Validate_bulk_resizePostResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CloudPcResizeValidationResult]] = Field(alias="value", default=None,)

from .cloud_pc_resize_validation_result import CloudPcResizeValidationResult

