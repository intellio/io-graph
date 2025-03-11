from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Entra(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	uxSetting: Optional[UxSetting] = Field(alias="uxSetting",default=None,)

from .ux_setting import UxSetting

