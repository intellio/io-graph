from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Schema(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	baseType: Optional[str] = Field(alias="baseType",default=None,)
	properties: Optional[list[Property]] = Field(alias="properties",default=None,)

from .property import Property

