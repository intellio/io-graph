from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudAppSecurityProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CloudAppSecurityProfile]] = Field(alias="value", default=None,)

from .cloud_app_security_profile import CloudAppSecurityProfile
