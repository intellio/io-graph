from __future__ import annotations
from enum import StrEnum


class AwsSecretInformationWebServices(StrEnum):
	secretsManager = "secretsManager"
	certificateAuthority = "certificateAuthority"
	cloudHsm = "cloudHsm"
	certificateManager = "certificateManager"
	unknownFutureValue = "unknownFutureValue"

