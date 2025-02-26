from __future__ import annotations
from enum import Enum


class X509CertificateCRLValidationConfigurationState(Enum):
	disabled = "disabled"
	enabled = "enabled"
	unknownFutureValue = "unknownFutureValue"

