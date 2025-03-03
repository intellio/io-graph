from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AppManagementServicePrincipalConfiguration(BaseModel):
	keyCredentials: Optional[list[KeyCredentialConfiguration]] = Field(default=None,alias="keyCredentials",)
	passwordCredentials: Optional[list[PasswordCredentialConfiguration]] = Field(default=None,alias="passwordCredentials",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .key_credential_configuration import KeyCredentialConfiguration
from .password_credential_configuration import PasswordCredentialConfiguration

