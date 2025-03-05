from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CommsNotification(BaseModel):
	changeType: Optional[ChangeType] = Field(default=None,alias="changeType",)
	resourceUrl: Optional[str] = Field(default=None,alias="resourceUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .change_type import ChangeType

