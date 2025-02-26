from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AlertDetectionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[AlertDetection] = Field(alias="value",)

from .alert_detection import AlertDetection

