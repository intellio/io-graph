from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MediaContentRatingJapan(BaseModel):
	movieRating: Optional[RatingJapanMoviesType] = Field(default=None,alias="movieRating",)
	tvRating: Optional[RatingJapanTelevisionType] = Field(default=None,alias="tvRating",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .rating_japan_movies_type import RatingJapanMoviesType
from .rating_japan_television_type import RatingJapanTelevisionType

