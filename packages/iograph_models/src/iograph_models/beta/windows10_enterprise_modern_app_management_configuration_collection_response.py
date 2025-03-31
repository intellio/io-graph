from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows10EnterpriseModernAppManagementConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Windows10EnterpriseModernAppManagementConfiguration]] = Field(alias="value", default=None,)

from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration
