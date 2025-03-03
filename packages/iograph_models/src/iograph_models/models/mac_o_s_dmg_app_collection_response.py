from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MacOSDmgAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[MacOSDmgApp]] = Field(default=None,alias="value",)

from .mac_o_s_dmg_app import MacOSDmgApp

