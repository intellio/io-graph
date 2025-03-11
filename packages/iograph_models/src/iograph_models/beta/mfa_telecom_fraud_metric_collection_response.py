from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MfaTelecomFraudMetricCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[MfaTelecomFraudMetric]] = Field(alias="value",default=None,)

from .mfa_telecom_fraud_metric import MfaTelecomFraudMetric

