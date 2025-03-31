from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DeliveryOptimizationGroupIdSourceOptions(BaseModel):
	odata_type: Literal["#microsoft.graph.deliveryOptimizationGroupIdSourceOptions"] = Field(alias="@odata.type", default="#microsoft.graph.deliveryOptimizationGroupIdSourceOptions")
	groupIdSourceOption: Optional[DeliveryOptimizationGroupIdOptionsType | str] = Field(alias="groupIdSourceOption", default=None,)

from .delivery_optimization_group_id_options_type import DeliveryOptimizationGroupIdOptionsType
