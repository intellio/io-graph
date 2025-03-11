from __future__ import annotations
from enum import StrEnum


class CertificateIssuanceStates(StrEnum):
	unknown = "unknown"
	challengeIssued = "challengeIssued"
	challengeIssueFailed = "challengeIssueFailed"
	requestCreationFailed = "requestCreationFailed"
	requestSubmitFailed = "requestSubmitFailed"
	challengeValidationSucceeded = "challengeValidationSucceeded"
	challengeValidationFailed = "challengeValidationFailed"
	issueFailed = "issueFailed"
	issuePending = "issuePending"
	issued = "issued"
	responseProcessingFailed = "responseProcessingFailed"
	responsePending = "responsePending"
	enrollmentSucceeded = "enrollmentSucceeded"
	enrollmentNotNeeded = "enrollmentNotNeeded"
	revoked = "revoked"
	removedFromCollection = "removedFromCollection"
	renewVerified = "renewVerified"
	installFailed = "installFailed"
	installed = "installed"
	deleteFailed = "deleteFailed"
	deleted = "deleted"
	renewalRequested = "renewalRequested"
	requested = "requested"

