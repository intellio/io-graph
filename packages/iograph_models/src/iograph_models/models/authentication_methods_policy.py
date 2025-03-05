from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AuthenticationMethodsPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	policyMigrationState: Optional[str | AuthenticationMethodsPolicyMigrationState] = Field(alias="policyMigrationState",default=None,)
	policyVersion: Optional[str] = Field(alias="policyVersion",default=None,)
	reconfirmationInDays: Optional[int] = Field(alias="reconfirmationInDays",default=None,)
	registrationEnforcement: Optional[RegistrationEnforcement] = Field(alias="registrationEnforcement",default=None,)
	authenticationMethodConfigurations: SerializeAsAny[Optional[list[AuthenticationMethodConfiguration]]] = Field(alias="authenticationMethodConfigurations",default=None,)

from .authentication_methods_policy_migration_state import AuthenticationMethodsPolicyMigrationState
from .registration_enforcement import RegistrationEnforcement
from .authentication_method_configuration import AuthenticationMethodConfiguration

