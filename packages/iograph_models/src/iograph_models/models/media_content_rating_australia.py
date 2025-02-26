from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MediaContentRatingAustralia(BaseModel):
	movieRating: Optional[RatingAustraliaMoviesType] = Field(default=None,alias="movieRating",)
	tvRating: Optional[RatingAustraliaTelevisionType] = Field(default=None,alias="tvRating",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .rating_australia_movies_type import RatingAustraliaMoviesType
from .rating_australia_television_type import RatingAustraliaTelevisionType

