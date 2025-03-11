from __future__ import annotations
from enum import StrEnum


class X509CertificateCRLValidationConfigurationState(StrEnum):
	disabled = "disabled"
	enabled = "enabled"
	unknownFutureValue = "unknownFutureValue"

