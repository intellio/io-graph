from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PartnersBillingBlob(BaseModel):
	name: Optional[str] = Field(default=None,alias="name",)
	partitionValue: Optional[str] = Field(default=None,alias="partitionValue",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


