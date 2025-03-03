from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class LandingPage(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[EmailIdentity] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedBy: Optional[EmailIdentity] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	locale: Optional[str] = Field(default=None,alias="locale",)
	source: Optional[SimulationContentSource] = Field(default=None,alias="source",)
	status: Optional[SimulationContentStatus] = Field(default=None,alias="status",)
	supportedLocales: Optional[list[str]] = Field(default=None,alias="supportedLocales",)
	details: Optional[list[LandingPageDetail]] = Field(default=None,alias="details",)

from .email_identity import EmailIdentity
from .email_identity import EmailIdentity
from .simulation_content_source import SimulationContentSource
from .simulation_content_status import SimulationContentStatus
from .landing_page_detail import LandingPageDetail

