from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityAction(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.securityAction"] = Field(alias="@odata.type", default="#microsoft.graph.securityAction")
	actionReason: Optional[str] = Field(alias="actionReason", default=None,)
	appId: Optional[str] = Field(alias="appId", default=None,)
	azureTenantId: Optional[str] = Field(alias="azureTenantId", default=None,)
	clientContext: Optional[str] = Field(alias="clientContext", default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	errorInfo: Optional[ResultInfo] = Field(alias="errorInfo", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	parameters: Optional[list[KeyValuePair]] = Field(alias="parameters", default=None,)
	states: Optional[list[SecurityActionState]] = Field(alias="states", default=None,)
	status: Optional[OperationStatus | str] = Field(alias="status", default=None,)
	user: Optional[str] = Field(alias="user", default=None,)
	vendorInformation: Optional[SecurityVendorInformation] = Field(alias="vendorInformation", default=None,)

from .result_info import ResultInfo
from .key_value_pair import KeyValuePair
from .security_action_state import SecurityActionState
from .operation_status import OperationStatus
from .security_vendor_information import SecurityVendorInformation
