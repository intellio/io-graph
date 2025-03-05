from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SharingLink(BaseModel):
	application: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="application",)
	preventsDownload: Optional[bool] = Field(default=None,alias="preventsDownload",)
	scope: Optional[str] = Field(default=None,alias="scope",)
	type: Optional[str] = Field(default=None,alias="type",)
	webHtml: Optional[str] = Field(default=None,alias="webHtml",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity import Identity

