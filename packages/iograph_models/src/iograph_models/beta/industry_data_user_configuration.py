from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataUserConfiguration(BaseModel):
	defaultPasswordSettings: SerializeAsAny[Optional[IndustryDataPasswordSettings]] = Field(alias="defaultPasswordSettings",default=None,)
	licenseSkus: Optional[list[str]] = Field(alias="licenseSkus",default=None,)
	roleGroup: Optional[IndustryDataRoleGroup] = Field(alias="roleGroup",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .industry_data_password_settings import IndustryDataPasswordSettings
from .industry_data_role_group import IndustryDataRoleGroup

