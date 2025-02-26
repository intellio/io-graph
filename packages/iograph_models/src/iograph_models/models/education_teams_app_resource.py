from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class EducationTeamsAppResource(BaseModel):
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appIconWebUrl: Optional[str] = Field(default=None,alias="appIconWebUrl",)
	appId: Optional[str] = Field(default=None,alias="appId",)
	teamsEmbeddedContentUrl: Optional[str] = Field(default=None,alias="teamsEmbeddedContentUrl",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet

