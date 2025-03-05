from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppConfigurationSettingItem(BaseModel):
	appConfigKey: Optional[str] = Field(alias="appConfigKey",default=None,)
	appConfigKeyType: Optional[str | MdmAppConfigKeyType] = Field(alias="appConfigKeyType",default=None,)
	appConfigKeyValue: Optional[str] = Field(alias="appConfigKeyValue",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .mdm_app_config_key_type import MdmAppConfigKeyType

