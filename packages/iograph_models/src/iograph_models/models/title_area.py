from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TitleArea(BaseModel):
	alternativeText: Optional[str] = Field(default=None,alias="alternativeText",)
	enableGradientEffect: Optional[bool] = Field(default=None,alias="enableGradientEffect",)
	imageWebUrl: Optional[str] = Field(default=None,alias="imageWebUrl",)
	layout: Optional[TitleAreaLayoutType] = Field(default=None,alias="layout",)
	serverProcessedContent: Optional[ServerProcessedContent] = Field(default=None,alias="serverProcessedContent",)
	showAuthor: Optional[bool] = Field(default=None,alias="showAuthor",)
	showPublishedDate: Optional[bool] = Field(default=None,alias="showPublishedDate",)
	showTextBlockAboveTitle: Optional[bool] = Field(default=None,alias="showTextBlockAboveTitle",)
	textAboveTitle: Optional[str] = Field(default=None,alias="textAboveTitle",)
	textAlignment: Optional[TitleAreaTextAlignmentType] = Field(default=None,alias="textAlignment",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .title_area_layout_type import TitleAreaLayoutType
from .server_processed_content import ServerProcessedContent
from .title_area_text_alignment_type import TitleAreaTextAlignmentType

