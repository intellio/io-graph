from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class LoginPage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.loginPage"] = Field(alias="@odata.type",)
	content: Optional[str] = Field(alias="content", default=None,)
	createdBy: Optional[EmailIdentity] = Field(alias="createdBy", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	language: Optional[str] = Field(alias="language", default=None,)
	lastModifiedBy: Optional[EmailIdentity] = Field(alias="lastModifiedBy", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	source: Optional[SimulationContentSource | str] = Field(alias="source", default=None,)
	status: Optional[SimulationContentStatus | str] = Field(alias="status", default=None,)

from .email_identity import EmailIdentity
from .simulation_content_source import SimulationContentSource
from .simulation_content_status import SimulationContentStatus
