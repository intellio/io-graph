from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MacOSIncludedAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[MacOSIncludedApp] = Field(alias="value",)

from .mac_o_s_included_app import MacOSIncludedApp

