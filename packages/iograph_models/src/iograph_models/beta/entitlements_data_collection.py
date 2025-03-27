from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EntitlementsDataCollection(BaseModel):
	odata_type: Literal["#microsoft.graph.entitlementsDataCollection"] = Field(alias="@odata.type", default="#microsoft.graph.entitlementsDataCollection")
	lastCollectionDateTime: Optional[datetime] = Field(alias="lastCollectionDateTime", default=None,)
	permissionsModificationCapability: Optional[PermissionsModificationCapability | str] = Field(alias="permissionsModificationCapability", default=None,)
	status: Optional[DataCollectionStatus | str] = Field(alias="status", default=None,)

from .permissions_modification_capability import PermissionsModificationCapability
from .data_collection_status import DataCollectionStatus

