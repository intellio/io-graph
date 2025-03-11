from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnenotePagePreview(BaseModel):
	links: Optional[OnenotePagePreviewLinks] = Field(alias="links",default=None,)
	previewText: Optional[str] = Field(alias="previewText",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .onenote_page_preview_links import OnenotePagePreviewLinks

