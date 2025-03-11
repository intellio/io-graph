from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EntitlementsDataCollection(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	lastCollectionDateTime: Optional[datetime] = Field(alias="lastCollectionDateTime",default=None,)
	permissionsModificationCapability: Optional[PermissionsModificationCapability | str] = Field(alias="permissionsModificationCapability",default=None,)
	status: Optional[DataCollectionStatus | str] = Field(alias="status",default=None,)

from .permissions_modification_capability import PermissionsModificationCapability
from .data_collection_status import DataCollectionStatus

