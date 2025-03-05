from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AdministrativeUnit(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isMemberManagementRestricted: Optional[bool] = Field(default=None,alias="isMemberManagementRestricted",)
	membershipRule: Optional[str] = Field(default=None,alias="membershipRule",)
	membershipRuleProcessingState: Optional[str] = Field(default=None,alias="membershipRuleProcessingState",)
	membershipType: Optional[str] = Field(default=None,alias="membershipType",)
	visibility: Optional[str] = Field(default=None,alias="visibility",)
	extensions: SerializeAsAny[Optional[list[Extension]]] = Field(default=None,alias="extensions",)
	members: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(default=None,alias="members",)
	scopedRoleMembers: Optional[list[ScopedRoleMembership]] = Field(default=None,alias="scopedRoleMembers",)

from .extension import Extension
from .directory_object import DirectoryObject
from .scoped_role_membership import ScopedRoleMembership

