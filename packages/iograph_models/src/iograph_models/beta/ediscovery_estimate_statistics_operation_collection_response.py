from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EdiscoveryEstimateStatisticsOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[EdiscoveryEstimateStatisticsOperation]] = Field(alias="value", default=None,)

from .ediscovery_estimate_statistics_operation import EdiscoveryEstimateStatisticsOperation

