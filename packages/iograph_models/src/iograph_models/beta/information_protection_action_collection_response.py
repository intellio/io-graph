from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InformationProtectionActionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[InformationProtectionAction]]] = Field(alias="value",default=None,)

from .information_protection_action import InformationProtectionAction

