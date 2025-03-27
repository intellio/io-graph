from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityBaselineTemplate(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.securityBaselineTemplate"] = Field(alias="@odata.type", default="#microsoft.graph.securityBaselineTemplate")
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	intentCount: Optional[int] = Field(alias="intentCount", default=None,)
	isDeprecated: Optional[bool] = Field(alias="isDeprecated", default=None,)
	platformType: Optional[PolicyPlatformType | str] = Field(alias="platformType", default=None,)
	publishedDateTime: Optional[datetime] = Field(alias="publishedDateTime", default=None,)
	templateSubtype: Optional[DeviceManagementTemplateSubtype | str] = Field(alias="templateSubtype", default=None,)
	templateType: Optional[DeviceManagementTemplateType | str] = Field(alias="templateType", default=None,)
	versionInfo: Optional[str] = Field(alias="versionInfo", default=None,)
	categories: Optional[list[DeviceManagementTemplateSettingCategory]] = Field(alias="categories", default=None,)
	migratableTo: Optional[list[Annotated[Union[SecurityBaselineTemplate],Field(discriminator="odata_type")]]] = Field(alias="migratableTo", default=None,)
	settings: Optional[list[Annotated[Union[DeviceManagementAbstractComplexSettingInstance, DeviceManagementBooleanSettingInstance, DeviceManagementCollectionSettingInstance, DeviceManagementComplexSettingInstance, DeviceManagementIntegerSettingInstance, DeviceManagementStringSettingInstance],Field(discriminator="odata_type")]]] = Field(alias="settings", default=None,)
	categoryDeviceStateSummaries: Optional[list[SecurityBaselineCategoryStateSummary]] = Field(alias="categoryDeviceStateSummaries", default=None,)
	deviceStates: Optional[list[SecurityBaselineDeviceState]] = Field(alias="deviceStates", default=None,)
	deviceStateSummary: Optional[Union[SecurityBaselineCategoryStateSummary]] = Field(alias="deviceStateSummary", default=None,discriminator="odata_type", )

from .policy_platform_type import PolicyPlatformType
from .device_management_template_subtype import DeviceManagementTemplateSubtype
from .device_management_template_type import DeviceManagementTemplateType
from .device_management_template_setting_category import DeviceManagementTemplateSettingCategory
from .device_management_abstract_complex_setting_instance import DeviceManagementAbstractComplexSettingInstance
from .device_management_boolean_setting_instance import DeviceManagementBooleanSettingInstance
from .device_management_collection_setting_instance import DeviceManagementCollectionSettingInstance
from .device_management_complex_setting_instance import DeviceManagementComplexSettingInstance
from .device_management_integer_setting_instance import DeviceManagementIntegerSettingInstance
from .device_management_string_setting_instance import DeviceManagementStringSettingInstance
from .security_baseline_category_state_summary import SecurityBaselineCategoryStateSummary
from .security_baseline_device_state import SecurityBaselineDeviceState
from .security_baseline_category_state_summary import SecurityBaselineCategoryStateSummary

