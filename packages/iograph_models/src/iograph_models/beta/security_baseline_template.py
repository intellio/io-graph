from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityBaselineTemplate(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	intentCount: Optional[int] = Field(alias="intentCount",default=None,)
	isDeprecated: Optional[bool] = Field(alias="isDeprecated",default=None,)
	platformType: Optional[PolicyPlatformType | str] = Field(alias="platformType",default=None,)
	publishedDateTime: Optional[datetime] = Field(alias="publishedDateTime",default=None,)
	templateSubtype: Optional[DeviceManagementTemplateSubtype | str] = Field(alias="templateSubtype",default=None,)
	templateType: Optional[DeviceManagementTemplateType | str] = Field(alias="templateType",default=None,)
	versionInfo: Optional[str] = Field(alias="versionInfo",default=None,)
	categories: Optional[list[DeviceManagementTemplateSettingCategory]] = Field(alias="categories",default=None,)
	migratableTo: SerializeAsAny[Optional[list[DeviceManagementTemplate]]] = Field(alias="migratableTo",default=None,)
	settings: SerializeAsAny[Optional[list[DeviceManagementSettingInstance]]] = Field(alias="settings",default=None,)
	categoryDeviceStateSummaries: Optional[list[SecurityBaselineCategoryStateSummary]] = Field(alias="categoryDeviceStateSummaries",default=None,)
	deviceStates: Optional[list[SecurityBaselineDeviceState]] = Field(alias="deviceStates",default=None,)
	deviceStateSummary: SerializeAsAny[Optional[SecurityBaselineStateSummary]] = Field(alias="deviceStateSummary",default=None,)

from .policy_platform_type import PolicyPlatformType
from .device_management_template_subtype import DeviceManagementTemplateSubtype
from .device_management_template_type import DeviceManagementTemplateType
from .device_management_template_setting_category import DeviceManagementTemplateSettingCategory
from .device_management_template import DeviceManagementTemplate
from .device_management_setting_instance import DeviceManagementSettingInstance
from .security_baseline_category_state_summary import SecurityBaselineCategoryStateSummary
from .security_baseline_device_state import SecurityBaselineDeviceState
from .security_baseline_state_summary import SecurityBaselineStateSummary

