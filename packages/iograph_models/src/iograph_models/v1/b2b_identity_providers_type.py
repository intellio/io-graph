from __future__ import annotations
from enum import StrEnum


class B2bIdentityProvidersType(StrEnum):
	azureActiveDirectory = "azureActiveDirectory"
	externalFederation = "externalFederation"
	socialIdentityProviders = "socialIdentityProviders"
	emailOneTimePasscode = "emailOneTimePasscode"
	microsoftAccount = "microsoftAccount"
	defaultConfiguredIdp = "defaultConfiguredIdp"
	unknownFutureValue = "unknownFutureValue"

