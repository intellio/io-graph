from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Endpoint(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	capability: Optional[str] = Field(default=None,alias="capability",)
	providerId: Optional[str] = Field(default=None,alias="providerId",)
	providerName: Optional[str] = Field(default=None,alias="providerName",)
	providerResourceId: Optional[str] = Field(default=None,alias="providerResourceId",)
	uri: Optional[str] = Field(default=None,alias="uri",)


