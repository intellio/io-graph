from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedIOSLobAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[ManagedIOSLobApp] = Field(alias="value",)

from .managed_i_o_s_lob_app import ManagedIOSLobApp

