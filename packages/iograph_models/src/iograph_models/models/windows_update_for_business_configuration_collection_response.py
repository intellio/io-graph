from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdateForBusinessConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[WindowsUpdateForBusinessConfiguration]] = Field(alias="value",default=None,)

from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration

