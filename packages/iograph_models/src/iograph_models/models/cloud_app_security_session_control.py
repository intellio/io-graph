from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudAppSecuritySessionControl(BaseModel):
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	cloudAppSecurityType: Optional[CloudAppSecuritySessionControlType] = Field(default=None,alias="cloudAppSecurityType",)

from .cloud_app_security_session_control_type import CloudAppSecuritySessionControlType

