from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudAppSecuritySessionControl(BaseModel):
	isEnabled: Optional[bool] = Field(alias="isEnabled",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	cloudAppSecurityType: Optional[CloudAppSecuritySessionControlType | str] = Field(alias="cloudAppSecurityType",default=None,)

from .cloud_app_security_session_control_type import CloudAppSecuritySessionControlType

