from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MacOSLobChildApp(BaseModel):
	buildNumber: Optional[str] = Field(default=None,alias="buildNumber",)
	bundleId: Optional[str] = Field(default=None,alias="bundleId",)
	versionNumber: Optional[str] = Field(default=None,alias="versionNumber",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


