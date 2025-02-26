from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ConnectedOrganization(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	identitySources: list[IdentitySource] = Field(alias="identitySources",)
	modifiedDateTime: Optional[datetime] = Field(default=None,alias="modifiedDateTime",)
	state: Optional[ConnectedOrganizationState] = Field(default=None,alias="state",)
	externalSponsors: list[DirectoryObject] = Field(alias="externalSponsors",)
	internalSponsors: list[DirectoryObject] = Field(alias="internalSponsors",)

from .identity_source import IdentitySource
from .connected_organization_state import ConnectedOrganizationState
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject

