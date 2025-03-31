from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IosHomeScreenApp(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	odata_type: Literal["#microsoft.graph.iosHomeScreenApp"] = Field(alias="@odata.type", default="#microsoft.graph.iosHomeScreenApp")
	bundleID: Optional[str] = Field(alias="bundleID", default=None,)

