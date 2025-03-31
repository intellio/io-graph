from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsQualityUpdateProductBuildVersionDetail(BaseModel):
	buildNumber: Optional[int] = Field(alias="buildNumber", default=None,)
	majorVersionNumber: Optional[int] = Field(alias="majorVersionNumber", default=None,)
	minorVersionNumber: Optional[int] = Field(alias="minorVersionNumber", default=None,)
	updateBuildRevision: Optional[int] = Field(alias="updateBuildRevision", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

