from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DeviceManagementConfigurationPolicyTemplateReference(BaseModel):
	templateDisplayName: Optional[str] = Field(alias="templateDisplayName", default=None,)
	templateDisplayVersion: Optional[str] = Field(alias="templateDisplayVersion", default=None,)
	templateFamily: Optional[DeviceManagementConfigurationTemplateFamily | str] = Field(alias="templateFamily", default=None,)
	templateId: Optional[str] = Field(alias="templateId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .device_management_configuration_template_family import DeviceManagementConfigurationTemplateFamily
