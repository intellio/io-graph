from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ResponsibleSensitiveType(BaseModel):
	description: Optional[str] = Field(alias="description", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	publisherName: Optional[str] = Field(alias="publisherName", default=None,)
	rulePackageId: Optional[str] = Field(alias="rulePackageId", default=None,)
	rulePackageType: Optional[str] = Field(alias="rulePackageType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


