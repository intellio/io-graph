from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Account(BaseModel):
	blocked: Optional[bool] = Field(alias="blocked", default=None,)
	category: Optional[str] = Field(alias="category", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[UUID] = Field(alias="id", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	number: Optional[str] = Field(alias="number", default=None,)
	subCategory: Optional[str] = Field(alias="subCategory", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

