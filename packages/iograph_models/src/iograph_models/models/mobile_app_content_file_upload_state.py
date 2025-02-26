from __future__ import annotations
from enum import Enum


class MobileAppContentFileUploadState(Enum):
	success = "success"
	transientError = "transientError"
	error = "error"
	unknown = "unknown"
	azureStorageUriRequestSuccess = "azureStorageUriRequestSuccess"
	azureStorageUriRequestPending = "azureStorageUriRequestPending"
	azureStorageUriRequestFailed = "azureStorageUriRequestFailed"
	azureStorageUriRequestTimedOut = "azureStorageUriRequestTimedOut"
	azureStorageUriRenewalSuccess = "azureStorageUriRenewalSuccess"
	azureStorageUriRenewalPending = "azureStorageUriRenewalPending"
	azureStorageUriRenewalFailed = "azureStorageUriRenewalFailed"
	azureStorageUriRenewalTimedOut = "azureStorageUriRenewalTimedOut"
	commitFileSuccess = "commitFileSuccess"
	commitFilePending = "commitFilePending"
	commitFileFailed = "commitFileFailed"
	commitFileTimedOut = "commitFileTimedOut"

