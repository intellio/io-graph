from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppRequirementCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[Win32LobAppRequirement]]] = Field(alias="value",default=None,)

from .win32_lob_app_requirement import Win32LobAppRequirement

