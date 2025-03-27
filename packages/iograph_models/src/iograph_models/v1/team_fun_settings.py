from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamFunSettings(BaseModel):
	allowCustomMemes: Optional[bool] = Field(alias="allowCustomMemes", default=None,)
	allowGiphy: Optional[bool] = Field(alias="allowGiphy", default=None,)
	allowStickersAndMemes: Optional[bool] = Field(alias="allowStickersAndMemes", default=None,)
	giphyContentRating: Optional[GiphyRatingType | str] = Field(alias="giphyContentRating", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .giphy_rating_type import GiphyRatingType

