from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationTeamsAppResource(BaseModel):
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appIconWebUrl: Optional[str] = Field(alias="appIconWebUrl",default=None,)
	appId: Optional[str] = Field(alias="appId",default=None,)
	teamsEmbeddedContentUrl: Optional[str] = Field(alias="teamsEmbeddedContentUrl",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet

