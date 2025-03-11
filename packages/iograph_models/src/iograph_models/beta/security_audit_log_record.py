from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAuditLogRecord(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	administrativeUnits: Optional[list[str]] = Field(alias="administrativeUnits",default=None,)
	auditData: SerializeAsAny[Optional[SecurityAuditData]] = Field(alias="auditData",default=None,)
	auditLogRecordType: Optional[SecurityAuditLogRecordType | str] = Field(alias="auditLogRecordType",default=None,)
	clientIp: Optional[str] = Field(alias="clientIp",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	objectId: Optional[str] = Field(alias="objectId",default=None,)
	operation: Optional[str] = Field(alias="operation",default=None,)
	organizationId: Optional[str] = Field(alias="organizationId",default=None,)
	service: Optional[str] = Field(alias="service",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	userType: Optional[SecurityAuditLogUserType | str] = Field(alias="userType",default=None,)

from .security_audit_data import SecurityAuditData
from .security_audit_log_record_type import SecurityAuditLogRecordType
from .security_audit_log_user_type import SecurityAuditLogUserType

