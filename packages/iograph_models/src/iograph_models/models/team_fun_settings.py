from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamFunSettings(BaseModel):
	allowCustomMemes: Optional[bool] = Field(default=None,alias="allowCustomMemes",)
	allowGiphy: Optional[bool] = Field(default=None,alias="allowGiphy",)
	allowStickersAndMemes: Optional[bool] = Field(default=None,alias="allowStickersAndMemes",)
	giphyContentRating: Optional[GiphyRatingType] = Field(default=None,alias="giphyContentRating",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .giphy_rating_type import GiphyRatingType

