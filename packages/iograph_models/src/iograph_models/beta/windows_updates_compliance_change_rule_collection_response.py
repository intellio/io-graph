from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesComplianceChangeRuleCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[WindowsUpdatesComplianceChangeRule]]] = Field(alias="value",default=None,)

from .windows_updates_compliance_change_rule import WindowsUpdatesComplianceChangeRule

