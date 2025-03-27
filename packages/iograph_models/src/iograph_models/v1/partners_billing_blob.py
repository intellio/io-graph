from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PartnersBillingBlob(BaseModel):
	name: Optional[str] = Field(alias="name", default=None,)
	partitionValue: Optional[str] = Field(alias="partitionValue", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


