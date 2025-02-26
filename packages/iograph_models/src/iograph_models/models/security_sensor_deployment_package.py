from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecuritySensorDeploymentPackage(BaseModel):
	downloadUrl: Optional[str] = Field(default=None,alias="downloadUrl",)
	version: Optional[str] = Field(default=None,alias="version",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


