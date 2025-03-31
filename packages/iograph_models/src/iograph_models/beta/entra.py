from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Entra(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.entra"] = Field(alias="@odata.type",)
	uxSetting: Optional[UxSetting] = Field(alias="uxSetting", default=None,)

from .ux_setting import UxSetting
