from __future__ import annotations
from enum import StrEnum


class AuthenticationEventType(StrEnum):
	tokenIssuanceStart = "tokenIssuanceStart"
	pageRenderStart = "pageRenderStart"
	unknownFutureValue = "unknownFutureValue"
	attributeCollectionStart = "attributeCollectionStart"
	attributeCollectionSubmit = "attributeCollectionSubmit"
	emailOtpSend = "emailOtpSend"

