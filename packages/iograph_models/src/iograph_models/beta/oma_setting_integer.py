from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class OmaSettingInteger(BaseModel):
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isEncrypted: Optional[bool] = Field(alias="isEncrypted", default=None,)
	omaUri: Optional[str] = Field(alias="omaUri", default=None,)
	secretReferenceValueId: Optional[str] = Field(alias="secretReferenceValueId", default=None,)
	odata_type: Literal["#microsoft.graph.omaSettingInteger"] = Field(alias="@odata.type", default="#microsoft.graph.omaSettingInteger")
	isReadOnly: Optional[bool] = Field(alias="isReadOnly", default=None,)
	value: Optional[int] = Field(alias="value", default=None,)


