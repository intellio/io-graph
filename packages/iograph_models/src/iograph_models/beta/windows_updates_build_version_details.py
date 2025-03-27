from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesBuildVersionDetails(BaseModel):
	buildNumber: Optional[int] = Field(alias="buildNumber", default=None,)
	majorVersion: Optional[int] = Field(alias="majorVersion", default=None,)
	minorVersion: Optional[int] = Field(alias="minorVersion", default=None,)
	updateBuildRevision: Optional[int] = Field(alias="updateBuildRevision", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


