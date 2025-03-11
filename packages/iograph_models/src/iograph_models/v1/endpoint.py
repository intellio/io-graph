from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Endpoint(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	capability: Optional[str] = Field(alias="capability",default=None,)
	providerId: Optional[str] = Field(alias="providerId",default=None,)
	providerName: Optional[str] = Field(alias="providerName",default=None,)
	providerResourceId: Optional[str] = Field(alias="providerResourceId",default=None,)
	uri: Optional[str] = Field(alias="uri",default=None,)


