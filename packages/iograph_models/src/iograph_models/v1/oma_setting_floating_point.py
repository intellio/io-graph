from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OmaSettingFloatingPoint(BaseModel):
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	omaUri: Optional[str] = Field(alias="omaUri",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	value: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric

