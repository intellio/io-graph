from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ManagedMobileApp(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	mobileAppIdentifier: Optional[MobileAppIdentifier] = Field(default=None,alias="mobileAppIdentifier",)
	version: Optional[str] = Field(default=None,alias="version",)

from .mobile_app_identifier import MobileAppIdentifier

