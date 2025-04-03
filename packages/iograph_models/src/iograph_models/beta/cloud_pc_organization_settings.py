from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CloudPcOrganizationSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPcOrganizationSettings"] = Field(alias="@odata.type", default="#microsoft.graph.cloudPcOrganizationSettings")
	enableMEMAutoEnroll: Optional[bool] = Field(alias="enableMEMAutoEnroll", default=None,)
	enableSingleSignOn: Optional[bool] = Field(alias="enableSingleSignOn", default=None,)
	osVersion: Optional[CloudPcOperatingSystem | str] = Field(alias="osVersion", default=None,)
	userAccountType: Optional[CloudPcUserAccountType | str] = Field(alias="userAccountType", default=None,)
	windowsSettings: Optional[CloudPcWindowsSettings] = Field(alias="windowsSettings", default=None,)

from .cloud_pc_operating_system import CloudPcOperatingSystem
from .cloud_pc_user_account_type import CloudPcUserAccountType
from .cloud_pc_windows_settings import CloudPcWindowsSettings
