from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeliveryOptimizationGroupIdCustom(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	groupIdCustom: Optional[str] = Field(alias="groupIdCustom",default=None,)


