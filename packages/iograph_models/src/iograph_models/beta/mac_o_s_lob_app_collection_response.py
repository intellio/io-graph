from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MacOSLobAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[MacOSLobApp]] = Field(alias="value", default=None,)

from .mac_o_s_lob_app import MacOSLobApp
