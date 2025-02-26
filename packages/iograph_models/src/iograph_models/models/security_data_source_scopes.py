from __future__ import annotations
from enum import Enum


class SecurityDataSourceScopes(Enum):
	none = "none"
	allTenantMailboxes = "allTenantMailboxes"
	allTenantSites = "allTenantSites"
	allCaseCustodians = "allCaseCustodians"
	allCaseNoncustodialDataSources = "allCaseNoncustodialDataSources"
	unknownFutureValue = "unknownFutureValue"

