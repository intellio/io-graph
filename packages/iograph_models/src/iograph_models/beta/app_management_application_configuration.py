from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AppManagementApplicationConfiguration(BaseModel):
	keyCredentials: Optional[list[KeyCredentialConfiguration]] = Field(alias="keyCredentials", default=None,)
	passwordCredentials: Optional[list[PasswordCredentialConfiguration]] = Field(alias="passwordCredentials", default=None,)
	odata_type: Literal["#microsoft.graph.appManagementApplicationConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.appManagementApplicationConfiguration")
	identifierUris: Optional[IdentifierUriConfiguration] = Field(alias="identifierUris", default=None,)

from .key_credential_configuration import KeyCredentialConfiguration
from .password_credential_configuration import PasswordCredentialConfiguration
from .identifier_uri_configuration import IdentifierUriConfiguration
