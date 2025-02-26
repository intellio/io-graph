from __future__ import annotations
from enum import Enum


class B2bIdentityProvidersType(Enum):
	azureActiveDirectory = "azureActiveDirectory"
	externalFederation = "externalFederation"
	socialIdentityProviders = "socialIdentityProviders"
	emailOneTimePasscode = "emailOneTimePasscode"
	microsoftAccount = "microsoftAccount"
	defaultConfiguredIdp = "defaultConfiguredIdp"
	unknownFutureValue = "unknownFutureValue"

