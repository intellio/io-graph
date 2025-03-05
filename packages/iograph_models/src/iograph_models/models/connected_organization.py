from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ConnectedOrganization(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	identitySources: SerializeAsAny[Optional[list[IdentitySource]]] = Field(default=None,alias="identitySources",)
	modifiedDateTime: Optional[datetime] = Field(default=None,alias="modifiedDateTime",)
	state: Optional[ConnectedOrganizationState] = Field(default=None,alias="state",)
	externalSponsors: Optional[list[DirectoryObject]] = Field(default=None,alias="externalSponsors",)
	internalSponsors: Optional[list[DirectoryObject]] = Field(default=None,alias="internalSponsors",)

from .identity_source import IdentitySource
from .connected_organization_state import ConnectedOrganizationState
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject

