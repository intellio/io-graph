from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CompanyPortalBlockedAction(BaseModel):
	action: Optional[CompanyPortalAction | str] = Field(alias="action", default=None,)
	ownerType: Optional[OwnerType | str] = Field(alias="ownerType", default=None,)
	platform: Optional[DevicePlatformType | str] = Field(alias="platform", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .company_portal_action import CompanyPortalAction
from .owner_type import OwnerType
from .device_platform_type import DevicePlatformType
