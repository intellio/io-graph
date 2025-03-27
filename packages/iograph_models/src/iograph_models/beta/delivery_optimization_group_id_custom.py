from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class DeliveryOptimizationGroupIdCustom(BaseModel):
	odata_type: Literal["#microsoft.graph.deliveryOptimizationGroupIdCustom"] = Field(alias="@odata.type", default="#microsoft.graph.deliveryOptimizationGroupIdCustom")
	groupIdCustom: Optional[str] = Field(alias="groupIdCustom", default=None,)


