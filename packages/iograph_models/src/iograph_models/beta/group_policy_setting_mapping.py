from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GroupPolicySettingMapping(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	admxSettingDefinitionId: Optional[str] = Field(alias="admxSettingDefinitionId", default=None,)
	childIdList: Optional[list[str]] = Field(alias="childIdList", default=None,)
	intuneSettingDefinitionId: Optional[str] = Field(alias="intuneSettingDefinitionId", default=None,)
	intuneSettingUriList: Optional[list[str]] = Field(alias="intuneSettingUriList", default=None,)
	isMdmSupported: Optional[bool] = Field(alias="isMdmSupported", default=None,)
	mdmCspName: Optional[str] = Field(alias="mdmCspName", default=None,)
	mdmMinimumOSVersion: Optional[int] = Field(alias="mdmMinimumOSVersion", default=None,)
	mdmSettingUri: Optional[str] = Field(alias="mdmSettingUri", default=None,)
	mdmSupportedState: Optional[MdmSupportedState | str] = Field(alias="mdmSupportedState", default=None,)
	parentId: Optional[str] = Field(alias="parentId", default=None,)
	settingCategory: Optional[str] = Field(alias="settingCategory", default=None,)
	settingDisplayName: Optional[str] = Field(alias="settingDisplayName", default=None,)
	settingDisplayValue: Optional[str] = Field(alias="settingDisplayValue", default=None,)
	settingDisplayValueType: Optional[str] = Field(alias="settingDisplayValueType", default=None,)
	settingName: Optional[str] = Field(alias="settingName", default=None,)
	settingScope: Optional[GroupPolicySettingScope | str] = Field(alias="settingScope", default=None,)
	settingType: Optional[GroupPolicySettingType | str] = Field(alias="settingType", default=None,)
	settingValue: Optional[str] = Field(alias="settingValue", default=None,)
	settingValueDisplayUnits: Optional[str] = Field(alias="settingValueDisplayUnits", default=None,)
	settingValueType: Optional[str] = Field(alias="settingValueType", default=None,)

from .mdm_supported_state import MdmSupportedState
from .group_policy_setting_scope import GroupPolicySettingScope
from .group_policy_setting_type import GroupPolicySettingType

