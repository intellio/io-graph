from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NetworkaccessNetworkAccessRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.networkAccessRoot"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.networkAccessRoot")
	alerts: Optional[list[NetworkaccessAlert]] = Field(alias="alerts", default=None,)
	connectivity: Optional[NetworkaccessConnectivity] = Field(alias="connectivity", default=None,)
	filteringPolicies: Optional[list[NetworkaccessFilteringPolicy]] = Field(alias="filteringPolicies", default=None,)
	filteringProfiles: Optional[list[NetworkaccessFilteringProfile]] = Field(alias="filteringProfiles", default=None,)
	forwardingPolicies: Optional[list[NetworkaccessForwardingPolicy]] = Field(alias="forwardingPolicies", default=None,)
	forwardingProfiles: Optional[list[NetworkaccessForwardingProfile]] = Field(alias="forwardingProfiles", default=None,)
	logs: Optional[NetworkaccessLogs] = Field(alias="logs", default=None,)
	reports: Optional[NetworkaccessReports] = Field(alias="reports", default=None,)
	settings: Optional[NetworkaccessSettings] = Field(alias="settings", default=None,)
	tenantStatus: Optional[NetworkaccessTenantStatus] = Field(alias="tenantStatus", default=None,)

from .networkaccess_alert import NetworkaccessAlert
from .networkaccess_connectivity import NetworkaccessConnectivity
from .networkaccess_filtering_policy import NetworkaccessFilteringPolicy
from .networkaccess_filtering_profile import NetworkaccessFilteringProfile
from .networkaccess_forwarding_policy import NetworkaccessForwardingPolicy
from .networkaccess_forwarding_profile import NetworkaccessForwardingProfile
from .networkaccess_logs import NetworkaccessLogs
from .networkaccess_reports import NetworkaccessReports
from .networkaccess_settings import NetworkaccessSettings
from .networkaccess_tenant_status import NetworkaccessTenantStatus
