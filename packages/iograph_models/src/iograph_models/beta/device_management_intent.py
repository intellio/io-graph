from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementIntent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isAssigned: Optional[bool] = Field(alias="isAssigned", default=None,)
	isMigratingToConfigurationPolicy: Optional[bool] = Field(alias="isMigratingToConfigurationPolicy", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	templateId: Optional[str] = Field(alias="templateId", default=None,)
	assignments: Optional[list[DeviceManagementIntentAssignment]] = Field(alias="assignments", default=None,)
	categories: Optional[list[DeviceManagementIntentSettingCategory]] = Field(alias="categories", default=None,)
	deviceSettingStateSummaries: Optional[list[DeviceManagementIntentDeviceSettingStateSummary]] = Field(alias="deviceSettingStateSummaries", default=None,)
	deviceStates: Optional[list[DeviceManagementIntentDeviceState]] = Field(alias="deviceStates", default=None,)
	deviceStateSummary: Optional[DeviceManagementIntentDeviceStateSummary] = Field(alias="deviceStateSummary", default=None,)
	settings: Optional[list[Annotated[Union[DeviceManagementAbstractComplexSettingInstance, DeviceManagementBooleanSettingInstance, DeviceManagementCollectionSettingInstance, DeviceManagementComplexSettingInstance, DeviceManagementIntegerSettingInstance, DeviceManagementStringSettingInstance]],Field(discriminator="odata_type")]]] = Field(alias="settings", default=None,)
	userStates: Optional[list[DeviceManagementIntentUserState]] = Field(alias="userStates", default=None,)
	userStateSummary: Optional[DeviceManagementIntentUserStateSummary] = Field(alias="userStateSummary", default=None,)

from .device_management_intent_assignment import DeviceManagementIntentAssignment
from .device_management_intent_setting_category import DeviceManagementIntentSettingCategory
from .device_management_intent_device_setting_state_summary import DeviceManagementIntentDeviceSettingStateSummary
from .device_management_intent_device_state import DeviceManagementIntentDeviceState
from .device_management_intent_device_state_summary import DeviceManagementIntentDeviceStateSummary
from .device_management_abstract_complex_setting_instance import DeviceManagementAbstractComplexSettingInstance
from .device_management_boolean_setting_instance import DeviceManagementBooleanSettingInstance
from .device_management_collection_setting_instance import DeviceManagementCollectionSettingInstance
from .device_management_complex_setting_instance import DeviceManagementComplexSettingInstance
from .device_management_integer_setting_instance import DeviceManagementIntegerSettingInstance
from .device_management_string_setting_instance import DeviceManagementStringSettingInstance
from .device_management_intent_user_state import DeviceManagementIntentUserState
from .device_management_intent_user_state_summary import DeviceManagementIntentUserStateSummary

