from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicyMigrationReport(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	groupPolicyCreatedDateTime: Optional[datetime] = Field(alias="groupPolicyCreatedDateTime", default=None,)
	groupPolicyLastModifiedDateTime: Optional[datetime] = Field(alias="groupPolicyLastModifiedDateTime", default=None,)
	groupPolicyObjectId: Optional[UUID] = Field(alias="groupPolicyObjectId", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	migrationReadiness: Optional[GroupPolicyMigrationReadiness | str] = Field(alias="migrationReadiness", default=None,)
	ouDistinguishedName: Optional[str] = Field(alias="ouDistinguishedName", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	supportedSettingsCount: Optional[int] = Field(alias="supportedSettingsCount", default=None,)
	supportedSettingsPercent: Optional[int] = Field(alias="supportedSettingsPercent", default=None,)
	targetedInActiveDirectory: Optional[bool] = Field(alias="targetedInActiveDirectory", default=None,)
	totalSettingsCount: Optional[int] = Field(alias="totalSettingsCount", default=None,)
	groupPolicySettingMappings: Optional[list[GroupPolicySettingMapping]] = Field(alias="groupPolicySettingMappings", default=None,)
	unsupportedGroupPolicyExtensions: Optional[list[UnsupportedGroupPolicyExtension]] = Field(alias="unsupportedGroupPolicyExtensions", default=None,)

from .group_policy_migration_readiness import GroupPolicyMigrationReadiness
from .group_policy_setting_mapping import GroupPolicySettingMapping
from .unsupported_group_policy_extension import UnsupportedGroupPolicyExtension

