from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RestoreSessionBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[RestoreSessionBase] = Field(alias="value",)

from .restore_session_base import RestoreSessionBase

