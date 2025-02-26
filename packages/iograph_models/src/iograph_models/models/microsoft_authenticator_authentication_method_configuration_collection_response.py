from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MicrosoftAuthenticatorAuthenticationMethodConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[MicrosoftAuthenticatorAuthenticationMethodConfiguration] = Field(alias="value",)

from .microsoft_authenticator_authentication_method_configuration import MicrosoftAuthenticatorAuthenticationMethodConfiguration

