from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ConnectedOrganization(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: Optional[str] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	identitySources: SerializeAsAny[Optional[list[IdentitySource]]] = Field(alias="identitySources",default=None,)
	modifiedBy: Optional[str] = Field(alias="modifiedBy",default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime",default=None,)
	state: Optional[ConnectedOrganizationState | str] = Field(alias="state",default=None,)
	externalSponsors: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="externalSponsors",default=None,)
	internalSponsors: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="internalSponsors",default=None,)

from .identity_source import IdentitySource
from .connected_organization_state import ConnectedOrganizationState
from .directory_object import DirectoryObject
from .directory_object import DirectoryObject

