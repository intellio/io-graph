from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnenotePagePreviewLinks(BaseModel):
	previewImageUrl: Optional[ExternalLink] = Field(alias="previewImageUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .external_link import ExternalLink
