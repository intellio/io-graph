from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerPlanConfigurationBucketDefinition(BaseModel):
	externalBucketId: Optional[str] = Field(alias="externalBucketId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


