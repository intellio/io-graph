from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OmaSettingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[OmaSetting]]] = Field(alias="value",default=None,)

from .oma_setting import OmaSetting

