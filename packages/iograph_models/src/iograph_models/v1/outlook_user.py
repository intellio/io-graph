from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OutlookUser(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	masterCategories: Optional[list[OutlookCategory]] = Field(alias="masterCategories", default=None,)

from .outlook_category import OutlookCategory

