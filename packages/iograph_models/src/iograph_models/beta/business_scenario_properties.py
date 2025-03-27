from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class BusinessScenarioProperties(BaseModel):
	externalBucketId: Optional[str] = Field(alias="externalBucketId", default=None,)
	externalContextId: Optional[str] = Field(alias="externalContextId", default=None,)
	externalObjectId: Optional[str] = Field(alias="externalObjectId", default=None,)
	externalObjectVersion: Optional[str] = Field(alias="externalObjectVersion", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


