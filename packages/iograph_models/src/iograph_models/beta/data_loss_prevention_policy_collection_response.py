from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DataLossPreventionPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[DataLossPreventionPolicy]] = Field(alias="value", default=None,)

from .data_loss_prevention_policy import DataLossPreventionPolicy
