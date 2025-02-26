from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class StartHoldMusicOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[StartHoldMusicOperation] = Field(alias="value",)

from .start_hold_music_operation import StartHoldMusicOperation

