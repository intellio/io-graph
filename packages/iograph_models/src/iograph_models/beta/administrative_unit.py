from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AdministrativeUnit(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isMemberManagementRestricted: Optional[bool] = Field(alias="isMemberManagementRestricted",default=None,)
	membershipRule: Optional[str] = Field(alias="membershipRule",default=None,)
	membershipRuleProcessingState: Optional[str] = Field(alias="membershipRuleProcessingState",default=None,)
	membershipType: Optional[str] = Field(alias="membershipType",default=None,)
	visibility: Optional[str] = Field(alias="visibility",default=None,)
	deletedMembers: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="deletedMembers",default=None,)
	extensions: SerializeAsAny[Optional[list[Extension]]] = Field(alias="extensions",default=None,)
	members: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="members",default=None,)
	scopedRoleMembers: Optional[list[ScopedRoleMembership]] = Field(alias="scopedRoleMembers",default=None,)

from .directory_object import DirectoryObject
from .extension import Extension
from .directory_object import DirectoryObject
from .scoped_role_membership import ScopedRoleMembership

