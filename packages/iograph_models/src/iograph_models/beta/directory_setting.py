from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DirectorySetting(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	templateId: Optional[str] = Field(alias="templateId",default=None,)
	values: Optional[list[SettingValue]] = Field(alias="values",default=None,)

from .setting_value import SettingValue

