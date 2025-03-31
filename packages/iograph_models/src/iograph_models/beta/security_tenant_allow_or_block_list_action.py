from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityTenantAllowOrBlockListAction(BaseModel):
	action: Optional[SecurityTenantAllowBlockListAction | str] = Field(alias="action", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	note: Optional[str] = Field(alias="note", default=None,)
	results: Optional[list[SecurityTenantAllowBlockListEntryResult]] = Field(alias="results", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .security_tenant_allow_block_list_action import SecurityTenantAllowBlockListAction
from .security_tenant_allow_block_list_entry_result import SecurityTenantAllowBlockListEntryResult
