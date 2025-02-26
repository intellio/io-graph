from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SubscribeToToneOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SubscribeToToneOperation] = Field(alias="value",)

from .subscribe_to_tone_operation import SubscribeToToneOperation

