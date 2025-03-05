from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Permission(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime",default=None,)
	grantedTo: SerializeAsAny[Optional[IdentitySet]] = Field(alias="grantedTo",default=None,)
	grantedToIdentities: SerializeAsAny[Optional[list[IdentitySet]]] = Field(alias="grantedToIdentities",default=None,)
	grantedToIdentitiesV2: Optional[list[SharePointIdentitySet]] = Field(alias="grantedToIdentitiesV2",default=None,)
	grantedToV2: Optional[SharePointIdentitySet] = Field(alias="grantedToV2",default=None,)
	hasPassword: Optional[bool] = Field(alias="hasPassword",default=None,)
	inheritedFrom: Optional[ItemReference] = Field(alias="inheritedFrom",default=None,)
	invitation: Optional[SharingInvitation] = Field(alias="invitation",default=None,)
	link: Optional[SharingLink] = Field(alias="link",default=None,)
	roles: Optional[list[str]] = Field(alias="roles",default=None,)
	shareId: Optional[str] = Field(alias="shareId",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .item_reference import ItemReference
from .sharing_invitation import SharingInvitation
from .sharing_link import SharingLink

