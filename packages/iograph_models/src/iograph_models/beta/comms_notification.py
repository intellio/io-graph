from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CommsNotification(BaseModel):
	changeType: Optional[ChangeType | str] = Field(alias="changeType", default=None,)
	resourceUrl: Optional[str] = Field(alias="resourceUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .change_type import ChangeType

