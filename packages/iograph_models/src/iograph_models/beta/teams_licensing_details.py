from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class TeamsLicensingDetails(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.teamsLicensingDetails"] = Field(alias="@odata.type",)
	hasTeamsLicense: Optional[bool] = Field(alias="hasTeamsLicense", default=None,)

