from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Permission(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	grantedTo: Optional[IdentitySet] = Field(default=None,alias="grantedTo",)
	grantedToIdentities: list[IdentitySet] = Field(alias="grantedToIdentities",)
	grantedToIdentitiesV2: list[SharePointIdentitySet] = Field(alias="grantedToIdentitiesV2",)
	grantedToV2: Optional[SharePointIdentitySet] = Field(default=None,alias="grantedToV2",)
	hasPassword: Optional[bool] = Field(default=None,alias="hasPassword",)
	inheritedFrom: Optional[ItemReference] = Field(default=None,alias="inheritedFrom",)
	invitation: Optional[SharingInvitation] = Field(default=None,alias="invitation",)
	link: Optional[SharingLink] = Field(default=None,alias="link",)
	roles: list[Optional[str]] = Field(alias="roles",)
	shareId: Optional[str] = Field(default=None,alias="shareId",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .item_reference import ItemReference
from .sharing_invitation import SharingInvitation
from .sharing_link import SharingLink

