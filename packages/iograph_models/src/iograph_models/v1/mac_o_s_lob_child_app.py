from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MacOSLobChildApp(BaseModel):
	buildNumber: Optional[str] = Field(alias="buildNumber", default=None,)
	bundleId: Optional[str] = Field(alias="bundleId", default=None,)
	versionNumber: Optional[str] = Field(alias="versionNumber", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

