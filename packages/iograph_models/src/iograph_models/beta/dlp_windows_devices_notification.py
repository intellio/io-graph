from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DlpWindowsDevicesNotification(BaseModel):
	author: Optional[str] = Field(alias="author",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	contentName: Optional[str] = Field(alias="contentName",default=None,)
	lastModfiedBy: Optional[str] = Field(alias="lastModfiedBy",default=None,)


