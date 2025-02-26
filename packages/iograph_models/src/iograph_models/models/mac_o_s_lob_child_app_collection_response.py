from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MacOSLobChildAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[MacOSLobChildApp] = Field(alias="value",)

from .mac_o_s_lob_child_app import MacOSLobChildApp

