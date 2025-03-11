from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DeliveryOptimizationGroupIdSourceOptions(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	groupIdSourceOption: Optional[DeliveryOptimizationGroupIdOptionsType | str] = Field(alias="groupIdSourceOption",default=None,)

from .delivery_optimization_group_id_options_type import DeliveryOptimizationGroupIdOptionsType

