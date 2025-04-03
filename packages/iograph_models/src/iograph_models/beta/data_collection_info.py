from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class DataCollectionInfo(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.dataCollectionInfo"] = Field(alias="@odata.type", default="#microsoft.graph.dataCollectionInfo")
	entitlements: Optional[Union[EntitlementsDataCollection, NoEntitlementsDataCollection]] = Field(alias="entitlements", default=None,discriminator="odata_type", )

from .entitlements_data_collection import EntitlementsDataCollection
from .no_entitlements_data_collection import NoEntitlementsDataCollection
