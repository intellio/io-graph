from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MediaContentRatingUnitedKingdom(BaseModel):
	movieRating: Optional[RatingUnitedKingdomMoviesType | str] = Field(alias="movieRating", default=None,)
	tvRating: Optional[RatingUnitedKingdomTelevisionType | str] = Field(alias="tvRating", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .rating_united_kingdom_movies_type import RatingUnitedKingdomMoviesType
from .rating_united_kingdom_television_type import RatingUnitedKingdomTelevisionType
