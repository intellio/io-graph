from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppConfigurationSettingItem(BaseModel):
	appConfigKey: Optional[str] = Field(default=None,alias="appConfigKey",)
	appConfigKeyType: Optional[MdmAppConfigKeyType] = Field(default=None,alias="appConfigKeyType",)
	appConfigKeyValue: Optional[str] = Field(default=None,alias="appConfigKeyValue",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .mdm_app_config_key_type import MdmAppConfigKeyType

