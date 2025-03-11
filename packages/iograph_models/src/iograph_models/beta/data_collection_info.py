from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DataCollectionInfo(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	entitlements: SerializeAsAny[Optional[EntitlementsDataCollectionInfo]] = Field(alias="entitlements",default=None,)

from .entitlements_data_collection_info import EntitlementsDataCollectionInfo

