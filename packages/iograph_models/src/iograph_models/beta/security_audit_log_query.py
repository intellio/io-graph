from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityAuditLogQuery(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.auditLogQuery"] = Field(alias="@odata.type", default="#microsoft.graph.security.auditLogQuery")
	administrativeUnitIdFilters: Optional[list[str]] = Field(alias="administrativeUnitIdFilters", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	filterEndDateTime: Optional[datetime] = Field(alias="filterEndDateTime", default=None,)
	filterStartDateTime: Optional[datetime] = Field(alias="filterStartDateTime", default=None,)
	ipAddressFilters: Optional[list[str]] = Field(alias="ipAddressFilters", default=None,)
	keywordFilter: Optional[str] = Field(alias="keywordFilter", default=None,)
	objectIdFilters: Optional[list[str]] = Field(alias="objectIdFilters", default=None,)
	operationFilters: Optional[list[str]] = Field(alias="operationFilters", default=None,)
	recordTypeFilters: Optional[list[SecurityAuditLogRecordType | str]] = Field(alias="recordTypeFilters", default=None,)
	serviceFilters: Optional[list[str]] = Field(alias="serviceFilters", default=None,)
	status: Optional[SecurityAuditLogQueryStatus | str] = Field(alias="status", default=None,)
	userPrincipalNameFilters: Optional[list[str]] = Field(alias="userPrincipalNameFilters", default=None,)
	records: Optional[list[SecurityAuditLogRecord]] = Field(alias="records", default=None,)

from .security_audit_log_record_type import SecurityAuditLogRecordType
from .security_audit_log_query_status import SecurityAuditLogQueryStatus
from .security_audit_log_record import SecurityAuditLogRecord
