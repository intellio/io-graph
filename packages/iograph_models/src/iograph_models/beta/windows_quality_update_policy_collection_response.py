from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsQualityUpdatePolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WindowsQualityUpdatePolicy]] = Field(alias="value", default=None,)

from .windows_quality_update_policy import WindowsQualityUpdatePolicy
