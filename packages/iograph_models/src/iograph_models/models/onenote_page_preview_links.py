from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnenotePagePreviewLinks(BaseModel):
	previewImageUrl: Optional[ExternalLink] = Field(default=None,alias="previewImageUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .external_link import ExternalLink

