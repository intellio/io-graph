from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PlayPromptOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[PlayPromptOperation]] = Field(default=None,alias="value",)

from .play_prompt_operation import PlayPromptOperation

