from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityTenantAllowBlockListEntryResultCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[SecurityTenantAllowBlockListEntryResult]] = Field(alias="value",default=None,)

from .security_tenant_allow_block_list_entry_result import SecurityTenantAllowBlockListEntryResult

