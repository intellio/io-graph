from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TitleArea(BaseModel):
	alternativeText: Optional[str] = Field(alias="alternativeText", default=None,)
	enableGradientEffect: Optional[bool] = Field(alias="enableGradientEffect", default=None,)
	imageWebUrl: Optional[str] = Field(alias="imageWebUrl", default=None,)
	layout: Optional[TitleAreaLayoutType | str] = Field(alias="layout", default=None,)
	serverProcessedContent: Optional[ServerProcessedContent] = Field(alias="serverProcessedContent", default=None,)
	showAuthor: Optional[bool] = Field(alias="showAuthor", default=None,)
	showPublishedDate: Optional[bool] = Field(alias="showPublishedDate", default=None,)
	showTextBlockAboveTitle: Optional[bool] = Field(alias="showTextBlockAboveTitle", default=None,)
	textAboveTitle: Optional[str] = Field(alias="textAboveTitle", default=None,)
	textAlignment: Optional[TitleAreaTextAlignmentType | str] = Field(alias="textAlignment", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .title_area_layout_type import TitleAreaLayoutType
from .server_processed_content import ServerProcessedContent
from .title_area_text_alignment_type import TitleAreaTextAlignmentType

