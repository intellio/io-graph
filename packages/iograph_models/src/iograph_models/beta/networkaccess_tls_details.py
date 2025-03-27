from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessTlsDetails(BaseModel):
	action: Optional[NetworkaccessTlsAction | str] = Field(alias="action", default=None,)
	policyId: Optional[str] = Field(alias="policyId", default=None,)
	policyName: Optional[str] = Field(alias="policyName", default=None,)
	status: Optional[NetworkaccessTlsStatus | str] = Field(alias="status", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .networkaccess_tls_action import NetworkaccessTlsAction
from .networkaccess_tls_status import NetworkaccessTlsStatus

