from __future__ import annotations
from enum import StrEnum


class EdiscoveryDataSourceScopes(StrEnum):
	none = "none"
	allTenantMailboxes = "allTenantMailboxes"
	allTenantSites = "allTenantSites"
	allCaseCustodians = "allCaseCustodians"
	allCaseNoncustodialDataSources = "allCaseNoncustodialDataSources"
	unknownFutureValue = "unknownFutureValue"

