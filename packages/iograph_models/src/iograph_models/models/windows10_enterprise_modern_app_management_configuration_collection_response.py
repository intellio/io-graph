from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows10EnterpriseModernAppManagementConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[Windows10EnterpriseModernAppManagementConfiguration] = Field(alias="value",)

from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration

