from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySensorDeploymentPackage(BaseModel):
	downloadUrl: Optional[str] = Field(alias="downloadUrl", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


