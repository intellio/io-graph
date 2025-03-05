from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnenotePagePreview(BaseModel):
	links: Optional[OnenotePagePreviewLinks] = Field(default=None,alias="links",)
	previewText: Optional[str] = Field(default=None,alias="previewText",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .onenote_page_preview_links import OnenotePagePreviewLinks

