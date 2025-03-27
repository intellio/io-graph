from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceManagementSettingCategoryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[DeviceManagementIntentSettingCategory, DeviceManagementTemplateSettingCategory]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .device_management_intent_setting_category import DeviceManagementIntentSettingCategory
from .device_management_template_setting_category import DeviceManagementTemplateSettingCategory

