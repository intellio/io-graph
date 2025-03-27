from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class DataCollectionInfo(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	entitlements: Optional[Union[EntitlementsDataCollection, NoEntitlementsDataCollection]] = Field(alias="entitlements", default=None,discriminator="odata_type", )

from .entitlements_data_collection import EntitlementsDataCollection
from .no_entitlements_data_collection import NoEntitlementsDataCollection

