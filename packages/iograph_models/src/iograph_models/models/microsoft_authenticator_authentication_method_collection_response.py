from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MicrosoftAuthenticatorAuthenticationMethodCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[MicrosoftAuthenticatorAuthenticationMethod] = Field(alias="value",)

from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod

