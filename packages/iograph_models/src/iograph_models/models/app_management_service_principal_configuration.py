from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AppManagementServicePrincipalConfiguration(BaseModel):
	keyCredentials: list[KeyCredentialConfiguration] = Field(alias="keyCredentials",)
	passwordCredentials: list[PasswordCredentialConfiguration] = Field(alias="passwordCredentials",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .key_credential_configuration import KeyCredentialConfiguration
from .password_credential_configuration import PasswordCredentialConfiguration

