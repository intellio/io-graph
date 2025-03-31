from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationAppPolicyDetailsCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AuthenticationAppPolicyDetails]] = Field(alias="value", default=None,)

from .authentication_app_policy_details import AuthenticationAppPolicyDetails
