from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MediaContentRatingFrance(BaseModel):
	movieRating: Optional[RatingFranceMoviesType | str] = Field(alias="movieRating", default=None,)
	tvRating: Optional[RatingFranceTelevisionType | str] = Field(alias="tvRating", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .rating_france_movies_type import RatingFranceMoviesType
from .rating_france_television_type import RatingFranceTelevisionType
