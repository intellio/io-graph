from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserCredentialUsageDetailsCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[UserCredentialUsageDetails]] = Field(alias="value", default=None,)

from .user_credential_usage_details import UserCredentialUsageDetails
