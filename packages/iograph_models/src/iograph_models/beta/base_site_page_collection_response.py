from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class BaseSitePageCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[NewsLinkPage, PageTemplate, SitePage, VideoNewsLinkPage],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .news_link_page import NewsLinkPage
from .page_template import PageTemplate
from .site_page import SitePage
from .video_news_link_page import VideoNewsLinkPage
