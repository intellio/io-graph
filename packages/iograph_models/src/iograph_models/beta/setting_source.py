from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SettingSource(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	sourceType: Optional[SettingSourceType | str] = Field(alias="sourceType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .setting_source_type import SettingSourceType

