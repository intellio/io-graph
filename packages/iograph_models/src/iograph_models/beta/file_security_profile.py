from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class FileSecurityProfile(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.fileSecurityProfile"] = Field(alias="@odata.type", default="#microsoft.graph.fileSecurityProfile")
	activityGroupNames: Optional[list[str]] = Field(alias="activityGroupNames", default=None,)
	azureSubscriptionId: Optional[str] = Field(alias="azureSubscriptionId", default=None,)
	azureTenantId: Optional[str] = Field(alias="azureTenantId", default=None,)
	certificateThumbprint: Optional[str] = Field(alias="certificateThumbprint", default=None,)
	extensions: Optional[list[str]] = Field(alias="extensions", default=None,)
	fileType: Optional[str] = Field(alias="fileType", default=None,)
	firstSeenDateTime: Optional[datetime] = Field(alias="firstSeenDateTime", default=None,)
	hashes: Optional[list[FileHash]] = Field(alias="hashes", default=None,)
	lastSeenDateTime: Optional[datetime] = Field(alias="lastSeenDateTime", default=None,)
	malwareStates: Optional[list[MalwareState]] = Field(alias="malwareStates", default=None,)
	names: Optional[list[str]] = Field(alias="names", default=None,)
	riskScore: Optional[str] = Field(alias="riskScore", default=None,)
	size: Optional[int] = Field(alias="size", default=None,)
	tags: Optional[list[str]] = Field(alias="tags", default=None,)
	vendorInformation: Optional[SecurityVendorInformation] = Field(alias="vendorInformation", default=None,)
	vulnerabilityStates: Optional[list[VulnerabilityState]] = Field(alias="vulnerabilityStates", default=None,)

from .file_hash import FileHash
from .malware_state import MalwareState
from .security_vendor_information import SecurityVendorInformation
from .vulnerability_state import VulnerabilityState
