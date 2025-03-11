from __future__ import annotations
from enum import StrEnum


class SignUpStage(StrEnum):
	credentialCollection = "credentialCollection"
	credentialValidation = "credentialValidation"
	credentialFederation = "credentialFederation"
	consent = "consent"
	attributeCollectionAndValidation = "attributeCollectionAndValidation"
	userCreation = "userCreation"
	tenantConsent = "tenantConsent"
	unknownFutureValue = "unknownFutureValue"

