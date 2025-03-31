from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class InvalidLicenseAlertIncident(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.invalidLicenseAlertIncident"] = Field(alias="@odata.type", default="#microsoft.graph.invalidLicenseAlertIncident")
	tenantLicenseStatus: Optional[str] = Field(alias="tenantLicenseStatus", default=None,)

