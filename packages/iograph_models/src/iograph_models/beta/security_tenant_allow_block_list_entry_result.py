from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityTenantAllowBlockListEntryResult(BaseModel):
	entryType: Optional[SecurityTenantAllowBlockListEntryType | str] = Field(alias="entryType",default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime",default=None,)
	identity: Optional[str] = Field(alias="identity",default=None,)
	status: Optional[SecurityLongRunningOperationStatus | str] = Field(alias="status",default=None,)
	value: Optional[str] = Field(alias="value",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .security_tenant_allow_block_list_entry_type import SecurityTenantAllowBlockListEntryType
from .security_long_running_operation_status import SecurityLongRunningOperationStatus

