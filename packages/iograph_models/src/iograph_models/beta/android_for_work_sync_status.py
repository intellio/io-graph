from __future__ import annotations
from enum import StrEnum


class AndroidForWorkSyncStatus(StrEnum):
	success = "success"
	credentialsNotValid = "credentialsNotValid"
	androidForWorkApiError = "androidForWorkApiError"
	managementServiceError = "managementServiceError"
	unknownError = "unknownError"
	none = "none"

