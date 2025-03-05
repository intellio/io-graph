from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationMethodsPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	policyMigrationState: Optional[AuthenticationMethodsPolicyMigrationState] = Field(default=None,alias="policyMigrationState",)
	policyVersion: Optional[str] = Field(default=None,alias="policyVersion",)
	reconfirmationInDays: Optional[int] = Field(default=None,alias="reconfirmationInDays",)
	registrationEnforcement: Optional[RegistrationEnforcement] = Field(default=None,alias="registrationEnforcement",)
	authenticationMethodConfigurations: SerializeAsAny[Optional[list[AuthenticationMethodConfiguration]]] = Field(default=None,alias="authenticationMethodConfigurations",)

from .authentication_methods_policy_migration_state import AuthenticationMethodsPolicyMigrationState
from .registration_enforcement import RegistrationEnforcement
from .authentication_method_configuration import AuthenticationMethodConfiguration

