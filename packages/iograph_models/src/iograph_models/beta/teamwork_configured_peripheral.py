from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkConfiguredPeripheral(BaseModel):
	isOptional: Optional[bool] = Field(alias="isOptional",default=None,)
	peripheral: Optional[TeamworkPeripheral] = Field(alias="peripheral",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .teamwork_peripheral import TeamworkPeripheral

