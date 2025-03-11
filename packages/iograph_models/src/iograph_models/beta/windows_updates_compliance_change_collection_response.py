from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesComplianceChangeCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[WindowsUpdatesComplianceChange]]] = Field(alias="value",default=None,)

from .windows_updates_compliance_change import WindowsUpdatesComplianceChange

