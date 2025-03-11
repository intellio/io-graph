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
	microsoftAuthenticatorPlatformSettings: Optional[MicrosoftAuthenticatorPlatformSettings] = Field(alias="microsoftAuthenticatorPlatformSettings",default=None,)
	policyMigrationState: Optional[AuthenticationMethodsPolicyMigrationState | str] = Field(alias="policyMigrationState",default=None,)
	policyVersion: Optional[str] = Field(alias="policyVersion",default=None,)
	reconfirmationInDays: Optional[int] = Field(alias="reconfirmationInDays",default=None,)
	registrationEnforcement: Optional[RegistrationEnforcement] = Field(alias="registrationEnforcement",default=None,)
	reportSuspiciousActivitySettings: Optional[ReportSuspiciousActivitySettings] = Field(alias="reportSuspiciousActivitySettings",default=None,)
	systemCredentialPreferences: Optional[SystemCredentialPreferences] = Field(alias="systemCredentialPreferences",default=None,)
	authenticationMethodConfigurations: SerializeAsAny[Optional[list[AuthenticationMethodConfiguration]]] = Field(alias="authenticationMethodConfigurations",default=None,)

from .microsoft_authenticator_platform_settings import MicrosoftAuthenticatorPlatformSettings
from .authentication_methods_policy_migration_state import AuthenticationMethodsPolicyMigrationState
from .registration_enforcement import RegistrationEnforcement
from .report_suspicious_activity_settings import ReportSuspiciousActivitySettings
from .system_credential_preferences import SystemCredentialPreferences
from .authentication_method_configuration import AuthenticationMethodConfiguration

