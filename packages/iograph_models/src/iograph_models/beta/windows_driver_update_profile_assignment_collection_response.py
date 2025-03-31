from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class WindowsDriverUpdateProfileAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[WindowsDriverUpdateProfileAssignment]] = Field(alias="value", default=None,)

from .windows_driver_update_profile_assignment import WindowsDriverUpdateProfileAssignment
