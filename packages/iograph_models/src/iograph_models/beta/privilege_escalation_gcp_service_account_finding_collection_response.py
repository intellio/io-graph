from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PrivilegeEscalationGcpServiceAccountFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[PrivilegeEscalationGcpServiceAccountFinding]] = Field(alias="value",default=None,)

from .privilege_escalation_gcp_service_account_finding import PrivilegeEscalationGcpServiceAccountFinding

