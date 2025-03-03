from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeletedChatCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[DeletedChat]] = Field(default=None,alias="value",)

from .deleted_chat import DeletedChat

