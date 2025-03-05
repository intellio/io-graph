from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SharingLink(BaseModel):
	application: SerializeAsAny[Optional[Identity]] = Field(alias="application",default=None,)
	preventsDownload: Optional[bool] = Field(alias="preventsDownload",default=None,)
	scope: Optional[str] = Field(alias="scope",default=None,)
	type: Optional[str] = Field(alias="type",default=None,)
	webHtml: Optional[str] = Field(alias="webHtml",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity import Identity

