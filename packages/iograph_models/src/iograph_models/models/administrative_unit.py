from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


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
	extensions: list[Extension] = Field(alias="extensions",)
	members: list[DirectoryObject] = Field(alias="members",)
	scopedRoleMembers: list[ScopedRoleMembership] = Field(alias="scopedRoleMembers",)

from .extension import Extension
from .directory_object import DirectoryObject
from .scoped_role_membership import ScopedRoleMembership

