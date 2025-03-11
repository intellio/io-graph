from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class VpnServer(BaseModel):
	address: Optional[str] = Field(alias="address",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	isDefaultServer: Optional[bool] = Field(alias="isDefaultServer",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


