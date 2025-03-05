from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class LandingPage(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: Optional[EmailIdentity] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedBy: Optional[EmailIdentity] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	locale: Optional[str] = Field(alias="locale",default=None,)
	source: Optional[str | SimulationContentSource] = Field(alias="source",default=None,)
	status: Optional[str | SimulationContentStatus] = Field(alias="status",default=None,)
	supportedLocales: Optional[list[str]] = Field(alias="supportedLocales",default=None,)
	details: Optional[list[LandingPageDetail]] = Field(alias="details",default=None,)

from .email_identity import EmailIdentity
from .email_identity import EmailIdentity
from .simulation_content_source import SimulationContentSource
from .simulation_content_status import SimulationContentStatus
from .landing_page_detail import LandingPageDetail

