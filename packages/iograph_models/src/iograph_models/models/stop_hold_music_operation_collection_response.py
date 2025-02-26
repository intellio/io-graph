from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class StopHoldMusicOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[StopHoldMusicOperation] = Field(alias="value",)

from .stop_hold_music_operation import StopHoldMusicOperation

