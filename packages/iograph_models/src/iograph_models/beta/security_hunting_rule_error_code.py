from __future__ import annotations
from enum import StrEnum


class SecurityHuntingRuleErrorCode(StrEnum):
	queryExecutionFailed = "queryExecutionFailed"
	queryExecutionThrottling = "queryExecutionThrottling"
	queryExceededResultSize = "queryExceededResultSize"
	queryLimitsExceeded = "queryLimitsExceeded"
	queryTimeout = "queryTimeout"
	alertCreationFailed = "alertCreationFailed"
	alertReportNotFound = "alertReportNotFound"
	partialRowsFailed = "partialRowsFailed"
	unknownFutureValue = "unknownFutureValue"
	noImpactedEntity = "noImpactedEntity"

