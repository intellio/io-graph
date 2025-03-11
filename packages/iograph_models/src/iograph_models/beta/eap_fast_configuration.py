from __future__ import annotations
from enum import StrEnum


class EapFastConfiguration(StrEnum):
	noProtectedAccessCredential = "noProtectedAccessCredential"
	useProtectedAccessCredential = "useProtectedAccessCredential"
	useProtectedAccessCredentialAndProvision = "useProtectedAccessCredentialAndProvision"
	useProtectedAccessCredentialAndProvisionAnonymously = "useProtectedAccessCredentialAndProvisionAnonymously"

