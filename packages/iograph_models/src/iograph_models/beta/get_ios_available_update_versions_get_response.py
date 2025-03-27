from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_ios_available_update_versionsGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IosAvailableUpdateVersion]] = Field(alias="value", default=None,)

from .ios_available_update_version import IosAvailableUpdateVersion

