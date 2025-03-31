from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CloudAppSecuritySessionControl(BaseModel):
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	odata_type: Literal["#microsoft.graph.cloudAppSecuritySessionControl"] = Field(alias="@odata.type", default="#microsoft.graph.cloudAppSecuritySessionControl")
	cloudAppSecurityType: Optional[CloudAppSecuritySessionControlType | str] = Field(alias="cloudAppSecurityType", default=None,)

from .cloud_app_security_session_control_type import CloudAppSecuritySessionControlType
