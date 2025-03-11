from __future__ import annotations
from enum import StrEnum


class EnrollmentNotificationTemplateType(StrEnum):
	email = "email"
	push = "push"
	unknownFutureValue = "unknownFutureValue"

