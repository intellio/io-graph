from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MediaContentRatingUnitedKingdom(BaseModel):
	movieRating: Optional[RatingUnitedKingdomMoviesType] = Field(default=None,alias="movieRating",)
	tvRating: Optional[RatingUnitedKingdomTelevisionType] = Field(default=None,alias="tvRating",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .rating_united_kingdom_movies_type import RatingUnitedKingdomMoviesType
from .rating_united_kingdom_television_type import RatingUnitedKingdomTelevisionType

