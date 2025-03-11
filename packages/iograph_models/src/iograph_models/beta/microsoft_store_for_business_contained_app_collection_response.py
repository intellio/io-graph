from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftStoreForBusinessContainedAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[MicrosoftStoreForBusinessContainedApp]] = Field(alias="value",default=None,)

from .microsoft_store_for_business_contained_app import MicrosoftStoreForBusinessContainedApp

