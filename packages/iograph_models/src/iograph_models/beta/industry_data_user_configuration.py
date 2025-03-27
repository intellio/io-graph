from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataUserConfiguration(BaseModel):
	defaultPasswordSettings: Optional[Union[IndustryDataSimplePasswordSettings]] = Field(alias="defaultPasswordSettings", default=None,discriminator="odata_type", )
	licenseSkus: Optional[list[str]] = Field(alias="licenseSkus", default=None,)
	roleGroup: Optional[IndustryDataRoleGroup] = Field(alias="roleGroup", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .industry_data_simple_password_settings import IndustryDataSimplePasswordSettings
from .industry_data_role_group import IndustryDataRoleGroup

